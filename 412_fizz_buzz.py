#First attempt from me
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range(1, n+1):
            if (i%3 == 0 and i%5 == 0):
                list.append("FizzBuzz")
            elif (i%3 == 0 and i%5 !=0 ):
                list.append("Fizz")
            elif (i%5 ==0 and i%3 !=0):
                list.append("Buzz")
            else:
                list.append(str(i))
        return list
    
    
#Approach 2: String Concatenation
#Much better approach in solution
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ""

            if divisible_by_3:
                # Divides by 3
                num_ans_str += "Fizz"
            if divisible_by_5:
                # Divides by 5
                num_ans_str += "Buzz"
            if not num_ans_str:
                # Not divisible by 3 or 5
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)  

        return ans
