import unittest
from dockshort import common

class TestCommon(unittest.TestCase):
    def split_on(self,token):
        tokens = ["a", "--", "b"]
        front,back = common.split_on_token(token, tokens)
        return front,back

    def extract_on(self, token, tokens = ["a", "-p", "target", "b"]):
        target, remains = common.extract_after_token(token, tokens)
        return target, remains

    def test_extract_target_found(self):
        target, remains = self.extract_on("-p")
        self.assertTrue(target == "target")

    def test_extract_target_remains(self):
        target, remains = self.extract_on("-p")
        self.assertTrue(''.join(remains) == "ab")

    def test_extract_target_not_found(self):
        target, remains = self.extract_on("-P")
        self.assertTrue(target == None)

    def test_extract_target_remains_not_found(self):
        target, remains = self.extract_on("-P")
        self.assertTrue(''.join(remains) == "a-ptargetb")
        

    def test_split_token_found_front(self):
        front,back = self.split_on("--")
        self.assertTrue(''.join(front) == "a" )

    def test_split_token_found_back(self):
        front,back = self.split_on("--")
        self.assertTrue(''.join(back) == "b" )

    def test_split_token_not_found_front(self):
        front,back = self.split_on("%%")
        self.assertTrue(''.join(front) == "a--b" )

    def test_split_token_not_found_back(self):
        front,back = self.split_on("%%")
        self.assertTrue(back == None )


    def test_args_check_less(self):
        ran_ok = common.args_check([1], 2)
        self.assertTrue( not ran_ok )

    def test_args_check_eq(self):
        ran_ok = common.args_check([1, 2], 2)
        self.assertTrue( ran_ok )

    def test_args_check_more(self):
        ran_ok = common.args_check([1, 2, 3], 2)
        self.assertTrue( ran_ok )

    # Note - not sure how to test the execution lines

unittest.main()
