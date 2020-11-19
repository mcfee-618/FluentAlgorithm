class Solution:

    brackets = set()
   
    def getBrackets(self,num):
        Solution.brackets=set()
        self.recursion("",0,num*2)
        return list(Solution.brackets)


    def recursion(self,value,length,num):
        if length==num:
            if self.isvalid_bracket(value):
                Solution.brackets.add(value)
        else:
            self.recursion(value+"(",length+1,num)
            self.recursion(value+")",length+1,num) 
    
    def isvalid_bracket(self,value):
        stack = []
        index = 0 
        while index!=len(value):
            if value[index] == "(":
                stack.append("(")
            else:
                if len(stack)==0:
                    return False
                if stack.pop()!="(":
                    return False
            index+=1
        return len(stack)==0
        
       
solution = Solution()
print(solution.getBrackets(1))
print(solution.getBrackets(2))
print(solution.getBrackets(3))


