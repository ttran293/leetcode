#https://codingbat.com/prob/p118406
#This code is from Hassan Raza
#Explaination: here goal%5<=small checks whether the remainder (i.e. the remaining inches after the big brick is used) can be fulfilled by the small bricks 
#(so if it is greater than the small bricks then it will return false else if small is greater than the remainder then it will return True as the number of bricks is sufficient). 
#(goal-(big*5))<=small here means to check whether the total number of inches of big bricks and small bricks are sufficient enough to complete the goal. 
#Instead of (goal-(big*5))<=small we can also use goal<=big*5+small as it may seem more clear and well-explained. 
def make_bricks(small, big, goal):
    return (goal%5)<=small and (goal-(big*5))<=small
