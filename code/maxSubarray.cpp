#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long t ; cin >> t; 

	while (t--){

		long long n; 
		cin >> n;
		long long arr[n];

		for (long long i = 0; i < n; i++)
		{
			cin >> arr[i];
		}

		for (long long i = 0; i < n; i++)
		{
			for (long long j = i ; j <n ; j++)
			{
				long long maxi = INT_MIN;  
				for (long long k = i ; k <=j; k++)
				{
					maxi = max(maxi, arr[k]); 
				}
				cout << maxi << " ";
			}
		}
		cout << endl; 
		
	}



	

}	