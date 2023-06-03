import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        nums = [1, 2, 3, 1]
        expected_result = True
        assert self.solution_instance.containsDuplicate(nums) == expected_result

    def test_two(self):
        nums = [1, 2, 3, 4]
        expected_result = False
        assert self.solution_instance.containsDuplicate(nums) == expected_result

    def test_three(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected_result = True
        assert self.solution_instance.containsDuplicate(nums) == expected_result


if __name__ == '__main__':
    unittest.main()
