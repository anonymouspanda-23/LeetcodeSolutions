# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = (10 ** 9) + 7

        # Initialize list of char counts to 0.
        char_counts = [0] * 26

        # Count number of chars in initial string.
        for char in s:
            char_counts[ord(char) - 97] += 1

        # Run transformation t times.
        for i in range(t):
            # Remove last index.
            temp = char_counts.pop()

            # Insert last index at start (z -> a).
            char_counts.insert(0, temp)

            # Insert last index at 'b' position. (z -> b).
            char_counts[1] += temp

        # Return number of characters modulo 10^9 + 7.
        return sum(char_counts) % MOD
