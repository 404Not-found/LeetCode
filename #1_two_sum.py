class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index_x, base in enumerate(nums):
            for index_y, num in enumerate(nums):
                if index_x != index_y:
                    if base + num == target:
                        return [index_x,index_y]
                else:
                    continue


s = Solution()


# Test case
nums = [2,7,11,2]
target = 4

result = s.twoSum(nums, target)

        