class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int temp = nums[0], cnt = 0;
        for(int i=0;i<nums.size();++i){
            if(nums[i]==temp){
                ++cnt;
            }else{
                --cnt;
                if(cnt==0){
                    temp=nums[i];cnt=1;
                }
            }
            // cout<<cnt<<nums[i]<<endl;
        }
        return temp;
    }
};