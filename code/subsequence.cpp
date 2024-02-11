#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long n, m; cin >> n >> m; 
	long long a[n],b[m]; 


	for (long long i = 0 ; i < n; i++)
	{
		cin >> a[i];
	}

	for (long long j = 0 ; j < m; j++)
	{
		cin >> b[j];
	}

	long long j = 0; 

	for (int i = 0; i < n ; i++)
	{
		// cout << i << endl; 
		if (a[i] != b[j])
		{
			continue ;
		}

		else {
			j++; 
		}
	} 

	if (j == m) cout << "YES" << endl; 
	else cout << "NO" << endl; 
}