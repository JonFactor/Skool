import numbers
import numpy
import re
import os
g1 = open("week_10\BPA\Grill_1.txt", "r")
g2 = open("week_10\BPA\Grill_2.txt", "r")
g3 = open("week_10\BPA\Grill_3.txt", "r")
g4 = open("week_10\BPA\Grill_4.txt", "r")
g5 = open("week_10\BPA\Grill_5.txt", "r")
g12 = ""
g22 = ""
g32 = ""
g42 = ""
g52 = ""
thingy = 0

sum1 = 0
min1 = 0
max1 = 0
mean1 = 0
stand1 = 0

sum2 = 0
min2 = 0
max2 = 0
mean2 = 0
stand2 = 0

sum3 = 0
min3 = 0
max3 = 0
mean3 = 0
stand3 = 0

sum4 = 0
min4 = 0
max4 = 0
mean4 = 0
stand4 = 0

sum5 = 0
min5 = 0
max5 = 0
mean5 = 0
stand5 = 0

#read 1
for line in g1:
    g12 += g1.readline()

g12 = [int(i) for i in g12.split() if i.isdigit()]

g1.close()


#read 2
for line in g2:
    g22 += g2.readline()

g22 = [int(i) for i in g22.split() if i.isdigit()]

g2.close()

#read3

for line in g3:
    g32 += g3.readline()

g32 = [int(i) for i in g32.split() if i.isdigit()]

g3.close()

#read4
for line in g4:
    g42 += g4.readline()

g42 = [int(i) for i in g42.split() if i.isdigit()]

g4.close()

#read5

for line in g5:
    g52 += g5.readline()

g52 = [int(i) for i in g52.split() if i.isdigit()]

g5.close()
#min1 pf
    
if min1 <= mean1 - stand1*2 and max1 >= mean1 + stand1*2:
    pf1 = "Too Hot and Too Cold: Fail!"
elif min1 <= mean1 - stand1*2:  
    pf1 = "Too Cold: Fail!"
elif max1 >= mean1 + stand1*2:
    pf1 = "Too Hot: Fail!"
else:
    pf1 = "Pass!"

#min 2 pf
if min2 <= mean2 - stand2*2 and min2 >= mean2 + stand2*2:
    pf2 = "Too Hot and Too Cold: Fail!"
elif min2 <= mean2 - stand2*2:  
    pf2 = "Too Cold: Fail!"
elif min2 >= mean2 + stand2*2:
    pf2 = "Too Hot: Fail!"
else:
    pf2 = "Pass!"

#min3 pf

if min3 <= mean3 - stand3*2 and min3 >= mean3 + stand3*2:
    pf3 = "Too Hot and Too Cold: Fail!"
elif min3 <= mean3 - stand3*2:  
    pf3 = "Too Cold: Fail!"
elif min3 >= mean3 + stand3*2:
    pf3 = "Too Hot: Fail!"
else:
    pf3 = "Pass!"

#min4 pf

if min4 <= mean4 - stand4*2 and min4 >= mean4 + stand4*2:
    pf4 = "Too Hot and Too Cold: Fail!"
elif min4 <= mean4 - stand4*2:  
    pf4 = "Too Cold: Fail!"
elif min4 >= mean4 + stand4*2:
    pf4 = "Too Hot: Fail!"
else:
    pf4 = "Pass!"

#min5 pf
if min5 <= mean5 - stand5*2 and min5 >= mean5 + stand5*2:
    pf5 = "Too Hot and Too Cold: Fail!"
elif min5 <= mean5 - stand5*2:  
    pf5 = "Too Cold: Fail!"
elif min5 >= mean5 + stand5*2:
    pf5 = "Too Hot: Fail!"
else:
    pf5 = "Pass!"

def Calculate():
    # global mean1, stand1, sum1, min1, max1, mean2, stand2, sum2, min2, max2, max3, min3, sum3, stand3, mean3, max4, min4, sum4, stand4, mean4, max5, min5, sum5, stand5, mean5, g52
    global mean1, stand1, sum1, min1, max1, mean2, stand2, sum2, min2, max2, max3, min3, sum3, stand3, mean3, max4, min4, sum4, stand4, mean4, max5, min5, sum5, stand5, mean5
    #1st
    max1 = max(g12)
    min1 = min(g12)
    sum1 = sum(g12)

    mean1 += sum1 / len(g12)
    stand1 += numpy.std(g12)
    #2cnd
    max2 = max(g22)
    min2 = min(g22)
    sum2 = sum(g22)

    stand2 += numpy.std(g22)
    mean2 += sum2 / len(g22)
    #3rd
    max3 = max(g32)
    min3 = min(g32)
    sum3 = sum(g32)

    stand3 += numpy.std(g32)
    mean3 += sum3 / len(g32)
    #4th
    max4 = max(g42)
    min4 = min(g42)
    sum4 = sum(g42)

    stand4 += numpy.std(g42)
    mean4 += sum4 / len(g42)
    #5th

    #max5 = max(g52)
    #min5 = min(g52)
    #sum5 = sum(g52)

    #stand5 += numpy.std(g52)
    #mean5 += sum5 / len(g52)

Calculate()
def Print():
    global gnum, mins, maxs, mean, stand, pfs, min1, max1, mean1, stand1, pf1, min2, max2, mean2, stand2, pf2, thingy
    while thingy <=4 :
        if thingy == 0:
            gnum = 1
            mins = min1
            maxs = max1
            mean = mean1
            stand = stand1
            pfs = pf1
        elif thingy == 1:
            gnum = 2
            mins = min2
            maxs = max2
            mean = mean2
            stand = stand2
            pfs = pf2       
        elif thingy == 2:
            gnum = 3
            mins = min3
            maxs = max3
            mean = mean3
            stand = stand3
            pfs = pf3     
        elif thingy == 3:
            gnum = 4
            mins = min4
            maxs = max4
            mean = mean4
            stand = stand4
            pfs = pf4       
        elif thingy == 4:
            gnum = 5
            mins = min5
            maxs = max5
            mean = mean5
            stand = stand5
            pfs = pf5        
        print(f" Grill",gnum,":\n Min:",mins,"\n Max:",maxs,"\n Mean:",mean,"\n Standard Deviation of temps is",stand,"\n",pfs)

        thingy +=1
Print()