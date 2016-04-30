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

version='0.1.2'

setup(
    name='nbawebstats',
    version=version,
    description="Python interface to stats.nba.com HTTP API.",
    long_description=readme,
    author="Andrew Girardeau-Dale",
    author_email='agirardeaudale@gmail.com',
    url='https://github.com/agirardeaudale/nbawebstats',
    download_url=('https://github.com/agirardeaudale/nbawebstats/tarball/v{0}'
                  .format(version)),
    packages=[
        'nbawebstats'
    ],
    py_modules=[
        'nbawebstats'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='nbawebstats',
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
