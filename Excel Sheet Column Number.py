import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = 0
        self.assertEqual(Solution().titleToNumber(Input),Output)
    def testSample(self):
        Input = "AAA"
        Output = 703
        self.assertEqual(Solution().titleToNumber(Input),Output)

class Solution():
    def titleToNumber(self, s):
        if s == "":
            return 0
        Ans = 0
        for i in range(len(s)):
            Ans *= 26
            Ans += ord(s[i]) - ord("A") + 1
        return Ans
if __name__ == '__main__':
    unittest.main()
