#include <iostream>
using namespace std;


int main() {
	int t;
	for (int i = 0; i<t;i++)
	{
		int n,k;
		int arr[n];

		cin >> n >> k ;

		for (int i =0;i<n;i++)
		{
			cin >> arr[i];
		}


		for(int i = 0;i<k;i++)
		{
			int temp = arr[n-1];
			
			for (int j = n-1;j>0;j--)
			{
				arr[j] = arr[j-1];
			}
			arr[0] = temp;
			
		}
		
        for (int i = 0;i <n;i++)
        {
            cout << arr[i];
        }

	}
}