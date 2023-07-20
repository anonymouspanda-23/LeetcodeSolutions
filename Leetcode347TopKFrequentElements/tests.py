import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_result = [1, 2]
        assert self.solution_instance.topKFrequent(nums, k) == expected_result

    def test_two(self):
        nums = [1]
        k = 1
        expected_result = [1]
        assert self.solution_instance.topKFrequent(nums, k) == expected_result


if __name__ == '__main__':
    unittest.main()
