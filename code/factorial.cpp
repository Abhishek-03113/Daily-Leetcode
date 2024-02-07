#include<bits/stdc++.h> 
using namespace std ; 

int main() {
	int t; 
	cin >> t; 

	while (t)
	{ 

	int n; cin >> n ; 
	long long int ans; 
	ans = 1; 
	while (n)
	{
		ans = n * ans; 

		n--; 

	}

	cout << ans << endl ; 	

	t--;
}
}