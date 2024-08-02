class Solution {
public:
    int reverse(int x) {
        ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        long limit= pow(2,31) ; 
        

        if (x < 0){
            long reverse = 0; 
            long temp = abs(x);
            int i = 0 ;
            while (temp){
                int digit = temp%10; 
                reverse += 10*i + digit;
                i++; 
                temp = temp/10;
            }

            if (reverse <= limit){
                return 0 - reverse;
            }
        }
        else{
            long reverse = 0; 
            long temp = abs(x);
            int i = 0 ;
            while (temp){
                int digit = temp%10; 
                reverse += 10*i + digit;
                i++; 
                temp = temp/10;
            }
             if (reverse <= limit){
                return reverse;
            }

        }

        return 0 ;
        }
        
    };
};