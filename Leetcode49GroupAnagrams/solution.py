from typing import List
from bisect import insort


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sorted_string = str(sorted(string))

            if sorted_string not in anagrams:
                anagrams[sorted_string] = []

            insort(anagrams[sorted_string], string)

        return list(anagrams.values())
