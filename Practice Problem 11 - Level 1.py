''' Write a python function which accepts a sentence and returns a list in which first value is the count of 
upper case letters and second value is the count of lower case letters in the sentence.
Ignore spaces, numbers and other special characters if any.'''
def find_upper_and_lower(sentence):
    upper_count = 0  # Initialize count for uppercase letters
    lower_count = 0  # Initialize count for lowercase letters
    
    # Iterate through each character in the sentence
    for char in sentence:
        if char.isupper():  # Check if the character is uppercase
            upper_count += 1
        elif char.islower():  # Check if the character is lowercase
            lower_count += 1
            
    # Create a result list with counts of uppercase and lowercase letters
    result_list = [upper_count, lower_count]
    
    return result_list

sentence = "Come Here"
print(find_upper_and_lower(sentence)) 
