class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                print(f"{target} = [{i}] {nums[i]} + [{j}] { nums[j]}")
                if i == j:
                    continue
                else:
                    z = nums[i] + nums[j]
                    if z == target:
                        return [i,j]
                        break




                     
                  

arry = [2,7,11,15]
tar = 9

arry1 = [3,2,4]
tar1 = 6

arry2 = [3,3]
tar2 = 6


arry3 = [2,5,5,11]
tar3 = 10

a = Solution()

print(a.twoSum(arry,9))
print(a.twoSum(arry1,6))
print(a.twoSum(arry2,6))
print(a.twoSum(arry3,10))