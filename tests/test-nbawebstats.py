#!/usr/bin/env python
"""Unit test for nbawebstats.

Presently this test is very basic, only checking that the module imports
without error. Module functionality is checked by the test located at
tests/functional/test-requests.py.
"""

import unittest
import nbawebstats


class TestInterface(unittest.TestCase):
    def test_version(self):
        self.assertTrue(nbawebstats.__version__ is not None)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
