#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

// signed main() {

	
// 	int n, m;
// 	cin >> n >> m;

// 	char arr[n+1][m+1]; 

// 	for (int i=0; i<=n;i++)
// 	{
// 		for (int j=0; j<=m;j++)
// 		{
// 			if (i==0 || j ==0 ){arr[i][j] = 'x' ;}
// 			else{
// 				cin >> arr[i][j]; 
// 			}
// 		}
// 	}

// 	int x,y; 
// 	cin >> x >> y; 

// 	if (arr[x-1][y-1]=='x' && arr[x-1][y]=='x' && arr[x-1][y+1]=='x' && arr[x][y-1]=='x' && arr[x][y+1] == 'x' && arr[x+1][y-1] == 'x' && arr[x+1][y]=='x' && arr[x+1][y+1] == 'x')
// 	{
// 		cout << "yes" << nl ; 
// 	}
// 	else cout << "no" << nl ; 
// }
signed main() {

	
	int n, m;
	cin >> n >> m;


	vector<string> v(n);


	for(auto &i : v){
		cin >> i;
	}


	int x, y;

	cin >> x >> y;


	x--;
	y--;
	int ct = 0;
	if(true){
		if(v[x + 1][y + 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(true){
		if(v[x + 1][y] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(true){
		if(v[x][y + 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(x - 1 >= 0 && y - 1 >= 0){
		if(v[x - 1][y - 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(x - 1 >= 0){
		if(v[x - 1][y] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(y - 1 >= 0){
		if(v[x][y - 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(y - 1 >= 0){
		if(v[x + 1][y - 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}
	if(x - 1 >= 0){
		if(v[x - 1][y + 1] == 'x'){
			ct++;
		}
	}
	else{
		ct++;
	}


	if(ct == 8){
		cout << "yes" << endl;
	}
	else{
		cout << "no" << endl;
	}
}