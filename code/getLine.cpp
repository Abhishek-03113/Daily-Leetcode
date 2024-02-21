#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

signed main(){
    string s; 
    
    getline(cin, s); 

    int pos = s.find("\\");

    cout << s.substr(0, pos) << nl ; 


}