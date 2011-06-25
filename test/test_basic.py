
from nsms_web_api import NSMS
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.nsms = NSMS('foo', 'test')

    def test_args(self):
        self.assertEqual (self.nsms.username, 'foo')
        self.assertEqual (self.nsms.password, 'test')

if __name__ == '__main__':
    print "1\n"
    unittest.main()

