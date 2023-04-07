menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENTED] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = 0 # initialize a variable to store the sum
    for item in order: # loop over the list of dictionaries
        subtotal += item["price"] # add the price of each item to the sum
    return subtotal # return the sum

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENTED] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tax = subtotal * 0.15 # multiply the subtotal by 0.15
    tax = round(tax, 2) # round the result to two decimal places
    return tax # return the tax

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENTED]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total
    """
    print('Summarizing order...')
    ### WRITE SOLUTION HERE
    subtotal = calculate_subtotal(order) # call calculate_subtotal function
    tax = calculate_tax(subtotal) # call calculate_tax function
    total = round(subtotal + tax, 2) # calculate total by adding subtotal and tax and rounding to two decimals
    names = [] # initialize an empty list to store names
    for item in order: # loop over the list of dictionaries
        names.append(item["name"]) # append the name of each item to the list
    return names, total # return a tuple of names and total
