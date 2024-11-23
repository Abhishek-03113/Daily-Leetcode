// #include <bits/stdc++.h>
// using namespace std;

// #define int long long
// #define nl '\n'
// #define V vector<int>

// #define mod 1000000007
// #define inf 1e18
// #define print(x) for (int i = 0; i < x.size(); i++) cout << x[i] << " "; 
// #define loop(i, n) for (int i = 0; i < n; i++)

// void solve(){

//     int n; cin >> n; 

//     V a; 
//     loop(i, n){
//         int temp; cin >> temp; 
//         a.push_back(temp); 
//     }

//     a.sort(); 

//     int left = 0, right = n-1; 

//     while

// }

// signed main(){
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     int t; cin >> t; 
//     while(t--){
//     solve(); 
// }
// }

#include <bits/stdc++.h>
using namespace std;

const int LIMIT = 1e9;

vector<long long> generate_periodic_numbers(int limit)
{
    set<long long> periodic_numbers;
    for (int l = 1; l <= 30; ++l)
    {
        int max_runs = 30 / l;
        for (int s = 0; s <= 1; ++s)
        {
            long long A = s == 1 ? ((1LL << l) - 1) : 0;
            long long B = s == 1 ? 0 : ((1LL << l) - 1);
            for (int k = 1; k <= max_runs; ++k)
            {
                long long n = 0;
                for (int i = 0; i < k; ++i)
                {
                    n <<= l;
                    if (i % 2 == 0)
                        n |= A;
                    else
                        n |= B;
                }
                if (n > limit || n == 0)
                    break;
                periodic_numbers.insert(n);
            }
        }
    }
    vector<long long> result(periodic_numbers.begin(), periodic_numbers.end());
    sort(result.begin(), result.end());
    return result;
}

void solve(const vector<long long> &periodic_numbers)
{
    long long L, R;
    cin >> L >> R;
    auto left = lower_bound(periodic_numbers.begin(), periodic_numbers.end(), L);
    auto right = upper_bound(periodic_numbers.begin(), periodic_numbers.end(), R);
    cout << distance(left, right) << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<long long> periodic_numbers = generate_periodic_numbers(LIMIT);
    int t;
    cin >> t;
    while (t--)
    {
        solve(periodic_numbers);
    }
    return 0;
}