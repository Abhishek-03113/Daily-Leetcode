#include<bits/stdc++.h> 
using namespace std ; 

int main() {
	long l1, r1, l2, r2; cin >> l1 >> r1 >> l2 >> r2 ; 

	if (l2 >= l1){
		if (l2 <= r1)
		{
			if (r2 < r1) 
			{
				cout << l2 << " " << r2 << endl; 
			}
			else
			{
				cout << l2 << " " << r1 << endl ; 
			}
		}
		else
		{
			cout << -1 << endl;
		}
	}
	else
	{
		if (r2 >=r1)
		{
			cout << l1 << " " << r1 <<endl;  
		}
		else if (r2 < l1)
		{
			cout << -1 << endl;
		}

		else{
			cout << l1 <<" " << r2 << endl;
		}
	
	}



}

	

