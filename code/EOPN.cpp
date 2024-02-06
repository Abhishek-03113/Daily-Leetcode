#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int n;cin >> n ;
	int positive, negative, even, odd;
	
	positive = 0;
	negative = 0 ;
	even = 0 ;
	odd = 0 ;

	for (int i = 0; i < n ; i++)
	{
		int x; 
		cin >> x;


		if (x < 0){negative++;}
		else if (x>0) {positive++;}

		if (x % 2 == 0) {even++;}
		else {odd++;}
	}

	cout << "Even: " << even << endl; 
	cout << "Odd: " << odd << endl; 
	cout << "Positive: " << positive << endl; 
	cout << "Negative: " << negative << endl; 

}