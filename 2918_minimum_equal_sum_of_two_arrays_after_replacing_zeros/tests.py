import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        nums1 = [3, 2, 0, 1, 0]
        nums2 = [6, 5, 0]
        expected_output = 12
        assert self.solution_instance.minSum(nums1, nums2) == expected_output

    def test_two(self):
        nums1 = [2, 0, 2, 0]
        nums2 = [1, 4]
        expected_output = -1
        assert self.solution_instance.minSum(nums1, nums2) == expected_output


if __name__ == '__main__':
    unittest.main()
