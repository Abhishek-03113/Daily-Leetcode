#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';

signed main()
{
    int t; cin >> t; 

    while (t--)
    {
        int n ; cin >> n; 

        if (n % 3 == 0){
            cout << "Second" << nl; 
        }
        else{
            cout << "First" << nl ; 
        }
    } 
}