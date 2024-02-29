#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';


signed main()
{
    int t; cin >> t; 

    while (t--)
    {
        int n, x; cin >> n >> x ; 
        int ans = 0, prev = 0; 

        for (int i = 0; i < n; i++){
            int f; 
            cin >> f; 
            ans = max(ans, f-prev); 
            prev = f; 
        }
        ans = max(ans, 2*(x-prev)) ; 
        cout << ans << nl ; 
    }
  
}