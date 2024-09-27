#include <bits/stdc++.h>
#include <cstring>
#include <iostream>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
using namespace std;


#define int long long
#define nl '\n'
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define V vector<int>
#define P pair<int, int>
#define all(x) x.begin(), x.end()
#define mod 1000000007
#define inf 1e18


signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int a = 1000; 

    int b = htons(a); 

    cout << b << " " << a << endl; 
     
}