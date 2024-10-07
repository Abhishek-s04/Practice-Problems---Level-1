''' Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements.
The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.'''
def exchange_list(number_list):
    half = len(number_list) // 2
    l1=number_list[half:]
    l1_1=l1[::-1]
    l2=number_list[:half]
    new_number_list=l1_1+l2
    return new_number_list

number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))
