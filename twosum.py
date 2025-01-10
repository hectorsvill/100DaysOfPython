

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
        
    i = 0
    while i < len(nums):
        x = nums[i]
        i_itter = i
        while i_itter < len(nums) -1:
            y_counter = i_itter + 1 
            y = nums[y_counter]
            print(f"{x} + {y} = {x+y}")

            if x + y == target:
                return [i, y_counter]
            else:
                i_itter+=1 
        i+=1    
    return []

# s = twoSum([3,2,4], 6)
s = twoSum([2,7,11,15], 9)
print(s)