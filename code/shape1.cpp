#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int n ; cin >> n; 

	for (int i = n; i > 0; i--)
	{
		int temp = i; 

		while (temp)
		{
			cout << "*" << ""; 
			temp--;
		}

		cout << endl; 

	}
	

}