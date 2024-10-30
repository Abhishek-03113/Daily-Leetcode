#include "bits/stdc++.h"
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<int>b(n-1), a;
    for(int i = 0; i < n - 1; i++) cin >> b[i];
    a.emplace_back(b[0]);
    for(int i = 0; i < n - 2; i++){
        a.emplace_back(min(b[i], b[i + 1]));
    }
    a.emplace_back(b[n - 2]);
    for(auto &i : a) cout << i << ' ';
    cout << "\n";
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}