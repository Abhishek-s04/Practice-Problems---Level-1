'''Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
It should return a list in which the first value should be letter count and second value should be digit count.
Ignore the spaces or any other special character in the sentence.'''
def count_digits_letters(sentence):
    # Initialize counters for letters and digits
    letter_count = 0
    digit_count = 0
    
    # Iterate through each character in the sentence
    for char in sentence:
        if char.isalpha():  # Check if the character is a letter
            letter_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
    
    # Create a list with the letter count and digit count
    result_list = [letter_count, digit_count]
    
    return result_list

sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))  # Output will be [12, 6]
