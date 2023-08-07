import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        assert self.solution_instance.productExceptSelf(nums) == expected_output

    def test_two(self):
        nums = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        assert self.solution_instance.productExceptSelf(nums) == expected_output


if __name__ == '__main__':
    unittest.main()
