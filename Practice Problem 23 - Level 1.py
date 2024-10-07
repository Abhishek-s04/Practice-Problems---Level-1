''' Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.'''
def divisible_by_sum(number):
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in digits)
    
    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0

number = 42
print(divisible_by_sum(number)) 
