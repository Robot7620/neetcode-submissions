class Solution:
    def binarySearch(self, arr: List[int], target: int) -> bool:
        lo = 0
        hi = len(arr)-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if arr[mid] > target:
                hi = mid - 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)-1
        while lo<= hi:
            mid = lo + (hi-lo) // 2
            if matrix[mid][-1] > target:
                if matrix[mid][0] <= target:
                    return self.binarySearch(matrix[mid], target)
                else:
                    hi = mid - 1
            if matrix[mid][-1] < target:
                lo = mid + 1
            if matrix[mid][-1] == target:
                return True
        return False