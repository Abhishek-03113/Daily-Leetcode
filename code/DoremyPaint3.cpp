#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';
#define yes cout << "YES" << nl ; 
#define no cout << "NO" << nl; 

signed main()
{
    int t; cin >> t;

    while (t--)
    {
        int n; cin >> n; 
        map<int, int> occ; 

        for (int i =1 ; i<=n;++i){
            int x; cin >> x;
            occ[x]++; 
        }

        if (occ.size() >= 3){
            puts("NO"); 
        }
        else{
            if (abs(occ.begin()->second - occ.rbegin()->second) <=1){
                puts("YES"); 
            }
            else{
                puts("NO");
            }
        }
    }
    
  
}