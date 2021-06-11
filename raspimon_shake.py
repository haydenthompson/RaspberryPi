from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

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
shake_left = [
        k, k, k, k, k, k, k, k,
        w, w, w, w, w, w, k, k,
        w, k, k, k, k, w, w, k,
        w, w, k, w, k, w, k, w,
        w, k, p, k, k, w, k, k,
        w, w, w, w, w, w, k, k,
        k, w, k, k, w, k, k, k,
        k, k, w, k, k, w, k, k
        ]

shake_right = [
        k, k, k, k, k, k, k, k,
        k, k, w, w, w, w, w, w,
        k, w, w, k, k, k, k, w,
        w, k, w, k, w, k, w, w,
        k, k, w, k, k, p, k, w,
        k, k, w, w, w, w, w, w,
        k, k, k, k, w, k, w, k,
        k, k, k, w, k, w, k, k
        ]

sense.set_pixels(shake_right) #set your own Raspimons here as default rest pose
while True:
    accel = sense.get_accelerometer_raw()
    print (accel)
    sense.set_pixels(rest) #set your own Raspimons here as default rest pose
    
    x = accel["x"]#get each seperate float value
    y = accel["y"]
    z = accel["z"]
    
    x = abs(x) #changes all neg to pos values
    x = round(x,3) #round x to 3 decimal places ex:0.02
    print("x : " +  x)
    y = abs(y)
    y = round(y,3)
    z = abs(z)
    z = round(z,3)
    
sum = x+y
sleep(.3)

if sum > 0.3:
    print("Tap")
    sense.set_pixels(tapped)
    random_choice = random.choice(laughs)
    sense.show_message(random_choice)
    sleep(.5)
    

#define your shake() function here:


    
#add your while True: loop below
