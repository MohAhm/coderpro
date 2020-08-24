class Solution(object):
    def twoSumA(self, nums, target):
        # Brute Force Solution
        # Time: O(n^2)
        # Space: O(0)
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]

        return []

    def twoSumB(self, nums, target):
        # Time: O(n)
        # Space: O(n)
        values = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i

        return []

nums = [2, 7, 11, 15]
target = 18
print(Solution().twoSumB(nums, target))


