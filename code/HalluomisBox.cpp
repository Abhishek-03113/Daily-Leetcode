#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';

signed main()
{

    int t ; cin >> t; 

    while (t--)
    {
        int n,k; 
        cin >> n >> k ; 
        vector<int> a(n); 
        for (int i = 0; i < n ; i++){
            cin >> a[i];
        }
        
        if ((k > 1) || (is_sorted(a.begin(), a.end()))){
            cout << "YES" << nl; 
        }
        else cout << "NO" << nl ; 
        
    }
    
   
}

