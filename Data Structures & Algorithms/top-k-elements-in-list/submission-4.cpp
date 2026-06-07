class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int, int> counts; 
        int n = nums.size(); 
        for( auto num : nums)
        {
            counts[num]++;            
        }; 

        vector<vector<int>> bucket(nums.size()+1); 

        for( auto it: counts)
        {
            bucket[it.second].push_back(it.first);
        };

        vector<int> ans;
        int a = 0; 

        for(int i = n; i >= 0; i--)
        {
            for( int num : bucket[i] )
            {
                ans.push_back(num);
                a++;

                if(a == k )
                {
                    return ans;
                };
            };
        };

        return ans;
    };
};
