''' Given a string, write a python function to return True if the strings "mat" and "jet" appear 
the same number of times in the given string, else return False.
Note: Perform case insensitive string comparison wherever necessary.'''
#lex_auth_0127136253311385601197
def check_occurence(string):
    # Convert the string to lowercase to make the search case insensitive
    lower_string = string.lower()
    
    # Count occurrences of "mat" and "jet"
    mat_count = lower_string.count("mat")
    jet_count = lower_string.count("jet")
    
    # Return True if both counts are equal, otherwise return False
    return mat_count == jet_count

# Example input
string = "Jet on the Mat but mat is too long"
print(check_occurence(string))
