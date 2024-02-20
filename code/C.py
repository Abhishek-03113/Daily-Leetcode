x = int(2*1e5) + 10 
ans = 0
store = [0] * x
p = [1, 10, 100, 1000, 10000, 100000, 100000, 1000000]
for i in range(1,x):
    if i > 9:
        ct = 0 
        temp = i 
        
        for j in range(1,8):
            l = temp % p[j]
            temp -= l 
            l //= p[j-1]
            ct += l 
        ans += ct 
    else:
        ans += i 
    
    store[i] = ans

for _ in range(int(input())):
    
    n = int(input()) 
    print(store[n])

# #include<bits/stdc++.h>
# using namespace std;
# #define int long long
# signed main(){
    

#     int ans = 0;
#     vector<int> store(2 * 1e5 + 10, 0);
#     vector<int> p = {1, 10, 100, 1000, 10000, 100000, 100000, 1000000};
#     for (int i = 1; i < (2 * 1e5) + 10; ++i) {
#         if (i > 9) {
#             int ct = 0;
#             int temp = i;
#             for (int j = 1; j < 8; ++j) {
#                 int l = temp % p[j];
#                 temp -= l;
#                 l /= p[j - 1];
#                 ct += l;
#             }
#             ans += ct;
#         } else {
#             ans += i;
#         }
#         store[i] = ans;
#     }

#     int test_cases;
#     cin >> test_cases;

#     for (int t = 0; t < test_cases; ++t) {
#         int n;
#         cin >> n;
#         cout << store[n] << endl;
#     }
# }
    
