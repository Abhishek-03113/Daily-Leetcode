#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';
#define yes cout << "YES" << nl ; 
#define no cout << "NO" << nl; 


signed main(){

	int tc; cin >> tc; 
	int cnt = 0; 
	while (tc--){
		cnt = 0;
		cnt = 0;
		string s; 
		cin >> s; 

		char l1, l2;

		l1 = s[0];

		l2 = s[s.size()-1]; 

		for (int i = 1; i <s.size()-1;++i){

			cnt++; 
		}

		if (s.size() > 10){
		cout <<l1 << cnt <<l2<< nl; 
	}
	else{
		cout << s << nl ; 
	}
	}
    


}