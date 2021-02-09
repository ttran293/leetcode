//
// Created by ThanhNam on 2/9/2021.
//Given 2 int values greater than 0, return whichever value is nearest to 21 without going over.
//Return 0 if they both go over.
//

#include <iostream>
using namespace std;

int blackjack(int a, int b)
{
	if (a > 21 && b > 21)
		return 0;
	else{// a<= 21 or b <= 21
		if(a<=21 and b <= 21)
			if(21-a >= 21-b) return b;
			else return a;
		else{
		if (a>21) return b;
		if (b>21) return a;
		}
	}
}
int main(){

	cout<<"Expect 21: "<<blackjack(19,21)<<"\n";
	cout<<"Expect 21: "<<blackjack(21,19)<<"\n";
	cout<<"Expect 19: "<<blackjack(19,22)<<"\n";


}
