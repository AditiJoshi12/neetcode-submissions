class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_str = "";

        for(auto str : strs)
        {
            encoded_str = encoded_str + to_string(str.size()) + "#" + str;
        };

        return encoded_str;
    }

    vector<string> decode(string s) {
        vector<string> strs; 

        int n = s.size(); 
        int i = 0;

        while(i < n)
        {
            int j = i;

            while(s[j] != '#')
            {
                j++;
            } ;

            int len = stoi(s.substr(i, j-i));

            string str = s.substr(j+1, len);

            strs.push_back(str);

            i = len+j+1;
        };

        return strs;
    }
};
