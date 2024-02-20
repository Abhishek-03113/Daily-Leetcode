#include<bits/stdc++.h> 
// #define int long long
#define nl endl; 
using namespace std ; 


signed main() {
	int n, q ; cin >> n >> q; 
	int A[n] ;

	for (int i = 0; i < n ; i++)
	{
		cin >> A[i];
	}

	sort(A,A+n); 

	while (q--)
	{
		int x ; cin >> x; 
		int start = 0, end = n-1; 	
		bool flag = false; 

	while (start <= end)
	{
		int mid = start + (end - start) / 2 ; 

		if (A[mid] == x)
		{
			flag = true; 
			break; 
		}
		else if (A[mid] > x)
		{ 
			end = mid-1; 
		}
		else{
			start = mid + 1 ; 
		}
	}

	if (flag == true){ cout << "found" << nl ; }
	else 
	{cout << "not found" << nl; }


}
}