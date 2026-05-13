from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for i in range(len(nums)):
            current = nums[i]
            length = 1

            while True:
                next_value = current + 1
                found_next = False

                for j in range(len(nums)):
                    if nums[j] == next_value:
                        found_next = True
                        break

                if found_next == False:
                    break

                current = next_value
                length += 1

            if length > longest:
                longest = length

        return longest