#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#define INF 1000000000
using namespace std;

#define int long long
#define nl '\n'
#define V vector<int>

#define mod 1000000007
#define inf 1e18
#define print(x) for (int i = 0; i < x.size(); i++) cout << x[i] << " "; 
#define loop(i, n) for (int i = 0; i < n; i++)


int coins(int n, int x, V a){
    V dp(x+1, -1); 
    dp[0] = 0;
    for (int i = 1; i<=x; i++){
        for (int j = 0; j < n; j++){
            if (a[j] > i){continue;}  
            dp[i] = dp[i] + dp[i-a[j]];
        }
    }

    print(dp);
    return 0; 
}

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); 


    int n,x; cin>> n >>x; 
    V a(n, 0); 

    loop(i, n){
        cin >> a[i];
    }

    int ans = coins(n,  x, a);
    cout << ans << nl;

    return 0;
    }

   