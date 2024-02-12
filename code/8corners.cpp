#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long n,m; 

	cin >> n >> m ; 

	char ar[n][m];

	for (int i = 0; i <= n; i++)
	{
		for (int j = 0; i <= m ; j++)
		{
			if (i==0 || j == 0)
			{
				ar[i][j] = '.'; 
			}
			cin >> ar[i][j]; 
		}
	}

	long long x, y; cin >> x >> y ; 


	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; i <= m ; j++)
		{
			
			cout << ar[i][j] << endl ; 
		}
	}


}
