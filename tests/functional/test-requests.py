#!/usr/bin/env python
"""
Functional test for nbawebstats. Tests whether each command is
is constructed suitably to garner a valid response from the
stats.nba.com server. Since it's success in dependent upon an outside
entity and a valid internet connection to function, it is not covered by
the unit tests and run as a part of continuous integration.
"""

import sys
import requests_cache
import pickle
import argparse
import json
from os.path import join, dirname, abspath

import nbawebstats

requests_cache.install_cache('response-cache')


def compare_string_lists(given, expected):
    results = {'missing': [], 'unexpected': []}

    for item in expected:
        if item not in given:
            results['missing'].append(item)

    for item in given:
        if item not in expected:
            results['unexpected'].append(item)

    return results


def compare_subfields(response, expected):
    mismatch_list = []

    for field_name, response_set, subfields_expected in \
            zip(response.keys(), response.values(), [x[1] for x in expected]):
        try:
            subfields_received = response_set[0].keys()        
        except IndexError:
            if subfields_expected:
                mismatch_list.append("Field {0} is empty.".format(field_name))
            continue

        comparison = compare_string_lists(subfields_received, subfields_expected)

        if comparison['missing']:
            mismatch_list.append(("{0} field declaration contains extraneous:\n"
                                  "        \"{1}\"")
                                 .format(field_name,
                                         '", "'.join(comparison['missing'])))

        if comparison['unexpected']:
            mismatch_list.append(("{0} field declaration is missing:\n"
                                  "        \"{1}\"")
                                 .format(field_name,
                                         '", "'.join(comparison['unexpected'])))

    return mismatch_list


def get_default_value(param_name):
    if param_name == 'TeamID':
        return '1610612764'  # 2015-16 Sacramento Kings
    elif param_name == 'PlayerID':
        return '202326'  # DeMarcus Cousins
    elif param_name == 'GameID':
        return '0021500391'  # Detroit @ Chicago, 2015-12-18
    elif param_name in ['Season', 'SeasonID', 'SeasonYear', 'Year']:
        return 2015
    elif param_name == 'StatCategory':
        return 'MIN'
    elif param_name == 'ClutchTime':
        return 'Last 5 Minutes'
    else:
        raise ValueError()


def attempt(request_name, request_data, verbose=False):
    request_type = nbawebstats._REQUEST_TYPES[request_name]

    params = {}
    for param_type in request_type.params:
        if not param_type.has_default or param_type.name == 'ClutchTime':
            params[param_type.name] = get_default_value(param_type.name)

    result = {}
    try:
        result['response'] = nbawebstats.request_stats(request_name,
                                                       params,
                                                       timeout=5)
        result['outcome'] = 'Success'
    except nbawebstats.HTTPResponseError as e:
        result['response'] = e.server_response
        result['outcome'] = 'Failure - {0} {1}'.format(type(e).__name__, e)
    except Exception as e:
        result['outcome'] = 'Failure - {0} {1}'.format(type(e).__name__, e)

    if result['outcome'] == 'Success' and verbose and 'returns' in request_data:
        comparison = compare_subfields(result['response'],
                                       request_data['returns'])
        if comparison:
            result['outcome'] = ('Subfield Mismatch\n    {0}'
                                 .format('\n    '.join(comparison)))

    return result


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=("Test request types defined "
        "in requests.json with the stats.nba.com server."))

    parser.add_argument("requests", nargs="*", help="List of requests to try.")
    parser.add_argument("-v", "--verbose", action="store_const", const=True,
            default=False, dest="verbose",
            help="verbose output, includes information about subfields.")

    args = parser.parse_args()

    if not args.requests:
        args.requests = sorted([x for x in nbawebstats._REQUEST_TYPES.keys()
                                if nbawebstats._REQUEST_TYPES[x].status
                                not in ['restricted', 'deprecated']])

    requests_data_filename = abspath(join(dirname(__file__),
                                          "../../nbawebstats/requests.json"))
    with open(requests_data_filename, "r") as f:
        request_data = json.load(f)['requests']

    results = {}
    for request_name in args.requests:
        results[request_name] = attempt(request_name,
                                        request_data[request_name],
                                        args.verbose)
        print('{0}: {1}'.format(request_name,
                                results[request_name]['outcome']))

    with open('test-results.pickle', 'wb') as f:
        pickle.dump(results, f)
