from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = [1] * len(nums)
        postfix = 1

        # use the first pass to store the values of the prefix product in the output array
        for i in range(len(nums) - 1):
            output_array[i + 1] = output_array[i] * nums[i]

        # then use this second pass to compute the postfix products and multiply them by the prefix products, then store
        # them in the output array
        for i in range(len(nums) - 1, -1, -1):
            output_array[i] = output_array[i] * postfix
            postfix = postfix * nums[i]

        return output_array
