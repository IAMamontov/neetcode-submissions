class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
        for current_string in strs:
            result_string += str(len(current_string))
            result_string += "#"
            result_string += current_string
        return result_string

    def decode(self, s: str) -> List[str]:
        delimiter = "#"
        result_list = []
        temp_string = ""
        counter = 0
        counter_str = ""
        len_flag = True
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result_list.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result_list

