#include<bits/stdc++.h> 
using namespace std ; 

int gcd(int a, int b)
{
	if (a == 0)
	{
		return b ;
	}

	return  gcd((b%a), a);
}

int main() { 

	int a, b, ans ;

	cin >> a >>  b; 

	if (a>b)
	{
		swap(a, b); 
	}

	ans = gcd(a, b); 
	cout << ans << endl;

}