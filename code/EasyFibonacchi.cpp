#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	long n ; cin >> n;

	long long a = 0, b = 1, c = 0; 

	if( n == 0)
		{cout << 0 << " ";
				return 0;
			}
		
	cout << a << " " << b << " " ; 

	for (int i = 2; i < n; i++)
	{
		c = a + b ;
		a = b;
		b = c;

		cout << c << " " ;
	}
}

// #include <bits/stdc++.h>
// using namespace std;

// int fib(int n)
// {
// 	int a = 0, b = 1, c, i;
// 	if (n == 0)
// 		return a;
// 	for (i = 2; i <= n; i++) {
// 		c = a + b;
// 		a = b;
// 		b = c;
// 	}
// 	return b;
// }

// int main()
// {
// 	int n ; cin >> n; 
//     for (int i = 0; i < n; i++)
// 	{
// 	cout << fib(i) << " ";}
// 	return 0;
// }
