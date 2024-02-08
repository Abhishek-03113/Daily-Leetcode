#include<bits/stdc++.h> 
using namespace std ; 

bool isLucky(int temp)
{ 
while (temp != 0)
	{
		int digit = temp % 10;

		if ((digit != 4))
		{
			if (digit != 7)
			{
				return false;
			}
		}
		temp = floor(temp/10);
	}

	return true; 
}

int main() {
	int a,b,cnt; cin >> a >> b;
	cnt = 0 ;

	for (int i = a; i<= b; i++)
	{ 
		int temp = i; 

		if (isLucky(temp))
		{
			cout << temp << " "; 
			cnt++;
		}

	}

	if (cnt == 0){
		cout << -1 << endl; 
	}

}