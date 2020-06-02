https://leetcode.com/problems/reverse-string/

//Solution 1
class Solution {
public:
    void reverseString(vector<char>& s) {
        
        char curr ;
        for ( int i =0; i < s.size() /2; i++){
            curr = s[i];
            s[i] = s[s.size()- 1 -i];
            s[s.size() -1 - i] = curr;
        }
    }
};


//Solution 2
