#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    
    vector<long long> batteries(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> batteries[i];
    }
    
    vector<vector<pair<int, long long>>> graph(n + 1);
    
    // Track only minimum required battery levels
    vector<long long> reqs;
    reqs.push_back(0);
    
    for (int i = 0; i < m; i++) {
        int s, t;
        long long w;
        cin >> s >> t >> w;
        graph[s].push_back({t, w});
        reqs.push_back(w);
    }
    
    // Sort and deduplicate battery requirements
    sort(reqs.begin(), reqs.end());
    reqs.erase(unique(reqs.begin(), reqs.end()), reqs.end());
    
    // Use vector-based dist map for better memory efficiency
    vector<vector<long long>> dist(n + 1, vector<long long>(reqs.size(), LLONG_MAX));
    
    // Mapping from actual battery value to compressed index
    map<long long, int> compress;
    for (int i = 0; i < reqs.size(); i++) {
        compress[reqs[i]] = i;
    }
    
    // Dijkstra: {cost, checkpoint, battery_index}
    priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<>> pq;
    
    // Start with node 1, battery level 0
    pq.push({0, 1, 0}); // 0 is the index for battery level 0
    dist[1][0] = 0;
    
    while (!pq.empty()) {
        auto [cost, cp, batt_idx] = pq.top();
        pq.pop();
        
        long long current_batt = reqs[batt_idx];
        
        // Reached destination
        if (cp == n) {
            cout << cost << "\n";
            return;
        }
        
        // Skip outdated states
        if (dist[cp][batt_idx] < cost) continue;
        
        // For each transition from current checkpoint
        for (auto [next, req] : graph[cp]) {
            // If we have enough batteries already
            if (current_batt >= req) {
                int next_batt_idx = batt_idx; // Keep same battery level
                
                if (dist[next][next_batt_idx] > cost) {
                    dist[next][next_batt_idx] = cost;
                    pq.push({cost, next, next_batt_idx});
                }
            }
        }
        
        // Try adding batteries to reach required levels or max level
        for (int i = 0; i < reqs.size(); i++) {
            long long target_batt = reqs[i];
            
            // Only consider valid battery increases
            if (target_batt > current_batt && target_batt <= current_batt + batteries[cp]) {
                long long add_cost = target_batt - current_batt;
                long long new_cost = cost + add_cost;
                
                // Check if this new battery level allows us to go somewhere
                bool useful = false;
                for (auto [next, req] : graph[cp]) {
                    if (target_batt >= req) {
                        useful = true;
                        break;
                    }
                }
                
                if (useful && dist[cp][i] > new_cost) {
                    dist[cp][i] = new_cost;
                    
                    for (auto [next, req] : graph[cp]) {
                        if (target_batt >= req && dist[next][i] > new_cost) {
                            dist[next][i] = new_cost;
                            pq.push({new_cost, next, i});
                        }
                    }
                }
            }
        }
        
        // Also try to reach max battery level if it's useful
        long long max_batt = current_batt + batteries[cp];
        
        // Skip if no additional batteries available
        if (batteries[cp] <= 0) continue;
        
        // Check if this max level could help us go somewhere
        bool useful = false;
        int max_batt_idx = -1;
        
        // Find the right index for the max battery or the closest smaller value
        for (int i = reqs.size() - 1; i >= 0; i--) {
            if (reqs[i] <= max_batt) {
                max_batt_idx = i;
                break;
            }
        }
        
        if (max_batt_idx == -1 || max_batt_idx == batt_idx) continue;
        
        for (auto [next, req] : graph[cp]) {
            if (reqs[max_batt_idx] >= req && current_batt < req) {
                useful = true;
                break;
            }
        }
        
        if (useful) {
            long long new_cost = cost + (max_batt - current_batt);
            
            if (dist[cp][max_batt_idx] > new_cost) {
                dist[cp][max_batt_idx] = new_cost;
                
                for (auto [next, req] : graph[cp]) {
                    if (reqs[max_batt_idx] >= req && dist[next][max_batt_idx] > new_cost) {
                        dist[next][max_batt_idx] = new_cost;
                        pq.push({new_cost, next, max_batt_idx});
                    }
                }
            }
        }
    }
    
    cout << -1 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}
