#include<bits/stdc++.h> 
using namespace std ; 
using ll= long long int; 
#define nl '\n';

int main() {

	ll n, m, x, y; cin >> n >> m ; 
	char arr[n+1][m+1];

	for (ll i = 0; i <=n;i++)
	{
		for (ll j = 0; j <= m ; j++)
		{
			if (i == 0 || j == 0){
				arr[i][j] = 'x'; 
			}
			else cin >> arr[i][j] ; 
		}
	}

	cin >> x >> y ; 
	
	// cout << arr[x][y] << nl ; 
	bool c1,c2,c3,c4,c5,c6,c7,c8; 
	c1 = arr[x][y-1] == 'x';
	c2 = arr[x][y+1] == 'x';


	c3 = arr[x-1][y]== 'x';
	c4 = arr[x+1][y] == 'x';

	c5 = arr[x-1][y-1] == 'x';
	c6 = arr[x+1][y+1] == 'x';
	c7 = arr[x+1][y-1] == 'x';
	c8 = arr[x-1][y+1] == 'x'; 

	// cout << c1 <<  c2 <<  c3 <<  c4 <<  c4 <<  c5 << c6 << c7 << c8;

	if (c1 && c2 && c3 && c4 && c4 && c5 && c6)
	{
		cout << "YES" << nl; 
	}
	else cout << "NO" << nl ; 
	
	

}
