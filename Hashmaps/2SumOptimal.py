class Solution(object):
    def twoSum(self, nums, target):
        known={}
        for i in range(len(nums)):
            required = target - nums[i]

            if required in known:
                return [known[required],i]

            known[nums[i]] = i