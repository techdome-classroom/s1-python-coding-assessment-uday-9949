import unittest
from program2 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        result = self.solution.decode_message("aa", "a")
        self.assertEqual(result, False)

    def test_case2(self):
        result = self.solution.decode_message("aa", "*")
        self.assertEqual(result, True)

    def test_case3(self):
        result = self.solution.decode_message("cb", "?a")
        self.assertEqual(result, False)

    def test_case4(self):
        result = self.solution.decode_message("abc", "?b?")
        self.assertEqual(result, True)

    def test_case5(self):
        result = self.solution.decode_message("ab", "ab*")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
