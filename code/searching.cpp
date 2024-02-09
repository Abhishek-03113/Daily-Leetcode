#include<bits/stdc++.h> 
using namespace std ; 


int main() {

	long long n,x, ind = -1; cin >> n; 
	long long arr[n]; 


	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}
	cin >> x ;

	for (int i = 0; i < n; i++ )
	{
		if (arr[i] == x)
		{
			ind = i; 
			break ; 
		}
	}
	cout << ind << endl; 
}