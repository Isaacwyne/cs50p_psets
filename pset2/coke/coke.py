def main():
    # initialize 'amount_due' to the total_cost of the coke
    amount_due = 50
    # check if amount_due is not 0 and continue with the evaluation
    while amount_due > 0:
        print(f'Amount Due {amount_due}')
        # prompt the user to insert a coin and check if it is valid i.e. '5, 10, 25'
        try:
            coin = int(input('Insert coin: '))
            if coin in [5, 10, 25]:
                amount_due -= coin
        except ValueError:
            print("Oops! That's not a valid positive interger. Try again")

    # return the absolute value of amount_due that is less than 0
    change_owed = abs(amount_due)
    print(f'Change Owed: {change_owed}')

    
if __name__ == '__main__':
    main()
