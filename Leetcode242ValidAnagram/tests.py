import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        s = "anagram"
        t = "nagaram"
        expected_result = True
        assert self.solution_instance.isAnagram(s, t) == expected_result

    def test_two(self):
        s = "rat"
        t = "car"
        expected_result = False
        assert self.solution_instance.isAnagram(s, t) == expected_result


if __name__ == '__main__':
    unittest.main()
