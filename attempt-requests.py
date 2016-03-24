#!/usr/bin/env python

import sys
import nbawebstats
import requests_cache
import pickle

requests_cache.install_cache('response-cache')


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
    else:
        raise ValueError()


def attempt(request_name):
    request_type = nbawebstats._REQUEST_TYPES[request_name]

    params = {}
    for param_type in request_type.params:
        if not param_type.has_default:
            params[param_type.name] = get_default_value(param_type.name)

    result = {}
    try:
        nbawebstats.request_stats(request_name, params)
        result['outcome'] = 'Success'
    except nbawebstats.HTTPResponseError as e:
        result['outcome'] = 'Failure - {0} {1}'.format(type(e).__name__, e)
        result['response'] = e.server_response
    except Exception as e:
        result['outcome'] = 'Failure - {0} {1}'.format(type(e).__name__, e)

    return result


if __name__ == '__main__':
    requests_to_try = sys.argv[1:]
    if not requests_to_try:
        requests_to_try = sorted(list(nbawebstats._REQUEST_TYPES.keys()))
        requests_to_try = sorted([x for x in nbawebstats._REQUEST_TYPES.keys()
                                  if nbawebstats._REQUEST_TYPES[x].status
                                  not in ['restricted', 'deprecated']])

    results = {}
    for request_name in sorted(requests_to_try):
        results[request_name] = attempt(request_name)
        print('{0}: {1}'.format(request_name,
                                results[request_name]['outcome']))

    with open('test-results.pickle', 'wb') as f:
        pickle.dump(results, f)
