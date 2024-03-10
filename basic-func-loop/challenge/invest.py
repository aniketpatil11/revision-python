# Investment tracker
def invest(amount, rate, years): 
    for i in range(years): 
        amount += (amount * rate)
        print(f" The amount for year {i+1} is : {amount:.2f}")


invest(100,0.05,5)