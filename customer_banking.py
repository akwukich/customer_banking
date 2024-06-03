# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is your savings account balance? "))
    savings_interest = float(input("What is the APR for your savings account? "))
    savings_maturity = int(input("How many months of interest? "))

    # Call the create_savings_account function and pass the variables from the user.
    new_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The updated savings account balance is ${new_balance:.2f} and the interest earned is ${savings_interest_earned:.2f} for {savings_maturity} months.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("What is your CD account balance? "))
    cd_interest = float(input("What is the APR for your CD account? "))
    cd_maturity = int(input("What is the length of months for your CD? "))


    # Call the create_cd_account function and pass the variables from the user.
    cd_new_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The updated CD account balance is ${cd_new_balance:.2f} and the interest earned is ${cd_interest_earned:.2f} for {cd_maturity} months.")

if __name__ == "__main__":
    # Call the main function
    #create_savings_account(10000, 5, 6)
    #create_cd_account(20000, 8, 12)
    main()

    