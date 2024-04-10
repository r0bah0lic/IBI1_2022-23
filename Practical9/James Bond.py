def Bond(year):  #The Bond function
    if 1973 <= year+18 <= 1986:
        return('Roger Moore')
    if 1987 <= year+18 <= 1994:
        return('Timothy Dalton')
    if 1995 <= year+18 <= 2005:
        return('Pierce Brosnan')
    if 2006 <= year+18 <= 2021:
        return('Daniel Craig')
    else:
        return('OOPS!NO BOND')
birthyear= int(input('输入出生年份'))  #example on calling
result= Bond(birthyear)
print("你的天命邦德是",result)