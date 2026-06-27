class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = list(set(nums))
        if(len(unique_numbers) == len(nums)):
            return False
        else:
            return True