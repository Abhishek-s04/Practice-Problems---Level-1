'''Write a python function which accepts a list of numbers and returns true if
the list contains a 2 next to a 2. Otherwise it should return false'''
def check_22(num_list):
    # Iterate through the list, checking pairs of elements
    for i in range(len(num_list) - 1):
        if num_list[i] == 2 and num_list[i + 1] == 2:
            return True  # Return True if two 2's are found next to each other
    return False  # Return False if no such pair is found

# Example input
print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))  
