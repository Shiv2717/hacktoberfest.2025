	class Solution:

	    def rob(self, nums: List[int]) -> int:

	        n = len(nums)

	        if n == 1:

	            return nums[0]

	        if n == 2:

	            return max(nums[0], nums[1])

	 

	        memo = {0:nums[0], 1:max(nums[0], nums[1])}

	 

	        def helper(i):

	            if i in memo:

	                return memo[i]

	            else:

	                memo[i] = max(nums[i] + helper(i-2),

	                              helper(i-1))

	                return memo[i]

	        

	        return helper(n-1)

	        # Time: O(n)

	        # Space: O(n)

	 
