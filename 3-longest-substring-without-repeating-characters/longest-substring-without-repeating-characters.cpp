class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int result = 0;

        // integer keeps track of index of last
        unordered_map<char, int> freq;

        for (int j = 0; j < s.size(); j++) {
            char c = s[j];
            
            while (freq.count(c) && freq[c] >= i) {
                i++;
            }

            freq[c] = j;
            result = max(result, j - i + 1);
        }

        return result;
    }
};