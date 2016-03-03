#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
        "requests" ]

test_requirements = []

setup(
    name='pynba',
    version='0.0.3',
    description="Python interface to stats.nba.com HTTP API.",
    long_description=readme,
    author="Andrew Girardeau-Dale",
    author_email='agirardeaudale@gmail.com',
    url='https://github.com/agirardeaudale/pynba',
    packages=[
        'pynba',
    ],
    package_dir={'pynba':
                 'pynba'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pynba',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
