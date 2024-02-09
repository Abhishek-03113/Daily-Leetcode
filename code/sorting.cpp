#include<bits/stdc++.h> 
using namespace std ; 


void sort(int n,int arr[])
{
	int i, j, min; 

	for (int i= 0; i < n-1; i++)
	{
		min = i;

		for (j = i + 1 ; j < n; j++)
		{
			if (arr[j] < arr[min]) min = j;
		}

		if (min != i){
			swap(arr[min],arr[i]);
		}
	}
}


int main() {
	int n; cin >> n ; 

	int arr[n];

	for (int i = 0; i<n; i++)
	{
		cin >> arr[i]; 
	}

	sort(n,arr);

	for (int j = 0; j < n; j++)
	{
		cout << arr[j] << " ";
	}

	return 0 ; 
}