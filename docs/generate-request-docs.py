#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import json
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(THIS_DIR, '../pynba/requests.json'))

if __name__ == '__main__':
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)

    jinja_env = Environment(loader=FileSystemLoader(THIS_DIR),
                            trim_blocks=True,
                            lstrip_blocks=True)
    print(jinja_env.get_template('requests.template').render(data))
