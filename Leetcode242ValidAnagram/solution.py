class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths of s and t are different, they cannot be anagrams, therefore we return False
        if len(s) != len(t):
            return False

        # we now loop through all the unique characters in s and check if the number of occurrences of this character is equal in both s and t
        for char in set(s):
            # if the number of occurrences of this character is unequal in both s and t, return False
            if s.count(char) != t.count(char):
                return False

        # if the for loop completed without returning False, both strings have the same number of each character, and are therefore anagrams, hence we return True
        return True
