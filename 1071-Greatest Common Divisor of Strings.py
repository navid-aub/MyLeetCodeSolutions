class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        length1 = len(str1)
        length2 = len(str2)
        
        if length2 > length1:
            str1,str2 = str2,str1
            length1,length2 = length2,length1
        
        output = ""
        for length in range(length2,0,-1):
            if length2/length == length2//length:
                pattern = str2[:length]
                count = str2.split(pattern).count("")
                if count > length2//length:            
                    count = str1.split(pattern).count("")
                    if count > length1//length:
                        return pattern

        return output
