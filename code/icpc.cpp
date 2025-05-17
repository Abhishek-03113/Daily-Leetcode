#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 998244353;

// Function to compute the count of valid queue arrangements
int count_arrangements(int n, vector<int>& reports) {
    // For each person, compute possible positions (front-facing or back-facing)
    vector<vector<int>> possible_positions(n);
    vector<vector<int>> position_to_person(n); // Reverse mapping
    
    for (int i = 0; i < n; i++) {
        int front_pos = reports[i];                // If looking toward front
        int back_pos = n - 1 - reports[i];         // If looking toward back
        
        if (0 <= front_pos && front_pos < n) {
            possible_positions[i].push_back(front_pos);
            position_to_person[front_pos].push_back(i);
        }
        
        if (0 <= back_pos && back_pos < n && front_pos != back_pos) {
            possible_positions[i].push_back(back_pos);
            position_to_person[back_pos].push_back(i);
        }
    }
    
    // Check for impossible cases early
    for (int i = 0; i < n; i++) {
        if (possible_positions[i].empty()) {
            return 0; // This person can't be placed anywhere
        }
    }
    
    // Use Hopcroft-Karp algorithm for maximum bipartite matching
    vector<int> match(n, -1);    // match[position] = person
    vector<bool> visited(n);
    
    // DFS to find augmenting paths
    function<bool(int)> dfs = [&](int person) {
        for (int pos : possible_positions[person]) {
            if (visited[pos]) continue;
            visited[pos] = true;
            
            if (match[pos] == -1 || dfs(match[pos])) {
                match[pos] = person;
                return true;
            }
        }
        return false;
    };
    
    // Find maximum matching
    int max_matching = 0;
    for (int i = 0; i < n; i++) {
        fill(visited.begin(), visited.end(), false);
        if (dfs(i)) {
            max_matching++;
        }
    }
    
    if (max_matching < n) {
        return 0; // Not all people can be placed
    }
    
    // Count perfect matchings using inclusion-exclusion and determinants
    // For bipartite graphs with specific structure, we can use a simpler approach
    
    // Analyze the structure further to determine if there's a unique solution or multiple
    vector<bool> unique_position(n, true);
    vector<bool> unique_person(n, true);
    
    for (int pos = 0; pos < n; pos++) {
        if (position_to_person[pos].size() > 1) {
            unique_position[pos] = false;
            for (int person : position_to_person[pos]) {
                unique_person[person] = false;
            }
        }
    }
    
    // Count connected components in the bipartite graph
    vector<bool> visited_pos(n, false);
    vector<bool> visited_per(n, false);
    
    function<void(int, bool)> bfs = [&](int node, bool is_position) {
        if (is_position) {
            visited_pos[node] = true;
            for (int person : position_to_person[node]) {
                if (!visited_per[person]) {
                    visited_per[person] = true;
                    for (int pos : possible_positions[person]) {
                        if (!visited_pos[pos]) {
                            bfs(pos, true);
                        }
                    }
                }
            }
        } else {
            visited_per[node] = true;
            for (int pos : possible_positions[node]) {
                if (!visited_pos[pos]) {
                    visited_pos[pos] = true;
                    bfs(pos, true);
                }
            }
        }
    };
    
    int components = 0;
    vector<int> component_size;
    
    for (int i = 0; i < n; i++) {
        if (!visited_per[i]) {
            components++;
            int before_size = count(visited_per.begin(), visited_per.end(), true) + 
                             count(visited_pos.begin(), visited_pos.end(), true);
            
            bfs(i, false);
            
            int after_size = count(visited_per.begin(), visited_per.end(), true) + 
                            count(visited_pos.begin(), visited_pos.end(), true);
            
            component_size.push_back((after_size - before_size) / 2);
        }
    }
    
    // For each independent component, we have 2 arrangements
    long long result = 1;
    for (int i = 0; i < components; i++) {
        // Each connected component contributes 2 possible arrangements
        result = (result * 2) % MOD;
    }
    
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> reports(n);
        for (int i = 0; i < n; i++) {
            cin >> reports[i];
        }
        
        cout << count_arrangements(n, reports) << endl;
    }
    
    return 0;
}