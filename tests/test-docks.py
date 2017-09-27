import unittest
from dockshort import common

class TestCommon(unittest.TestCase):

    def test_split_token_found_front(self):
        tokens = ["a", "--", "b"]
        front,back = common.split_on_token("--", tokens)
        self.assertTrue(''.join(front) == "a" )

    def test_split_token_found_back(self):
        tokens = ["a", "--", "b"]
        front,back = common.split_on_token("--", tokens)
        self.assertTrue(''.join(back) == "b" )

    def test_split_token_not_found_front(self):
        tokens = ["a", "--", "b"]
        front,back = common.split_on_token("%%", tokens)
        self.assertTrue(''.join(front) == "a--b" )

    def test_split_token_not_found_back(self):
        tokens = ["a", "--", "b"]
        front,back = common.split_on_token("%%", tokens)
        self.assertTrue(back == None )

unittest.main()
