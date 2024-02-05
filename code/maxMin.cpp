#include<bits/stdc++.h> 
using namespace std ; 

int main() {
	long long a, b, c, min, max; 
	cin >> a >> b >> c ;


	if (a >= b && a >= c){
		max = a ;
	}

	if (a <= b && a <= c)
		{min = a; }

	if (b >= a && b >= c){
		max = b ;
	}

	if (b <= a && b <= c)
		{min = b; }

	if (c >= a && c >= b){
		max = c ;
	}

	if (c <= b &&c <= a)
		{min = c; }

	cout << min << " " << max ; 

}