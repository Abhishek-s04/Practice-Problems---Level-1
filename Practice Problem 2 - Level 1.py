''' Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct.
Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.'''
def bracket_pattern(input_str):
    # Check if the pattern starts with a closing bracket or ends with an opening bracket
    if input_str[0] == ')' or input_str[-1] == '(':
        return False
    
    # Initialize a counter to check the balance of brackets
    count = 0
    
    # Iterate through each character in the string
    for char in input_str:
        if char == '(':
            count += 1  
        elif char == ')':
            count -= 1  
        if count < 0:
            return False
    
    # If the count is 0 at the end, the brackets are balanced
    return count == 0

input_str = "(())("
print(bracket_pattern(input_str))  # Output will be False
