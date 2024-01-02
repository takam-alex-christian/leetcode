
class Solution:
    def maxArea(self, height: list[int]) -> int:

        left, right = 0, len(height) - 1

        max_area = 0

        while left < len(height) - 1 and right > 0:

            if abs(left - right) * min(height[left], height[right]) > max_area:
                max_area = abs(left - right) * min(height[left], height[right])

            if left == len(height) - 2 or right == 1:
                break

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            elif height[left] == height[right]:

                if left <= len(height) - 2 and right >= 1:

                    if height[left + 1] > height[right - 1]:
                        right -= 1

                    elif height[right - 1] > height[left + 1]:
                        left += 1

                    else:
                        left += 1



                print(f"left: {left} & right: {right} max: {max_area}")

        return max_area

sampleSolution = Solution()
height = [1,2,1]
print(sampleSolution.maxArea(height))
