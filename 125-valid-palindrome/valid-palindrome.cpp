class Solution {
public:
    bool isPalindrome(string s) {
        string news;
        for( char c : s ){
            if ( isalnum(c) ){
                news += tolower(c);
            }
        }

        int left = 0;
        int right = news.size() - 1;
        while( left < right ){
            if( news[left] != news[right] ){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};