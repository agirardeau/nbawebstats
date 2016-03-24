#!/usr/bin/env python

import unittest
import nbawebstats


class TestInterface(unittest.TestCase):
    def test_something(self):
        self.assertTrue(nbawebstats.__version__ is not None)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
