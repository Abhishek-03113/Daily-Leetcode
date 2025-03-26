#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, x;
    cin >> n >> x;

    vector<int> a(n);

    // Case when x = 0
    if (x == 0) {
        for (int i = 0; i < n; i++) {
            cout << i << " ";
        }
        cout << "\n";
        return;
    }

    int current_or = 0;
    for (int i = 0; i < n - 1; i++) {
        a[i] = i;
        current_or |= i;
    }

    // The last element should adjust the OR to exactly x
    a[n - 1] = x ^ current_or;

    // If the last element is already present in the array, we need a workaround
    if (a[n - 1] < n - 1) {
        // Swap with some existing number
        a[n - 2] |= a[n - 1];
        a[n - 1] = n - 1;
    }

    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
