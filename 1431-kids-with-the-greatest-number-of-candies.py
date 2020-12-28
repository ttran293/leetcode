#32 ms	13.3 MB
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        for i in range (len(candies)):
            if candies[i] < (max(candies)-extraCandies):
                res.append(False)
            else:
                res.append(True)
        return res
