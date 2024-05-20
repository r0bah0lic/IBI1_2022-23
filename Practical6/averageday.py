sleeping=8
classes=6
studying=3.5
TV=2
music=1
other=24-sleeping-classes-studying-TV-music

dic={'sleeping':sleeping,'classes':classes,'studying':studying,'TV':TV,'music':music,'other':other} #create overall dictionary
activity=list(dic.keys()) #fetch keys of dic as activity list
time=list(dic.values()) #fetch values of dic as time list
print(dic)
import matplotlib.pyplot as plt
plt.pie(x=time,labels=activity) #draw the picture,with 'activity' as labels and 'time' as sizes
plt.show()
print(sum(time)/len(time))  #calculate the average time of activity