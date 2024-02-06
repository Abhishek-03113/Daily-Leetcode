#include<bits/stdc++.h> 
using namespace std ; 

int main() {
	long n, rev, temp; 
	cin >> n ; 
	rev =  0 ;
	temp = n; 
	while (temp != 0)
	{
		rev = (rev*10)+(temp%10);
		temp = floor(temp/10);
	}

	if (rev == n)
	{
		cout << rev << endl; 
		cout << "YES" << endl; 
	}
	else
	{
		cout << rev << endl; 
		cout << "NO";
	}

	// cout << rev; 

}