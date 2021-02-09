//We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
//Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
//https://codingbat.com/prob/p191363

#include <iostream>
using namespace std;
int makeChocolate(int small, int big, int goal) {
    //small 1 kilo big 5 kilo use big bar before small 1x + 5y = Goal
    //5y = Goal -> return
    //if there is more than big bar

    if (big >= 1){
        if (goal < 5 && small == goal) return small;
        for (int i = big; i >=1; i--){
            if (5*i + small == goal) return small;
            if (goal - 5*i <= small && goal -5*i >=0) return goal-5*i;
        }
        return -1;
    }
    else {
        if (small == goal) return small;
    }
    
}


int main() {
    cout<<"Expect 4: " << makeChocolate(4,1,9) <<"\n";
    cout<<"Expect -1: " << makeChocolate(4,1,10) <<"\n";
    cout<<"Expect 2: " << makeChocolate(4,1,7) <<"\n";
    cout<<"Expect 2: " << makeChocolate(6,2,7) <<"\n";
    cout<<"Expect 0: " << makeChocolate(4,1,5) <<"\n";
    cout<<"Expect 4: " << makeChocolate(4,1,4) <<"\n";
    cout<<"Expect 3: " << makeChocolate(9,3,18) <<"\n";
    cout<<"Expect 2: " << makeChocolate(6,2,7) <<"\n";
    return 0;
}


