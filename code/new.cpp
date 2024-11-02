#include <bits/stdc++.h>
using namespace std;

#define int long long
#define nl '\n'
#define V vector<int>

#define mod 1000000007
#define inf 1e18
#define print(x) for (int i = 0; i < x.size(); i++) cout << x[i] << " "; 
#define loop(i, n) for (int i = 0; i < n; i++)

void solve(){ 
   int n; cin >> n; 
   V a(n+1, 0);

   set<int> s; 

   loop(i, n){ 
    int x; cin >> x; a[i] = x; 
   }

   int curr, ans; 
   
   curr = 0; ans = 0;

   loop(i, n){

    if (s.find(a[i]) != s.end()){
        ans = max(ans, curr); 
        curr -= 1; 
        s.erase(a[i]);
        
    }
    else{
        curr += 1; 
        s.insert(a[i]);  
    }
    ans = max(ans, curr); 
   }

   cout << ans << nl; 
   
   
}

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    solve();    
}
