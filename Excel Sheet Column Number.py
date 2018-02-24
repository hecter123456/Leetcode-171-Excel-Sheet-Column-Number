import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = 0
        self.assertEqual(Solution().titleToNumber(Input),Output);

class Solution():
    def titleToNumber(self, s):
        if s == "":
            return 0
if __name__ == '__main__':
    unittest.main()
