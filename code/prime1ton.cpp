#include<bits/stdc++.h> 
using namespace std ; 

bool isPrime(int n)
{
	int cnt = 0; 
	for (int i = 1; i <= n; i++ )
	{
		if (n % i == 0){cnt++;}
	}
	
	if (cnt == 2){
		return true;
	}
	else return false; 
}


int main() {
	int x; cin >> x; 

	for (int i = 1; i <= x; i++)
	{
		if (isPrime(i))
		{
	
			cout << i << " "; 
		}
	}
}