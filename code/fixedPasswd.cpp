#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long passwd;
	bool check=true;
	while (check)
	{
		cin >> passwd; 
		if (passwd == 1999)
		{
			cout << "Correct" << endl ;
			check = false; 
		}
		else cout << "Wrong" << endl ; 
	}

	

}