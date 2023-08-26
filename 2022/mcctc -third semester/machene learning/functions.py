#Intro To functions
### 3/ 13
# Your code below:
def three():
    def directions_to_timesSq(): # making functions
        print('Walk 4 mins to 34th St Herald Square train station')
        print('Take the Northbound N, Q, R, or W train 1 stop')
        print('Get off the Times Square 42nd Street stop')
### 4/13
def four(): # calling functions
    def directions_to_timesSq():
        print('Walk 4 mins to 34th St Herald Square train station')
        print('Take the Northbound N, Q, R, or W train 1 stop')
        print('Get off the Times Square 42nd Street stop')
        print("Take lots of pictures!")
    directions_to_timesSq()
### 5/13
def five():# function order
    def weather_check():
        print('Looks great outside! Enjoy your trip.')
    print('False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.')
    weather_check()