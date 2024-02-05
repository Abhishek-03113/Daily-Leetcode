#include<bits/stdc++.h> 
using namespace std ; 

int main() {

	char ch ; cin >> ch; 
	int asc; 
	asc = (int)(ch);

	if (64 < asc && asc  < 92) {cout << "ALPHA" << "\n" << "IS CAPITAL" ;}
	else if (96 < asc && asc < 124) {cout << "ALPHA" << "\n" << "IS SMALL" ; }
	else cout << "IS DIGIT";


}