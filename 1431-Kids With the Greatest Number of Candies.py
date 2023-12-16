class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        hashed = {}
        mx = max(candies)
        for item in candies:
            if hashed.get(item):
                result.append(hashed.get(item))
            else:
                if item + extraCandies >= mx:
                    result.append(True)
                    hashed[item]=True
                else:
                    result.append(False)
                    hashed[item]=False
        return result
