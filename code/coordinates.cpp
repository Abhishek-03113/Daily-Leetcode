#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	double a, b ; cin >> a >> b ; 

	if( a == 0 && b == 0){
			cout << "Origem";
	}

	if (a == 0 && b != 0 ){
		cout << "Eixo Y";
	}
	if (b == 0 && a != 0 ){
		cout << "Eixo X";
	}


	if (a > 0 && b > 0)
	{
		cout << "Q1";

	}
	if (a < 0 && b > 0)
	{
		cout << "Q2";
		
	}
	if (a < 0 && b < 0)
	{
		cout << "Q3";
		
	}
	if (a > 0 && b < 0)
	{
		cout << "Q4";
		
	}

}