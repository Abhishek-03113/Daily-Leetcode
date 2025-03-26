#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
#define INF 1e9
using namespace std;

#define int long long
#define nl '\n'
#define V vector<int>

#define mod 1000000007
#define inf 1e18
#define print(x) for (int i = 0; i < x.size(); i++) cout << x[i] << " "; 
#define loop(i, n) for (int i = 0; i < n; i++)

int coin(int n,int x,V& a){

    int res = 0; 
    if (x == 0) return 0; 
    if (x < 0) return -1;

    for (int i = 0; i < n; i++){
        if (a[i] > x){
            continue; 
        }
        res = res + coin(n, x-a[i], a) + 1; 
    }
    return res;
}


signed main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); 


    int n,x; cin>> n >>x; 
    V a(n, 0); 

    loop(i, n){
        cin >> a[i];
    }

    int ans = coin(n,  x, a);
    cout << ans << nl;

    return 0;
    }

   