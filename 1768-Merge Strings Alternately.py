class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        output = ""

        if length1 <= length2:
            length = length1
            flag = True
        else:
            length = length2
            flag = False
            
        for index in range(length):
                output = output + word1[index] + word2[index]
        
        if flag:
            output = output + word2[length:]
        else:
            output = output + word1[length:]
        
        return output
