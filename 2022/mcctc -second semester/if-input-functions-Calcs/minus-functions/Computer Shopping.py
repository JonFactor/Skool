from cgitb import small
import imp


msiRtxa5000Price = 4199.35
gigabyteAeroPrice = 4295.54
raxerBlande15Price = 3696.99
asusZephyrusM16Price = 1849.79

computers = [msiRtxa5000Price, gigabyteAeroPrice, raxerBlande15Price, asusZephyrusM16Price]

biggest = max(computers)

smallest = min(computers)

msiRtxa5000Price2 = round(msiRtxa5000Price)
gigabyteAeroPrice2 = round(gigabyteAeroPrice)
raxerBlande15Price2 = round(raxerBlande15Price)
asusZephyrusM16Price2 = round(asusZephyrusM16Price)

print (f"""
 The most expencive laptop amount is: {biggest}
 The least ecpenceive laptop amount is: {smallest}
 The rounded price of msiRtxa5000P is {msiRtxa5000Price2}
 The rounded price of the gigabyteAeroPrice is {gigabyteAeroPrice2} 
 The rounded price of the raxerBlande15 is {raxerBlande15Price2} 
 The rounded price of the asusZephyrusM16 is {asusZephyrusM16Price2}""")