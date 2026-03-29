class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            length = len(word)
            encoded_str += f'{length}#'
            encoded_str += word
        # print(f"encoded_str: {encoded_str}")
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # if s == "0#":
        #     return [""]

        return_list = []
        word = ""
        flagHash = True
        flagChar = False
        length = ""
        i = 0
        while i < len(s):
            letter = s[i]
            if flagHash and (not flagChar):
                if letter in "0123456789":
                    length += letter
                    # print(f"length append = {length,i}")
                    i+=1
                    continue
                elif letter == "#":
                    length = int(length)
                    if length == 0:
                        return_list.append("")
                        length = ""
                        word = ""
                        i+=1
                        continue
                    flagHash = False
                    flagChar = True
                    # print(f"lenght # finish {letter,i}")
                    i+=1
                    continue
            if flagChar and (not flagHash):
                word += letter
                # print(f"in elif {word,length} and i: {i}")
                length -= 1
                i+=1
                if length == 0:
                    flagChar = False
                    flagHash = True
                    return_list.append(word)
                    # print(f"Word appended!: {word}")
                    length = ""
                    word = ""
        return return_list
            



