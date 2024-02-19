# import math 

# t = int(input()) 

# for _ in range(t): 
#     n, m = map(int, input().split()) 
#     a = list(map(int, input().split())) 
#     s = input() 
    
#     prod = 1
#     for i in range(n):
#         prod *= a[i]
#     rem = prod % m 
#     print(rem, end =" ")
    
#     for i in s: 
#         if i == 'L':
#             p = a.pop(0)
#             prod =  int(prod / p)   # o(n*n) 
#             rem = prod % m 
#             if len(a)==0:
#                 break
#             print(rem , end= " ")
#         elif i == 'R':
#             p = a.pop(-1)
#             prod = int(prod / p)  # o(n*n)
#             rem = prod % m 
            
#             if len(a)==0:
#                 break
#             print(rem, end =" ")
#     print("") 


t = int(input()) 

for _ in range(t): 
    ans = []
    n, m = map(int,input().split()) 
    a = list(map(int,input().split()))
    s = input() 
    
    
#include <algorithm>
#include <iostream>
#include <vector>
#include <bitset>
#include <string>
#include <array>
#include <queue>
 
using namespace std;
 
array<int,200001> vals,order,answers;
deque<int> ids;
string str;
 
int main(int argc,char* argv[],char* envp[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int testcnt;
    cin>>testcnt;
    while(testcnt--)
    {
        int cnt,moder;
        cin>>cnt>>moder;
        for(int i=0;i<cnt;i++)
            cin>>vals[i],ids.push_back(i);
        for(int i=0;i<cnt;i++)
        {
            char tmp;
            cin>>tmp;
            if(tmp=='L')
                order[i]=ids.front(),ids.pop_front();
            else
                order[i]=ids.back(),ids.pop_back();
        }
        answers[0]=1;
        for(int i=1;i<=cnt;i++)
            answers[i]=answers[i-1]*vals[order[cnt-i]]%moder;
        for(int i=1;i<=cnt;i++)
            cout<<answers[cnt-i+1]<<' ';
        cout<<'\n';
    }
    return 0;
}