#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import json
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(THIS_DIR, '../nbawebstats/requests.json'))
RST_PATH = os.path.abspath(os.path.join(THIS_DIR, 'requests.rst'))

def format_internal_link(name, domain):
    return ":ref:`{0} <{1}-{2}>`".format(name, domain, name.lower())

def with_default(request_params, global_param_map):
    return [x for x in request_params if 'default' in global_param_map[x]]

def without_default(request_params, global_param_map):
    return [x for x in request_params if 'default' not in global_param_map[x]]

def format_string_literals(strings):
    return ["``'{0}'``".format(x) for x in strings]

def format_param_links(param_names):
    return [format_internal_link(x, 'param') for x in param_names]

def format_param_type_link(param_type):
    param_type_name = {'int': 'Integer',
                      'boolean-yn': 'Boolean',
                      'boolean-01': 'Boolean',
                      'enum': 'Enumerated',
                      'enum-mapped': 'Enumerated',
                      'date': 'Date',
                      'season': 'Season',
                      'season-id': 'Season'}[param_type]

    return format_internal_link(param_type_name, 'type')

def update_request_rst():
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)

    jinja_env = Environment(loader=FileSystemLoader(THIS_DIR),
                            trim_blocks=True,
                            lstrip_blocks=True)

    jinja_env.filters['with_default'] = with_default
    jinja_env.filters['without_default'] = without_default
    jinja_env.filters['format_string_literals'] = format_string_literals
    jinja_env.filters['format_param_links'] = format_param_links
    jinja_env.filters['format_param_type_link'] = format_param_type_link

    rst_contents = jinja_env.get_template('requests.template').render(data)

    with open(RST_PATH, 'w') as f:
        f.write(rst_contents)

if __name__ == '__main__':
    update_request_rst()
