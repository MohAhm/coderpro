class Solution(object):
    def searchRange(self, arr, target):
        # Time: O(log(n))
        # Space: O(log(n))
        first = self.binarySearch(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearch(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1

        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)

        else:
            if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))