class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        return self.split(nums, 0, len(nums))


    def split(self, nums, l, r):
        n = r-l
        if n == 1:
            return l
        if n == 2:
            if nums[l] > nums[l+1]:
                return l
            else:
                return l+1
        mid = l + (n//2)

        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        
        if nums[mid-1] > nums[mid]:
            return self.split(nums, l, mid)
        else:
            return self.split(nums, mid+1, r)
    
