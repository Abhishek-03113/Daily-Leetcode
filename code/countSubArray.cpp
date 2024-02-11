#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long t; cin >> t; 

	while (t--)
	{
		long long n, cnt = 1, ans = 0 , valid = 0;cin >> n ;
		long long a[n]; 

		for (long long i=0; i<n; i++)
		{
			cin >> a[i];
		}

		for (long long j = 1; j < n; j++){
			if (a[j] >= a[j-1]) cnt++; 
			else {
				valid += (cnt*(cnt+1)/2); 
				cnt=1; 
			}
		}
		valid += (cnt*(cnt+1)/2); 
		cout << valid << endl;	
	}
}