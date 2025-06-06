
""" 
Find maximum sub array ?
 arr = [1,2,3,4]
"""


""" 
Two sum

"""
# O(n^2)
def twoSum(nums: list[int], target: int) -> list[int]:

    # # O(n^2)
    # size=len(nums)
    # for i in range(size):
    #     for j in range(1, size):
    #         if (nums[i] + nums[j] == target and i!=j):
    #             return i, j
            
    
    # # O(nlogn) - optimized ---- Two Pointer
    # i=0
    # j=len(nums)-1
    # nums.sort()
    # while i<=j:
    #     if (nums[i] + nums[j]) == target:
    #         return i, j
    #     elif (nums[i]+nums[j]) > target:
    #         j-=1
    #     elif (nums[i]+nums[j]) < target:
    #         i+=1
    
    # O(n) - more optimized ----- Hash-map
    hashmap={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return hashmap[complement], i
        
        hashmap[num]=i


if __name__ == "__main__":
    print(twoSum([4,2,5,6,8], target=8))

