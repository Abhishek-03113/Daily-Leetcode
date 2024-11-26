#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define all(v) v.begin(), v.end()
#define mod 998244353
#define pb push_back
#define fi first
#define se second
#define sz(x) ((int)(x).size())  
/*
void spicyy()
{
    
}

int main()
{
    
}
*/
#include <bits/stdc++.h>
using namespace std;

// Function to solve each test case
void solveTestCase() {
    int N, K;
    cin >> N >> K;  // Input size of the array and the target AND value
    vector<int> arr(N);

    // Input the array
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    // Filter elements satisfying A[i] & K == K
    vector<pair<int, int>> validElements; // {value, 1-based index}
    for (int i = 0; i < N; ++i) {
        if ((arr[i] & K) == K) {
            validElements.push_back({arr[i], i + 1});
        }
    }

    if (validElements.empty()) {
        // If no valid elements, print NO
        cout << "NO\n";
        return;
    }

    // Generate all subsets of valid elements
    int size = validElements.size();
    for (int mask = 1; mask < (1 << size); ++mask) { // Avoid empty subset
        int currentAND = ~0; // Start with all bits set
        vector<int> subsetIndices;

        for (int i = 0; i < size; ++i) {
            if (mask & (1 << i)) {
                currentAND &= validElements[i].first; // Update the AND
                subsetIndices.push_back(validElements[i].second); // Save index
            }
        }

        if (currentAND == K) {
            // Found a valid subset
            cout << "YES\n";
            cout << subsetIndices.size() << "\n";
            for (int idx : subsetIndices) {
                cout << idx << " ";
            }
            cout << "\n";
            return;
        }
    }

    // If no valid subset found
    cout << "NO\n";
}

// Main function
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T; // Number of test cases
    while (T--) {
        solveTestCase();
    }

    return 0;
}