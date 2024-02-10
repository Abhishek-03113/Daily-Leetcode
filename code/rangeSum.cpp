#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long long n, q, l , r; cin >> n >> q ; 
	long long A[n+1]={0};
	long long Pref[n+1] = {0}; 

	for (long long i = 1; i <= n; i++)
	{
		cin >> A[i];
	}

	for (long long i = 1; i<=n; i++)
	{
		Pref[i] = Pref[i-1] + A[i];
	}
	for (long long j = 0 ; j < q; j++ )
	{
		long long ans = 0; 
		cin >> l >> r; 
		
		ans = Pref[r]-Pref[l-1];
		cout << ans << endl; 
		
	}

	
}