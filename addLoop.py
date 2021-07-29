def addLoop(groceries):
    print(groceries)
    price = 0.00
    for x in groceries:
        price = price + x    
    return price

#main
groceryPrices = [12.12, 13.23, 6.00]
print(addLoop(groceryPrices))
print(sum(groceryPrices))