class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 1;
        int indicator = false;

        for( int i = 1; i < nums.size(); i++ ){
            if( nums.at(i) != nums.at(i-1) ){
                indicator = false;
                nums.at(k) = nums.at(i);
                k++;
            } else if( indicator == true ) {
                continue;
            } else if( indicator == false ){
                indicator = true;
                nums.at(k) = nums.at(i);
                k++;
            }
        }
        return k;
    }
};