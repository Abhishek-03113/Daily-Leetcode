#include <iostream>
#include <deque>
#include <vector>

std::vector<int> soln(int n, std::deque<int> a) {
    std::vector<int> b;
    int time = 0;
    while (!a.empty()) {
        time += 1;
        b.push_back(a.size());
        a.pop_front();
        std::deque<int> temp;
        for (int x : a) {
            if (x > 1) {
                temp.push_back(x - 1);
            }
        }
        a = temp;
    }
    b.push_back(0);
    return b;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        std::cin >> n;
        std::deque<int> a(n);
        for (int j = 0; j < n; j++) {
            std::cin >> a[j];
        }
        std::vector<int> result = soln(n, a);
        for (int x : result) {
            std::cout << x << " ";
        }
        std::cout << "\n";
    }
    return 0;
}