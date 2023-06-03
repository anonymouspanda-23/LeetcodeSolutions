import unittest
from solution import Solution


class TestCases(unittest.TestCase):
    solution_instance = Solution()

    def test_one(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert sorted(self.solution_instance.groupAnagrams(strs)) == sorted(expected_output)

    def test_two(self):
        strs = [""]
        expected_output = [[""]]
        assert sorted(self.solution_instance.groupAnagrams(strs)) == sorted(expected_output)

    def test_three(self):
        strs = ["a"]
        expected_output = [["a"]]
        assert sorted(self.solution_instance.groupAnagrams(strs)) == sorted(expected_output)


if __name__ == '__main__':
    unittest.main()
