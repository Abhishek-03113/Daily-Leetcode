#include<bits/stdc++.h> 
using namespace std ; 

#define int long long 
signed main() {

    int ans = 0 ;
    vector<int>store (2*1e5+10,0); 
    vector<int>p = {1, 10, 100, 1000, 10000, 100000, 100000, 1000000}; 

    for (int i = 1; i < 2*1e5 + 10; ++i)
    {
        if (i > 9)
        {
            int ct = 0; 
            int temp = i; 

            for (int j = 1; j < 8; ++j)
            {
                int l = temp % p[j]; 
                temp -= l; 
                l /= p[j-1]; 
                ct += l ; 
            }
            ans += ct; 
        }
        else{
            ans += i; 
        }
        store[i] = ans; 
    }

	int t ; cin >> t; 
    while (t--)
    {
        int n ; cin >> n; 
        cout << store[n] << endl ; 
    }
    
    return 0; 

}