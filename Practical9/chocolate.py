def chocolateaffordability(money, price):
    bars= money//price
    change=money%price
    return bars,change
money=int(input('How much do you have?'))  #example
price=int(input('How much is a bar of chocolate?'))
print(chocolateaffordability(money, price))