from operator import *


class Solution:

    def diffWaysToCompute(self, input):
        functions = {"+": add, "-": sub, "*": mul}
        results = []
        flag = True
        for i, ch in enumerate(input):
            if ch in functions:
                l = self.diffWaysToCompute(input[0:i])
                r = self.diffWaysToCompute(input[i+1:])
                results.extend(self.compute(l, r,ch))
                flag = False
        if flag:
            return [int(input)]
        results.sort()
        return results

    def compute(self, nums1, nums2, op):
        functions = {"+": add, "-": sub, "*": mul}
        results = []
        for num1 in nums1:
            for num2 in nums2:
                result = functions[op](num1, num2)
                results.append(result)
        return results

print(Solution().diffWaysToCompute("12*3-4*5"))
