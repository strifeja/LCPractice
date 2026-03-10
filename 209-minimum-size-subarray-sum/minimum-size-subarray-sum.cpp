class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0;
        int curr = 0;
        int min_len = INT_MAX;
        int result = 0;

        for (int j = 0; j < nums.size(); j++) {
            curr = curr + nums[j];
            while (curr >= target) {
                min_len = min(min_len, j - i + 1);
                curr = curr - nums[i];
                i++;
            }
        }

        result = (min_len == INT_MAX) ? 0 : min_len;
        return result;
    }
};