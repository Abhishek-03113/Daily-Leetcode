#include<bits/stdc++.h> 
using namespace std ; 

int main() {
	long n,s,c=0; 
	cin >> n >> s;
	
	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; j<=n; j++)
		{
			if (s-i-j >= 0 && s-i-j <= n)
			{
				c++;
			}
			
		}
	}

	cout <<  c << endl; 
}