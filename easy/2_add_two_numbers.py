from math import floor

class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        #find the smaller number
        #give it leading zeroes
        #loop through the numbers
        #sum each iterables at the same index with the carry and push the result to the output number list
        #update carry value

        #if the value of the carry at the end of the loop is non zero, push this value to the output number

        number1 = l1.copy()
        number2 = l2.copy()

        output_number = []

        carry = 0

        if len(number1) > len(number2):
            number2.extend([0 for i in range(0, len(number1) - len(number2))])
        elif len(l1) < len(l2):
            number1.extend([0 for i in range(0, len(number2) - len(number1))])
        else: 
            pass
        
        for i in range(0, len(number1)):
            total = number1[i] + number2[i] + carry

            output_number.append(total % 10)

            carry = floor(total / 10)

        if carry > 0:
            output_number.append(carry)
        
        return output_number

newSol = Solution()
newSol.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])