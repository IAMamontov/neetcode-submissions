class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_of_products = []
        array_of_products.append(1)

        for i in range(1, len(nums)):
            array_of_products.append(array_of_products[i - 1] * nums[i - 1])
        suffix_mult = 1
        for i in range(len(nums) - 1, -1, -1):
           array_of_products[i] *= suffix_mult
           suffix_mult *= nums[i]
        return array_of_products
