#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';

signed main()
{
    int t; cin >> t; 

    while (t--)
    {
        int n; cin >> n; 
        vector<char> s(n); 

        for (auto &x:s) cin >> x;

        int empty = 0 ;
        bool flag = true ;
        for (int i = 0; i < n-2; i++){

            if (s[i] == '.' && s[i+1] == '.' && s[i+2]=='.')
            {
                cout << 2 << nl ;
                flag = false; 
                break; 
            }
        }
        if (flag){
        for (int i = 0 ; i < n; i++){
            if (s[i] == '.'){
                empty++; 
            }
        }

        cout << empty << nl ; }

    }
    
  
}