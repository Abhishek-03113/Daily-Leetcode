#include <bits/stdc++.h>
using namespace std;

#define int long long
#define nl '\n'
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define for(i, n) for (int i = 0; i < n; i++)
#define forr(i, n) for (int i = n - 1; i >= 0; i--)
#define for(i, n, step) for (int i = 0; i < n; i += step)
#define V vector<int>
#define P pair<int, int>
#define all(x) x.begin(), x.end()
#define mod 1000000007
#define inf 1e18

void solve()
{
    int n;
    cin >> n;

    V a(n); 
    for(i, n,1) cin >> a[i]; 

    int ans = 0; 

    for(i, n-1, 1) ans += abs(a[i] - a[i+1]);

    cout << ans << nl;
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}