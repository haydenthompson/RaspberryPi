from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

#replace with your own colors and Raspimons
w = (255,255,255)
p = (128,0,128)
k = (0, 0, 0)


rest = [
        k, k, k, k, k, k, k, k,
        k, w, w, w, w, w, w, k,
        k, w, k, k, k, k, w, k,
        k, w, w, k, w, k, w, k,
        k, w, k, w, k, k, w, k,
        k, w, w, w, w, w, w, k,
        k, k, w, k, w, k, k, k,
        k, k, w, k, w, k, k, k
        ]
tapped = [
        k, k, k, k, k, k, k, k,
        k, p, p, p, p, p, p, k,
        k, p, k, k, k, k, p, k,
        k, p, p, k, p, k, p, k,
        k, p, k, p, k, k, p, k,
        k, p, p, p, p, p, p, k,
        k, k, p, k, p, k, k, k,
        k, k, p, k, p, k, k, k
        ]


#make the system lauh once tapped
laughs =["hahaha", "haaaaaa!", "hohoho", "heee heee"]

#add a while True: loop below
while True:
    accel = sense.get_accelerometer_raw()
    print (accel)
    sense.set_pixels(rest) #set your own Raspimons here as default rest pose
    
    x = accel["x"]#get each seperate float value
    y = accel["y"]
    z = accel["z"]
    
    x = abs(x) #changes all neg to pos values
    x = round(x,3) #round x to 3 decimal places ex:0.02
    y = abs(y)
    z = abs(z)
    
sum = x+y
sleep(.3)

if sum > 0.3:
    print("Tap")
    sense.set_pixels(tapped)
    random_choice = random.choice(laughs)
    sense.show_message(random_choice)
    sleep(.5)
    
    
    
    


