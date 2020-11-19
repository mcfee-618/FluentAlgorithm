class Solution:

    brackets = set()
   
    def getBrackets(self,num):
        Solution.brackets=set()
        self.recursion("",0,0,num)
        return list(Solution.brackets)


    def recursion(self,value,left,right,num):
        if right > left or left > num:
            return
        if left + right == num*2:
            Solution.brackets.add(value)
            return
        if left == right:
            self.recursion(value+"(",left+1,right,num)
        else:
            self.recursion(value+"(",left+1,right,num)
            self.recursion(value+")",left,right+1,num)
        
        
       
solution = Solution()
print(solution.getBrackets(1))
print(solution.getBrackets(2))
print(solution.getBrackets(3))


# 回溯法：进行遍历解空间的大小

