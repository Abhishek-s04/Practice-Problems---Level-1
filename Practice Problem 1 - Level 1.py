''' Write a python function to add 'ing' at the end of a given string and return the new string. 
If the given string already ends with 'ing' then add 'ly'.
If the length of the given string is less than 3, leave it unchanged.'''
def add_string(str1):
    # Check if the length of the string is less than 3
    if len(str1) < 3:
        return str1
    # Check if the string ends with 'ing'
    elif str1.endswith('ing'):
        return str1 + 'ly'
    # Add 'ing' if the string doesn't end with 'ing'
    else:
        return str1 + 'ing'

str1 = "com"
print(add_string(str1))
