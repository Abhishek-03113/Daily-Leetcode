#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';

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


        if (a[0] == 1){
            cout << "YES" << nl ; 
        }
        else{
            cout << "NO" << nl ;    
        }
        // bool isSorted = is_sorted(a.begin(), a.end());

        // if (!isSorted)
        // {

        //     for (int i = 1; i < n; i++)
        //     {
        //         if ((a[i - 1] < a[i]) && (a[i] > a[i + 1]))
        //         {
        //             swap(a[i], a[i + 1]);
        //         }
        //     }
        // }

        // if (is_sorted(a.begin(), a.end()))
        // {
        //     cout << "YES" << nl;
        // }
        // else
        // {
        //     cout << "NO" << nl;
        // }
    }
}