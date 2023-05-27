from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we begin by initializing a hash table using the python dictionary
        nums_dict = {}

        # we now loop through nums to populate nums_dict
        for idx, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [0]

            nums_dict[num][0] += 1
            nums_dict[num].append(idx)

        # finally, we loop through all the keys in nums_dict to find a number which when added to the key, gives target
        for key in nums_dict:
            # if there is no number, which when added with key, gives target, continue searching the other keys in nums_dict
            if target - key not in nums_dict:
                continue

            # if the number which, when added with key, gives target, does not have the same value as key, return this pair
            if target - key != key:
                first_index = nums_dict[key][1]
                second_index = nums_dict[target - key][1]
                return [first_index, second_index]

            # if the number which, when added with key, gives target, has the same value as key,
            # check if multiple instances of this number exists in the original list
            else:
                # if only 1 instance of this number exists, continue searching
                if nums_dict[key][0] < 2:
                    continue

                # if multiple instances of this number exist, return the first to indices
                else:
                    return nums_dict[key][1:3]
