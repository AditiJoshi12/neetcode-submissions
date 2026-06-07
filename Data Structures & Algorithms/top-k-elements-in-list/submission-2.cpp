class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int, int> counts; 
        
        for( auto num : nums)
        {
            counts[num]++;            
        }; 

        vector<pair<int, int>> freq;

        for( auto it: counts )
        {
            freq.push_back({it.second, it.first});
        }; 

        sort( freq.begin(), freq.end(), greater<pair<int, int>>());

        vector<int> ans;

        for(int i=0; i<k; i++)
        {
            ans.push_back(freq[i].second);
        };

        return ans;
    };
};
