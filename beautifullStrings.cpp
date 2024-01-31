// #include <bits/stdc++.h>
// using namespace std;

// int Substring(string s)
// {
 
//     int ans = 1, temp = 1;
//     for (int i = 1; i < s.size(); i++) {
//         // If character is same as
//         // previous increment temp value
//         if (s[i] == s[i - 1]) {
//             ++temp;
//         }
//         else {
//             ans = max(ans, temp);
//             temp = 1;
//         }
//     }
//     ans = max(ans, temp);
//     return ans;
// }
// int main() {
    
//     int t; 
//     cin >> t; 
    
//     for(int i =0;i < t; i++)
//     {
//         int N, Q; 
//         string S;
        
//         cin >> N >> Q ; 
        
//         cin >> S; 
//         cout << Substring(S) << " "; 
        
//         for (int j = 0; j < Q; j ++){
            
//             char c ; 
//             cin >> c; 
            
//             S += c ;
            
//             cout << Substring(S) << ' '; 
//         }
        
//         cout << "\n" ;
//     }
// 	// your code goes here

// }


