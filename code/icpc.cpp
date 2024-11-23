#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define all(v) v.begin(), v.end()
#define mod 998244353
#define pb push_back
#define fi first
#define se second
#define sz(x) ((int)(x).size())  

void spicyy()
{
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(),a.end());

    vector<ll> pre(n, 0);
    vector<ll> ans(n + 1, 0);

    pre[0] = a[0];
    ans[0] = a[0];

    for (int i = 1; i < n; ++i)
    {
        if (i < k)
        {
            pre[i] = pre[i - 1] + a[i];
            ans[i] = pre[i];
        }
        else
        { 
            if (k == 1 && i < 2){
                pre[i] = a[i]; 
                ans[i] = pre[i];
            }
            else{
            pre[i] = a[i] + pre[i - 2];
            ans[i] = pre[i];}
        }
    }

    for (int i = 0; i < n; ++i)
    {
        cout << ans[i] << " ";
    }
    cout << "\n";
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        spicyy();
    }

    return 0;
}
