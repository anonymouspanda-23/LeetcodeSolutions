from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count occurrence of each element in nums and store into a hashmap. -- O(n) time.
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0

            hashmap[num] += 1

        # Convert dictionary into a list. -- O(n) time.
        hashmap = [(num, occurrences) for num, occurrences in hashmap.items()]

        # Sort dictionary by the number of occurrences in increasing order. -- O(n log n) time.
        hashmap.sort(key=lambda x: x[1])

        # Retrieve the top k frequent elements from the list. -- O(k) time.
        k_frequent_elements = []

        for i in range(k):
            k_frequent_elements.append(hashmap.pop(-1)[0])

        return k_frequent_elements
