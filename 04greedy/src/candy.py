class Solution:
    def candy(self, ratings):
        left_array =  [1] * len(ratings)
        right_array = [1] * len(ratings)
        count=0
        for i in range(1,len(ratings)):
            if ratings[i]> ratings[i-1]:
                left_array[i] = left_array[i-1]+1
        count = left_array[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right_array[i]= right_array[i+1]+1
            count=max(right_array[i],left_array[i])+count
        return count

print(Solution().candy([1,0,2]))
                