#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long int nonzero_product = 1;
        int n = nums.size();
        int zero_count = 0;

        for( auto num: nums)
        {
            if(num != 0) nonzero_product = nonzero_product * num;
            if(num == 0) zero_count++;
        };

        vector<int> prodExSelf(n, 0);

        for(int x : prodExSelf)
        {
            cout << x << " " ;
        }

        cout <<  "\n" << zero_count;
        
        if( zero_count > 1 )
        {
            return prodExSelf;
        };

        for( int i=0; i<n; i++ )
        {
            if( zero_count == 1 )
            {
                if(nums[i] == 0) prodExSelf[i] = nonzero_product;
            }
            else
            {
                prodExSelf[i] = nonzero_product/nums[i]; 
            }
        };

        return prodExSelf;
    }
};
