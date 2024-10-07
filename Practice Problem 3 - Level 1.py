''' Write a python function to create and return a new dictionary from the given dictionary(item:price).
Given the following input, create a new dictionary with elements having price more than 200.
prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}'''
def create_new_dictionary(prices):
    # Create a new dictionary with items having price more than 200
    new_dict = {item: price for item, price in prices.items() if price > 200}
    
    return new_dict

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
print(create_new_dictionary(prices))
