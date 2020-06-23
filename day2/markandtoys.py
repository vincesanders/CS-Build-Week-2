def maximumToys(prices, k):
    # sort prices using timsort.
    prices.sort() # O(nlogn)

    # initialize variables representing the money we've spent and the number of toys we've bought.
    money_spent = 0
    num_toys = 0

    # iterate through sorted prices, keeping a running tally of money spent
    # and the number of toys we've bought
    for price in prices:

        # When we get to an amount that can't be added, we break out of the loop.
        if money_spent + price > k:
            break

        # Otherwise, we add the price of the toy we bought to money spent
        # and increment the number of toys we've bought
        money_spent += price
        num_toys += 1

    # Return the total number of toys we were able to buy with our budget.
    return num_toys