#include <bits/stdc++.h>
using namespace std;

#define int long long
#define nl '\n'
#define V vector<int>

#define mod 1000000007
#define inf 1e18
#define print(x) for (int i = 0; i < x.size(); i++) cout << x[i] << " "; 
#define loop(i, n) for (int i = 0; i < n; i++)

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n,k; cin >> n >> k;
    
    if (n == 1){
        cout << 1 << nl;
    }
    
    else{
    vector<int> ans; 

    queue<int> queue;

    for (int i = 1; i <=n; i++){
        queue.push(i);
    }

    while (!queue.empty()){

        for (int i = 0; i < k; i++){
                queue.push(queue.front()); 
                queue.pop();}
        ans.push_back(queue.front());
        queue.pop();
    }

    print(ans);
   }

}
