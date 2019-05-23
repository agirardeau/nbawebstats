.. highlight:: bash

===========
Development
===========

Clone the source code off Github::

    git clone http://github.com/agirardeaudale/nbawebstats
    cd nbawebstats

Install virtualenv as well as the relevant Python versions. On Ubuntu::

    sudo apt install virtualenv
    sudo add-apt-repository ppa:deadsnakes/ppa  # PPA for Python versions < 3.6 as of 2019
    sudo apt update
    sudo apt install python3.3
    sudo apt install python3.4
    sudo apt install python3.5

Create and activate virtual environment::

    virtualenv env -p `which python3.5`
    . env/bin/activate

Install development requirements::

    pip install -r requirements-dev.txt

Run tests::

    make test      # runs unit tests using current python version
    make test-all  # runs unit tests for all supported python versions
