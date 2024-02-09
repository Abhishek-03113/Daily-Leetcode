#include<bits/stdc++.h> 
using namespace std ; 

bool isPalindrome(int arr[],int n)
{
	int j = 0; 

	for (int i = n-1; i >=0; i--)
	{
		if (arr[i] != arr[j])
		{
			return false;
		}
		j++;

	}

	return true ;
}

int main() {

	int n ; cin >> n; 
	int arr[n];
	bool flag;

	for (int i = 0 ; i < n; i++)
	{
		cin >> arr[i];
	}

	flag = isPalindrome(arr, n);

	if (flag) cout << "YES";
	else cout << "NO";	

}