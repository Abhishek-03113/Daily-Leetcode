#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	int t ; cin >> t; 
	char arr[3][3];

	while (t--)
	{
		vector<string> s(3);
		for (int i = 0 ; i <3 ; i++){
			cin >> s[i]; 
		}
		int a = 0,b = 0,c =0 ; 
		for (int i = 0 ; i <3 ; i++){
			for (int j =0 ; j < 3 ; j++){
				if (s[i][j] == 'A') a++;
				else if (s[i][j] == 'B') b++; 
				else if (s[i][j] == 'C') c++; 
			}
			
		}

		if (a !=3) cout << "A" << endl; 
		else if (b != 3) cout << 'B' << endl; 
		else if (c != 3) cout << "C" << endl; 
	}

	

} 