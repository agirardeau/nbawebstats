import requests
import json
import dateutil.parser
from os import path
from abc import ABCMeta, abstractmethod


_REQUEST_DATA_PATH = path.join(path.dirname(path.abspath(__file__)), "requests.json")

class WebInterface:
    def __init__(self):
        with open(_REQUEST_DATA_PATH, 'r') as f:
            request_data = json.load(f)

        self.param_types = {x: ParamType(x, y)
                for x, y in request_data['params'].items()}
        self.request_types = {x: RequestType(x, y, self.param_types)
                for x, y in request_data['requests'].items()}

    def request(request_name, params):
        self.request_types[request_name].send(params)

class _RequestType:
    #TODO
    def __init__(self, name, data, param_types):
        pass

    def send(self, params):
        pass

    def _label_result_sets(result_set_list):
        pass

_PARAM_TYPE_NAME_MAP = {
        'int': _IntParamType,
        'season': _SeasonParamType,
        'season-id': _SeasonIdParamType,
        'boolean-yn': _BooleanYNParamType,
        'boolean-01': _Boolean01ParamType,
        'enum': _EnumParamType,
        'enum-mapped': _MappedEnumParamType,
        'date': _DateParamType
}

def _construct_param_type_from_json(name, data):
    return _PARAM_TYPE_NAME_MAP[data['type']](name, data)

class _ParamType(metaclass=ABCMeta):
    def __init__(self, name, data):
        self.name = name
        self.description = data.get('description', '')

        self.default_string = data.get('default')
        self.has_default = (self.default_string is not None)
        if self.has_default:
            if self.default_string:
                self.default_value = self._parse(self.default_string)
                self.default_formatted = self.format_value(self.default_value)
            else:
                self.default_value = None
                self.default_formatted = ""

    def _parse(self, text):
        return text

    def format_value(self, value):

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

class _BooleanParamType(_ParamType, metaclass=ABCMeta):
    def _parse(self, text):
        return {'True': True, 'False': False}[text]

class _BooleanYNParamType(_BooleanParamType):
    def format_value(self, value):
        return 'y' if value else 'n'

class _Boolean01ParamType(_BooleanParamType):
    def format_value(self, value):
        return '1' if value else '0'

class _EnumParamType(_ParamType):
    def __init__(self, name, data):
        super().__init__(self, name, data)
        self.options = data['options']

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
        return dateutil.parser.parse(text)

    def format_value(self, value):
        return str(value)
