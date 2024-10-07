'''Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9.
Otherwise it should return false.
The length of the list can be less than 4 also.'''
def find_nine(nums):
    # Check the first 4 elements or the entire list if its length is less than 4
    return 9 in nums[:4]

nums = [1, 9, 4, 5, 6]
print(find_nine(nums))  # Output will be True
