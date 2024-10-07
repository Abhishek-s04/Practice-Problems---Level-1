'''Write a python function which accepts a list of strings containing details of
deposits and withdrawals made in a bank account and returns the net amount in the account.
Suppose the following input is supplied to the function 
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.'''
def calculate_net_amount(trans_list):
    net_amount = 0  # Initialize the net amount as 0
    
    # Iterate through each transaction in the list
    for transaction in trans_list:
        action, amount = transaction.split(":")  # Split the transaction into action (D/W) and amount
        amount = int(amount)  # Convert the amount to an integer
        
        # Update the net amount based on the action
        if action == "D":
            net_amount += amount  # Add for deposits
        elif action == "W":
            net_amount -= amount  # Subtract for withdrawals
    
    return net_amount

trans_list = ["D:300", "D:200", "W:200", "D:100"]
print(calculate_net_amount(trans_list)) 
