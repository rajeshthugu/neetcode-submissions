class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i, num in enumerate(nums):
            product = 1
            for j, n in enumerate(nums):
                if i != j:
                    product = product*n
            result.append(product)
        
        return result

        