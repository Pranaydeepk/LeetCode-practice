class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        def max_normal(arr,n):
            max_norm = arr[0]
            curr_max = arr[0]
            for i in range(1,n):
                curr_max = max(curr_max+arr[i],arr[i])
                max_norm = max(max_norm,curr_max)
            return max_norm      
        max_norm = max_normal(nums,n)
        if max_norm < 0:
            return max_norm
        arr_sum=0
        for i in range(n):
            arr_sum+=nums[i]
            nums[i]=-nums[i]
        max_circular=arr_sum+max_normal(nums, n)
        return max(max_circular, max_norm)
             
           
        # O(N^2)
        # res = nums[0]
        # n = len(nums)
        # for i in range(n):
        #     curr_sum = nums[i]
        #     curr_max = nums[i]
        #     for j in range(1,n):
        #         index = (i+j)%n
        #         curr_sum += nums[index]
        #         curr_max = max(curr_max,curr_sum)
        #     res = max(res,curr_max)
        # return res