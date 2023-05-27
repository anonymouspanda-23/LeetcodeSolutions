from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set which will be used for storing the numbers in the list
        numbers = set()

        # loop through all the numbers in the list
        for num in nums:
            # if the number currently yielded by the generator already exists in the current set, return True
            if num in numbers:
                return True

            # if not, add the currently yielded number to the set created above
            numbers.add(num)

        # if the for loop completes, no duplicate numbers exist in the list, therefore we return False here.
        return False
