import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        s = "abcyy"
        t = 2
        expected_output = 7
        assert self.solution_instance.lengthAfterTransformations(s, t) == expected_output

    def test_two(self):
        s = "azbk"
        t = 1
        expected_output = 5
        assert self.solution_instance.lengthAfterTransformations(s, t) == expected_output

    def test_three(self):
        s = "jqktcurgdvlibczdsvnsg"
        t = 7517
        expected_output = 79033769
        assert self.solution_instance.lengthAfterTransformations(s, t) == expected_output


if __name__ == '__main__':
    unittest.main()
