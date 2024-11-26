#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define all(v) v.begin(), v.end()
#define mod 998244353
#define pb push_back
#define fi first
#define se second
#define sz(x) ((int)(x).size())

void spicyy() {
    int n, k;
    cin >> n >> k;

    vector<int> arr(n, n);  
    vector<pair<pair<int, int>, int>> constraints(k);

    
    for (int i = 0; i < k; i++) {
        int l, r, m;
        cin >> l >> r >> m;
        constraints[i] = {{l - 1, r - 1}, m};  
    }

    bool possible = true;

    
    for (const auto& constraint : constraints) {
        int l = constraint.fi.fi, r = constraint.fi.se, m = constraint.se;

        bool fixed = false;

        for (int i = l; i <= r; i++) {
            if (arr[i] <= m) {
                if (m > 1) {
                    arr[i] = m - 1;
                } else {
                    fixed = false;
                    for (int j = l; j <= r; j++) {
                        if (arr[j] == m) {
                            if (m + 1 <= n) arr[j] = m + 1;
                            fixed = true;
                            break;
                        }
                    }
                    if (!fixed) {
                        possible = false;
                        break;
                    }
                }
            }
        }
        if (!possible) break;
    }

    
    if (possible) {
        for (const auto& constraint : constraints) {
            int l = constraint.fi.fi, r = constraint.fi.se, m = constraint.se;

            bool valid = false;
            for (int i = l; i <= r; i++) {
                if (arr[i] == m) {
                    valid = true;
                    break;
                }
            }
            if (valid) {
                possible = false;
                break;
            }
        }
    }

    
    if (!possible) {
        cout << -1 << endl;
    } else {
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        spicyy();
    }

    return 0;
}
