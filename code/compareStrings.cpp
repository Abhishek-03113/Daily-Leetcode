#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

signed main(){
    string a, b; 

    cin >> a; 
    cin >> b ; 

    int len = 0 ; 
    bool flag = false; 
    len = min(a.size(), b.size()); 

    for (int i = 0; i < len; i++){
        if (a[i] == b[i]){
            continue;
        }
        else{
            if (a[i]<b[i]){
                cout << a << nl ; 
            }
            else{
                cout << b << nl; 
            }
            flag = true; 
            break;
        }

    }


    if (flag==false){
        if( a.size() > b.size()){
            cout << b << nl ; 
        }
        else{
            cout << a << nl ; 
        }
    }
}