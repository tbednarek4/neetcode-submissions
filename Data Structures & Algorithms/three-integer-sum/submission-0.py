# Time complexity: O(n^2)
# Space complexity: O(n) hashmap + O(m) triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = {}

        for i in range(len(nums)):
            prevSeen = {}
            target = -nums[i]

            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in prevSeen:
                    temp = sorted([nums[i], nums[prevSeen[diff]], nums[j]])
                    triplets[tuple(temp)] = temp
                prevSeen[nums[j]] = j

        return list(triplets.values())