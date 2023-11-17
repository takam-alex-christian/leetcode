#compare the length of both strings
#use the shortest string's length upper loop limit
#for each iteration, apply binary addition of two digits, sum and cary
#add the cary
import math

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        formated_a = [int(x) for x in a]
        formated_b = [int(y) for y in b]

        formated_a = formated_a[::-1]
        formated_b = formated_b[::-1]

        result_list = []
        
        cary = 0

        if len(a) != len(b):
            if len(formated_a) > len(formated_b):
                formated_b.extend([0 for i in range(0, len(formated_a)-len(formated_b))])
            elif len(formated_b) > len(formated_a):
                formated_a.extend([0 for i in range(0, len(formated_b)-len(formated_a))])
        
        


        for i in range(0, len(formated_a)):
            sum = (formated_a[i] + formated_b[i] + cary) % 2
            cary = math.floor((formated_a[i] + formated_b[i] + cary ) / 2)

            result_list.append(sum)

        if cary != 0:
            result_list.append(cary)
        
        return ''.join(str(x) for x in result_list[::-1])
            
    
someSolution = Solution()
a = "11"
b = "1"

print(someSolution.addBinary(a, b))