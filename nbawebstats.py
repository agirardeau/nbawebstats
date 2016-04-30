"""Module containing funcitonality for interfacing with the
stats.nba.com HTTP interface."""
import requests
import json
from os import path
from abc import ABCMeta, abstractmethod
from collections import OrderedDict


__version__ = '0.1.2'
_HTTP_HEADERS = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; WOW64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/48.0.2564.82 '
                   'Safari/537.36'),
    'Accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
               'image/webp,*/*;q=0.8'),
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}


class HTTPResponseError(Exception):
    """Error indicating that the stats.nba.com server returned an
    unexpected status code.

    Attributes:
        server_response (requests.models.Response): Response given by
            the server. May contain useful information about the reason
            for the failure.
    """
    def __init__(self, server_response):
        self.server_response = server_response

    def __repr__(self):
        return ("Server returned unexpected HTTP status code {}"
                .format(self.server_response.status_code))


def request_stats(request_name, params={}, **kwargs):
    """Send an HTTP request to stats.nba.com.

    Args:
        request_name (str): Identifier to the request type.
        params (dict): Dictionary of paramters to the request.
            Any parameters not provided in this argument will be set
            to default vaues. Some paramters do not have default
            values; all of these must be provided. See the
            documantation for individual request types for which
            parameters they accept. A parameter may be left unspecified
            by providing an empty string.
        kwargs: Any additional keyword arguments that would be accepted
            by requests.get().

    Returns:
        dict: Dictionary containing fields specific to the
            request type.
    """
    return _REQUEST_TYPES[request_name].send(params, **kwargs)


class _RequestType:

    def __init__(self, name, data, param_types):
        self.name = name
        self.endpoint = data['endpoint']
        self.params = [param_types[x] for x in data['params']]
        self.response_format = data['response-format']
        if self.response_format == 'result-set':
            self.outputs = [x[0] for x in data['returns']]
        self.url_param = data.get('url-param')
        self.status = data.get('status', 'supported')

    def send(self, params, **kwargs):
        params_composed = self._compose_params(params)

        url = 'http://stats.nba.com/{0}?'.format(self.endpoint)
        if self.url_param is not None:
            url = url.format(params_composed.pop(self.url_param))

        response = requests.get(url,
                                params=params_composed,
                                headers=_HTTP_HEADERS,
                                **kwargs)

        if not (response.status_code >= 200 and response.status_code <= 399):
            raise HTTPResponseError(response)

        if self.response_format == 'result-set':
            if 'resultSets' in response.json().keys():
                return self._label_result_sets(response.json()['resultSets'])
            else:
                # The response from the league-leaders request has a typo. This
                # accounts for that.
                return self._label_result_sets(response.json()['resultSet'])
        else:
            return response.json()

    def _compose_params(self, param_values_provided):
        params_composed = {}
        for param in self.params:
            if param.name in param_values_provided:
                value_provided = param_values_provided[param.name]
                params_composed[param.name] = \
                    param.format_value(value_provided)
            else:
                if param.has_default:
                    params_composed[param.name] = param.default_formatted
                else:
                    raise ValueError("Request {0} is missing parameter {1}."
                                     .format(self.name, param.name))

        return params_composed

    def _label_result_sets(self, result_set_list):
        results = OrderedDict()
        if isinstance(result_set_list, list):
            for output, index in zip(self.outputs, range(len(self.outputs))):
                results[output] = \
                        self._extract_result_set(result_set_list[index])
        else:
            results[self.outputs[0]] = \
                    self._extract_result_set(result_set_list)

        return results

    def _extract_result_set(self, result_set):
            headers = result_set['headers']
            values = result_set['rowSet']
            return [dict(zip(headers, x)) for x in values]


class _ParamType(metaclass=ABCMeta):
    def __init__(self, name, data):
        self.name = name

        self.default_string = data.get('default')
        self.has_default = (self.default_string is not None)
        if self.has_default:
            if self.default_string != '':
                self.default_value = self._parse(self.default_string)
                self.default_formatted = self.format_value(self.default_value)
            else:
                self.default_value = None
                self.default_formatted = ""

    @abstractmethod
    def _parse(self, text):
        """Parse argument value from string"""

    @abstractmethod
    def format_value(self, value):
        """Format argument value into string to be used in HTTP request"""


class _IntParamType(_ParamType):
    def _parse(self, text):
        return int(text)

    def format_value(self, value):
        return value


class _SeasonParamType(_IntParamType):
    def format_value(self, value):
        if value < 1000 or value > 9999:
            raise ValueError("Seasons should be four digit integers")
        next_year_two_digits = str(int(value) % 100 + 1)[-2:].zfill(2)
        return '{0}-{1}'.format(value, next_year_two_digits)


class _SeasonIDParamType(_IntParamType):
    def format_value(self, value):
        if value < 1000 or value > 9999:
            raise ValueError("Seasons should be four digit integers")
        return '2{0}'.format(value)


class _BooleanParamType(_ParamType):
    def _parse(self, text):
        return {'True': True, 'False': False}[text]


class _BooleanYNParamType(_BooleanParamType):
    def format_value(self, value):
        return 'Y' if value else 'N'


class _Boolean01ParamType(_BooleanParamType):
    def format_value(self, value):
        return '1' if value else '0'


class _EnumParamType(_ParamType):
    def __init__(self, name, data):
        self.options = data['options']
        super().__init__(name, data)

    def _parse(self, text):
        return text

    def format_value(self, value):
        if value not in self.options:
            raise ValueError(("Unrecognized value '{0}' for option "
                              "'{1}'. Options are [{2}]")
                             .format(value, self.name, self.options))
        return value


class _MappedEnumParamType(_EnumParamType):
    def format_value(self, value):
        if value not in self.options:
            raise ValueError(("Unrecognized value '{0}' for option "
                              "'{1}'. Options are [{2}]")
                             .format(value, self.name,
                                     list(self.options.keys())))
        return self.options[value]


class _DateParamType(_ParamType):
    def _parse(self, text):
        if not text:
            return None
        else:
            raise NotImplementedError

    def format_value(self, value):
        return str(value)


def _construct_param_type_from_json(name, data):
    param_type_map = {
            'int': _IntParamType,
            'season': _SeasonParamType,
            'season-id': _SeasonIDParamType,
            'boolean-yn': _BooleanYNParamType,
            'boolean-01': _Boolean01ParamType,
            'enum': _EnumParamType,
            'enum-mapped': _MappedEnumParamType,
            'date': _DateParamType,
    }

    return param_type_map[data['type']](name, data)


def _load_request_metadata():
    request_data_path = path.join(path.dirname(path.abspath(__file__)),
                                  "nbawebstats/requests.json")

    with open(request_data_path, 'r') as f:
        request_data = json.load(f)

    param_types = {x: _construct_param_type_from_json(x, y)
                   for x, y in request_data['params'].items()}
    request_types = {x: _RequestType(x, y, param_types)
                     for x, y in request_data['requests'].items()}

    return request_types


_REQUEST_TYPES = _load_request_metadata()
