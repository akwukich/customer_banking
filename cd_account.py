"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # interest_earned = balance * ((interest_rate/100)*(months/12))
    # updated_CD = balance + interest_earned
    # return updated_CD, interest_earned

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    # cd_data = Account(cd_balance, cd_interest)
    CDAccount = Account(balance, 0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    cd_interest_earned = balance * ((interest_rate/100)*(months/12))

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    cd_new_balance = balance + cd_interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    CDAccount.set_balance(cd_new_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    CDAccount.set_interest(cd_interest_earned)

    # Return the updated balance and interest earned.
    return cd_new_balance, cd_interest_earned