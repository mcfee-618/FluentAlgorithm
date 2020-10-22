class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        sequence_name = self.construct_sequence(name)
        sequence_typed = self.construct_sequence(typed)
        if len(sequence_typed) != len(sequence_name):
            return False
        for index, _ in enumerate(sequence_name):
            if sequence_name[index][0] != sequence_typed[index][0]:
                return False
            if sequence_name[index][1] > sequence_typed[index][1]:
                return False
        return True

    def construct_sequence(self, value: str):
        sequence = []
        current_ch = None
        current_num = None
        for ch in value:
            if current_ch == ch:
                current_num += 1
            else:
                if current_num is not None:
                    sequence.append((current_ch, current_num))
                current_ch = ch
                current_num = 1
        if current_num is not None:
            sequence.append((current_ch, current_num))
        return sequence


print(Solution().isLongPressedName("alex","aaleex"))

## https://leetcode-cn.com/problems/long-pressed-name/solution/chang-an-jian-ru-by-leetcode-solution/