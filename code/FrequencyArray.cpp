#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

signed main(){
    int n, m; cin >> n >> m ; 
    int arr[n];
    vector<int> freq (m+1, 0); 
    for (int i = 0; i<n; i++)
    {
        int x = 0; cin >> x;

        if (x<=m)
        {
            freq[x]++;
        }
    }
    for(int i= 1; i<=m;i++)
    {
        cout << freq[i] << nl ; 
    }

}