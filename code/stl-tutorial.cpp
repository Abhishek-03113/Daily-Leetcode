#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nl '\n';

void printVect(vector<int> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << nl;
}

signed main()
{
    pair<int, string> p;

    // cin >> p.first >> p.second ;

    // cout << p.first << " " << p.second ;

    int a[10];
    vector<int> v;

    int n = 5;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }

    printVect(v);
}