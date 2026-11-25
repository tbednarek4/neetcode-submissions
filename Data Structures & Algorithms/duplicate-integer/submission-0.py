# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums)) # set contains only unique elements