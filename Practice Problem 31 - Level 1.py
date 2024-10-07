'''Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list. 
Note: Don't add the given number and also the numbers present before and after the given number in the list.'''
def sum_of_elements(num_list, number):
    result_sum = 0
    skip_indices = []

    for i in range(len(num_list)):
        if num_list[i] == number:
            skip_indices.append(i)
            if i > 0:
                skip_indices.append(i - 1)
            if i < len(num_list) - 1:
                skip_indices.append(i + 1)

    for i in range(len(num_list)):
        if i not in skip_indices:
            result_sum += num_list[i]

    return result_sum

num_list = [1, 7, 3, 4, 1, 7, 10, 5]
number = 7
print(sum_of_elements(num_list, number)) 
