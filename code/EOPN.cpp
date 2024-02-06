#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	double n;
	long positive, negative, even, odd;

	cin >> n ;
	positive = 0;
	negative = 0 ;
	even = 0 ;
	odd = 0 ;

	for (int i = 0; i < n ; i++)
	{	int x; 
		cin >> x;

		if (x >0){positive++;}
		else if (x < 0 ){negative++;}


		if (x%2==0) {even++;}
		else if (x%2 != 0){odd++;}


	}

	cout << "Even: " << even << endl;
	cout << "Odd: " << odd << endl; 
	cout << "Positve: " << positive << endl; 
	cout << "Negative: " << negative << endl; 

}