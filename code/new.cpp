#include <bits/stdc++.h>
using namespace std;
 
int computeMex(const vector<int>& a, int l, int r) {
    bool present[4] = {false, false, false, false};
    for (int i = l; i <= r; i++) {
        if (a[i] < 4)
            present[a[i]] = true;
    }
    for (int x = 0; x < 4; x++) {
        if (!present[x])
            return x;
    }
    return 4;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (auto &x : a)
            cin >> x;
 
        vector<pair<int, int>> ops;
 
        while ((int)a.size() > 3) {
            bool hasZero = false;
            for (auto x : a) {
                if (x == 0) { 
                    hasZero = true; 
                    break; 
                }
            }
            if (hasZero) {
                int pos = -1;
                for (int i = 0; i < (int)a.size(); i++) {
                    if (a[i] == 0) { 
                        pos = i; 
                        break; 
                    }
                }
                if (pos == 0) {
                    int m = computeMex(a, 0, 1);
                    ops.push_back({1, 2});
                    vector<int> newA;
                    newA.push_back(m);
                    for (int i = 2; i < (int)a.size(); i++) {
                        newA.push_back(a[i]);
                    }
                    a = newA;
                } else {
                    int m = computeMex(a, pos - 1, pos);
                    ops.push_back({pos, pos + 1});
                    vector<int> newA;
                    for (int i = 0; i < pos - 1; i++) {
                        newA.push_back(a[i]);
                    }
                    newA.push_back(m);
                    for (int i = pos + 1; i < (int)a.size(); i++) {
                        newA.push_back(a[i]);
                    }
                    a = newA;
                }
            } else {
                int m = computeMex(a, 0, a.size() - 1);
                ops.push_back({1, (int)a.size()});
                vector<int> newA;
                newA.push_back(m);
                a = newA;
                break;
            }
            if (a.size() == 3) {
                int p = computeMex(a, 0, 1);
                if (p != 0 && a[2] != 0) {
                    ops.push_back({1, 2});
                    vector<int> newA;
                    newA.push_back(p);
                    newA.push_back(a[2]);
                    a = newA;
                } else {
                    int q = computeMex(a, 1, 2);
                    if (a[0] != 0 && q != 0) {
                        ops.push_back({2, 3});
                        vector<int> newA;
                        newA.push_back(a[0]);
                        newA.push_back(q);
                        a = newA;
                    } else {
                        ops.push_back({1, 3});
                        int m = computeMex(a, 0, 2);
                        vector<int> newA;
                        newA.push_back(m);
                        a = newA;
                    }
                }
            }
 
            if (a.size() == 2) {
                int m = computeMex(a, 0, 1);
                ops.push_back({1, 2});
                vector<int> newA;
                newA.push_back(m);
                a = newA;
            }
        }
 
        cout << ops.size() << "\n";
        for (auto &op : ops) {
            cout << op.first << " " << op.second << "\n";
        }
    }
    return 0;
}