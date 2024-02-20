#include<bits/stdc++.h> 
using namespace std ; 
#define int long long
#define nl '\n';

signed main(){
    int n, m; cin >> n >> m ; 

    int arr[n];

    for (int i =0; i < n ; i++){
        cin >> arr[i] ; 
    }

    for (int j = 1; j <= m; j++){    
        int freq =  0; 

        for (int i = 0; i<n; i++)
        {
            if (arr[i] == j){
                freq++; 
            }
        }
        cout << freq << nl; 
    }

}