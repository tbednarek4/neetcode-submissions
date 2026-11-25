# Time complexity: O(n)
# Space complexity: O(n) output + O(1) extra space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * (len(nums))
        
        prefix = 1
        for index in range(len(nums)):
            results[index] = prefix
            prefix *= nums[index]
        
        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            results[index] *= postfix
            postfix *= nums[index]
        
        return results