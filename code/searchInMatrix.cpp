#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long n, m ; cin >> n >> m; 

	long long arr[n][m];

	for (int i = 0 ; i< n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> arr[i][j];
		}
	}

	long long x; 

	cin >> x; 
	bool flag = false; 
	for (long long i = 0 ; i< n; i++)
	{
		for (long long j = 0; j < m; j++)
		{
			if (arr[i][j] == x) 
			{
				
				flag = true ; 
			}
		}
	}
	if (!flag) cout << "will take number"; 
	else cout << "will not take number"; 
}