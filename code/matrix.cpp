#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

signed main(){
    int n; cin >> n;
    int mat[n][n]; 

    for(int i=0; i <n;i++)
    {
        for (int j=0; j < n; j++)
        {
            cin >> mat[i][j]; 
        }
    }

    int dig1 = 0,dig2 = 0, diff = 0, c1=0,c2=n-1; 

    for (int i=0; i<n; i++)
    {
        for (int j=0;j<n;j++)
        {
            if (i == j) {

                dig1 += mat[i][j]; 
            }

            if (i==c1 && j == c2){
                dig2 += mat[i][j]; 

                c1++; 
                c2--; 
            }
            
        }
    }

    diff = dig1-dig2; 

    // cout << dig1 << " " << dig2 << nl; 
    cout << abs(diff) << nl ;

}