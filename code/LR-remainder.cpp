#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int t ; cin >> t; 

	while (t--)
	{
		int n, m,prod,rem= 1 ; cin >> n >> m; 
		vector <int> arr(n); 
		string s; 
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
			prod = prod * arr[i]; 
		}

		rem = prod % m ;

		cout << rem << " "; 

		for (int i = 0; i < n; i++)
		{
			if (s[i] == 'L')
			{
				int temp = arr[0]; 
				prod = prod / temp; 
				rem = prod % m ; 

				cout << rem << " ";
				arr.erase(arr.begin()+0); 
			}
			else{
				int temp = arr[-1]; 
				prod = prod / temp; 
				rem = prod % m ; 
				cout << rem << " ";
			}
		}


	}
	

}
