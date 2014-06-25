# pylint: disable=locally-disabled,missing-docstring,too-many-public-methods
# The above is ONLY permissible in test suites
import unittest
import CRABAPI
class test_TopLevel(unittest.TestCase):
    def test_getTask_notimpl(self):
        self.assertRaises(NotImplementedError, CRABAPI.getTask, "")
