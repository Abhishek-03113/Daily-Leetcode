#include<bits/stdc++.h>
using namespace std;

int arr[100001];


int main()
{
  {
	int t, n, i, j, k, a, b, c;
	cin >> t;
	while (t--) {
		cin >> n;
		cin >> k;
		while (k >= n) k -= n;
		for (i = 0; i < n; ++i) {
			cin >> arr[i];
		}
		for (i = n-k; i < n; ++i) {
			cout << arr[i] << " ";
		}
		for (i = 0; i < n-k; ++i) {
			cout << arr[i] << " ";
		} cout << endl;
	}

	return 0;
}

}