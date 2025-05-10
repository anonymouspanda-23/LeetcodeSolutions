# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the sum of both lists.
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # Get the number of zeros in each list.
        zeros1 = 0
        zeros2 = 0

        for num in nums1:
            if num == 0:
                zeros1 += 1

        for num in nums2:
            if num == 0:
                zeros2 += 1

        # If either list does not have zeros, then see if list with zeros is greater.
        # If yes, then it is impossible to get an equal sum.
        if (
                zeros1 == 0 and sum2 + zeros2 > sum1
        ) or (
            zeros2 == 0 and sum1 + zeros1 > sum2
        ):
            return -1

        min_sum = max(sum1 + zeros1, sum2 + zeros2)
        return min_sum
