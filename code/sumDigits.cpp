#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long n, sum, dig;
	string m;  
	cin >> n;
	sum = 0;  
	cin >> m ;

	for (int i = 0; i < n; i++)
	{
		sum += ((int)(m[i])-48) % 10 ;
	}

	cout << sum; 

}