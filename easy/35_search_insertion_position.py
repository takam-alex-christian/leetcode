class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        #testing left extreme
        if nums[0] > target:
            return 0

        #testing right extreme
        if nums[-1] < target:
            return len(nums) -1
        
        
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            
            if nums[i] < target and i < len(nums) - 2:
                if nums[i + 1] > target:
                    return i + 1
            

someListOfNums = [1]
target = 2

someSolution = Solution()
print(someSolution.searchInsert(someListOfNums, target))
