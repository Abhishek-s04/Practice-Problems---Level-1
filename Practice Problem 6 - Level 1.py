'''Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
Otherwise, it should return false.'''
def list123(nums):
    # Iterate through the list, checking if the sequence 1, 2, 3 appears
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

nums = [1, 2, 3, 4, 5]
print(list123(nums))  
