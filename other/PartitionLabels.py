class Solution:
    def partitionLabels(self, S: str):
        if len(S)==0:
            return []
        list = []
        flag = True
        for i in range(1,len(S)):
            str1 = S[:i]
            str2 = S[i:]
            if self.compareSet(str1,str2):
                list1 = self.partitionLabels(str1)
                list2 = self.partitionLabels(str2)
                flag = False
                break
        if flag:
            return [len(S)]
        list.extend(list1)
        list.extend(list2)
        return list

    def compareSet(self,str1: str, str2: str) -> bool:
        set1 = set()
        set2 = set()
        for ch in str1:
            set1.add(ch)
        for ch in str2:
            set2.add(ch)
        return len(set1.intersection(set2)) == 0

# https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode-solution/

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))