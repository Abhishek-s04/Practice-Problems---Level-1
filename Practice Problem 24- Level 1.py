# Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.
#lex_auth_0127136213490565121191
def find_gcd(num1, num2):
    # Ensure the inputs are positive integers
    if num1 <= 0 or num2 <= 0:
        return "Both numbers must be positive integers."
    
    # Implement the Euclidean algorithm to find GCD
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1

# Example input
num1 = 45
num2 = 90
print(find_gcd(num1, num2)) 
