// Created by ThanhNam on 2/9/2021.
/*Given three ints, a b c, one of them is small, one is medium and one is large.
Return true if the three values are evenly spaced,
so the difference between small and medium is the same as the difference between medium and large.

evenlySpaced(2, 4, 6) → true
evenlySpaced(4, 6, 2) → true
evenlySpaced(4, 6, 3) → false*/

#include <iostream>
using namespace std;

bool evenlySpace(int a, int b, int c){
    //if a is largest
    if (a - b > 0 && a - c >0){
	    //if b is medium
	    if (a - b == b - c) return true;
	    //else c is medium
	    if (a - c == c - b) return true;
	    return false;
    }
    //else if b is largest
    else if (b - a > 0 && b - c > 0){
		//if a is medium
		if (b-c == c- a) return true;
		if (b-a == a-c) return true;
		return false;
		// else c is medium
    }

    //else c is largest
    else
	{
		if (c-a == a- b) return true;
		if (c-b == b-a) return true;
		return false;
		//if b is medium
		//else a is medium
	}

}

int main(){
    cout<<"Expect 1: "<<evenlySpace(2,4,6)<<"\n";
    cout<<"Expect 1: "<<evenlySpace(4,6,2)<<"\n";
    cout<<"Expect 0: "<<evenlySpace(4,6,3)<<"\n";
    return 0;
}