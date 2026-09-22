class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""
        for current_string in strs:
            result_string += str(len(current_string))
            result_string += "#"
            result_string += current_string
        print(result_string)
        return result_string

    def decode(self, s: str) -> List[str]:
        delimiter = "#"
        result_list = []
        temp_string = ""
        counter = 0
        counter_str = ""
        len_flag = True
        for current_char in s:
            if len_flag == True:
                if current_char != delimiter:
                    counter_str += current_char
                else:
                    counter = int(counter_str)
                    if counter == 0:
                        result_list.append("")
                        continue
                    counter_str = ""
                    len_flag = False
            else:
                temp_string += current_char
                counter -= 1
                if counter == 0:
                    result_list.append(temp_string)
                    len_flag = True
                    temp_string = ""
        print(result_list)
        return result_list

