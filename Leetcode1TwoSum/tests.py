import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def testOne(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_result = [0, 1]
        assert self.solution_instance.twoSum(nums, target) == expected_result

    def testTwo(self):
        nums = [3, 2, 4]
        target = 6
        expected_result = [1, 2]
        assert self.solution_instance.twoSum(nums, target) == expected_result

    def testThree(self):
        nums = [3, 3]
        target = 6
        expected_result = [0, 1]
        assert self.solution_instance.twoSum(nums, target) == expected_result


if __name__ == '__main__':
    unittest.main()
