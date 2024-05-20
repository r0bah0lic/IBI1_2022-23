a=5 #a refers to the current density
i=0 #i refers to the days passed
while a <= 90: 
    i+=1
    a=a*2 #double the density until it's over 90%
print("I could rest for",i-1,"days")
