#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int n; cin >> n; 
	int spaces = n-1; 

	for (int row=1; row<= n ; row++)
	{
		for (int j = 1; j<= spaces; j++)
		{
			cout << " " ;
		}
		spaces--;

		for (int star = 1; star <=2*row-1; star++)
		{
			cout << "*";
		}
		cout << endl; 
	}

	

}