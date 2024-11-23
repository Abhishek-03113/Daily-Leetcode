#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

struct Flight {
    string from, to;
    int takeoff, landing, cost;
};

int flightOptimization(vector<Flight>& flights, string start, string end, int startTime, int endTime) {
    int n = flights.size();
    vector<vector<pair<int, int>>> dp(n + 1, vector<pair<int, int>>(1441, {INT_MAX, -1}));
    dp[0][startTime] = {0, -1};

    for (int i = 1; i <= n; i++) {
        for (int t = 0; t <= 1440; t++) {
            if (dp[i - 1][t].first != INT_MAX) {
                if (flights[i - 1].from == start && flights[i - 1].takeoff >= t && flights[i - 1].landing <= endTime) {
                    dp[i][flights[i - 1].landing] = min(dp[i][flights[i - 1].landing], {dp[i - 1][t].first + flights[i - 1].cost, i - 1});
                }
                if (flights[i - 1].to == end && flights[i - 1].landing <= endTime) {
                    dp[i][flights[i - 1].landing] = min(dp[i][flights[i - 1].landing], dp[i - 1][t]);
                }
            }
        }
    }

    int minCost = INT_MAX, lastFlight = -1;
    for (int t = 0; t <= 1440; t++) {
        if (dp[n][t].first < minCost && dp[n][t].first != INT_MAX) {
            minCost = dp[n][t].first;
            lastFlight = dp[n][t].second;
        }
    }

    if (minCost == INT_MAX) {
        return -1;
    }

    return minCost;
}

int main() {
    int n;
    cin >> n;

    vector<Flight> flights(n);
    for (int i = 0; i < n; i++) {
        cin >> flights[i].from >> flights[i].to >> flights[i].takeoff >> flights[i].landing >> flights[i].cost;
    }

    string start, end;
    int startTime, endTime;
    cin >> start >> end >> startTime >> endTime;

    int minCost = flightOptimization(flights, start, end, startTime, endTime);

    if (minCost == -1) {
        cout << "Impossible" << endl;
    } else {
        cout << minCost << endl;
    }

    return 0;
}