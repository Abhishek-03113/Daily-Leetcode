#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int t ; cin >> t; 

	while (t--)
	{
		long long  n, m,prod = 1 ,rem=1 ; cin >> n >> m; 
		vector <long long> arr(n); 
		string s; 

		for (long long i = 0; i < n; i++)
		{
			cin >> arr[i];
			prod = prod * arr[i]; 
		}
		cin >> s; 
		rem = prod % m ;
		cout << rem << " "; 

		long long l = 0, r = n-1 ;

		while (l < r)
		{
			
		}

		

	}
	

}
