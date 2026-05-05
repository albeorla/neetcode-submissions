class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Get the state
        zero_count, zero_idx = self._get_zero_info(nums)

        # 2. Route to the correct logic
        if zero_count > 1:
            return [0] * len(nums)
            
        if zero_count == 1:
            return self._calc_single_zero(nums, zero_idx)
            
        # 3. Default to standard logic
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res


    # --- Private Helpers ---
    def _get_zero_info(self, nums: List[int]):
        c = nums.count(0)
        return c, (nums.index(0) if c == 1 else None)

    def _calc_single_zero(self, nums: List[int], zero_idx: int) -> List[int]:
        res = [0] * len(nums)
        total_prod = 1
        for i, x in enumerate(nums):
            if i != zero_idx:
                total_prod *= x
        res[zero_idx] = total_prod
        return res
