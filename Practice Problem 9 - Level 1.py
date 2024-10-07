'''Write a Python function which generates and returns a dictionary where the
keys are numbers between 1 and n (both inclusive) and the values are square of keys.'''
def generate_dict(number):
    # Create a dictionary using a dictionary comprehension
    new_dict = {i: i**2 for i in range(1, number + 1)}
    
    return new_dict

number = 20
print(generate_dict(number))
