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
#24 ms	13.5 MB found in discussion
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highenough = max(candies) - extraCandies
        return [i >= highenough for i in candies]
