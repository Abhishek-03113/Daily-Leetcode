#include <iostream>
using namespace std;

int main() {
	// your code goes here
	
	int n,t; 
	int maxT,maxN,sumN;
	
	cin >> t; 
	
	for (int i=0; i<t;i++)
	
	{
	    cin >>maxT>>maxN>>sumN;
	    int T = sumN/maxN;
	    int r = sumN%maxN;
	    
	    if (T<maxT)
	    {
	        cout << T*maxN*maxN + r*r <<endl;
	        
	    }
	    else
	    {
	        cout << maxT*maxN*maxN << endl;
	        
	    }
	    
	    
	    
	}
	return 0;
}
