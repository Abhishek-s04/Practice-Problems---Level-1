# Write a python function that accepts a list of words and returns the list of integers representing the length of the corresponding words.
#lex_auth_0127136291543285761194

def list_of_count(word_list):
    #start writing your code here
    count_list = [len(word) for word in word_list]
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))

