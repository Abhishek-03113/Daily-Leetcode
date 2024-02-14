#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

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