class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
        temp_list = []
        delimiter = "#"
        for current_string in strs:
            temp_list.append(str(len(current_string)))
            temp_list.append(delimiter)
            temp_list.append(current_string)
        result_string = "".join(temp_list)
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
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            result_list.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result_list
