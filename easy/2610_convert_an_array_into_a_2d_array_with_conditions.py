class Solution:
    def find_matrix(self, nums: list[int]) -> list[list[int]]:

        nums_copy: list[int] = nums.copy()

        resulting_array: list[list[int]] = []

        while len(nums_copy) > 0:
            resulting_array.append([])

            for num in nums:
                if num not in resulting_array[-1]:
                    resulting_array[-1].append(num)
                    nums_copy.remove(num)

            nums = nums_copy.copy()

        return resulting_array

sampleSolution = Solution()
nums = [1,3,4,1,2,3,1]
print(sampleSolution.find_matrix(nums))

