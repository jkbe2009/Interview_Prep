
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def using_3_arrays():
            left = [1] * len(nums)
            right = [1] * len(nums)
            answer = [1] * len(nums)

            for i in range(1, len(nums)):
                left[i] = left[i-1] * nums[i-1]

            for i in range(len(nums)-2, -1, -1):
                right[i] = right[i+1] * nums[i+1]

            for i in range(len(nums)):
                answer[i] = left[i] * right[i]

            return answer


        def using_2_arrays():
            left = [1] * len(nums)
            answer = [1] * len(nums)

            for i in range(1, len(nums)):
                left[i] = left[i-1] * nums[i-1]

            product = 1

            for i in range(len(nums)-1, -1, -1):
                
                answer[i] = left[i] * product
                product *= nums[i]

            return answer


        def using_1_arrays():
            left = [1] * len(nums)

            for i in range(1, len(nums)):
                left[i] = left[i-1] * nums[i-1]

            product = 1

            for i in range(len(nums)-1, -1, -1):
                left[i] =  left[i] * product
                product *= nums[i]

            return left

        # return using_3_arrays()
        # return using_2_arrays()
        return using_1_arrays()
        