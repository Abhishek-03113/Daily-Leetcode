#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';
#define yes cout << "YES" << nl;
#define no cout << "NO" << nl;

signed main()
{

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> a(n);

        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        vector<int> b({a[n - 1]});

        for (int i = n - 2; i >= 0; i--)
        {
            if (a[i] > b.back())
            {
                b.push_back(a[i] % 10);
                b.push_back(a[i] / 10);
            }
            else
            {
                b.push_back(a[i]);
            }
        }

        if (is_sorted(b.rbegin(), b.rend()))
        {
            yes
        }
        else
        {
            no
        }
    }
}