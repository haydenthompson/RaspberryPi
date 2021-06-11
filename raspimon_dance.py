from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

#colors
r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0)   #blank (black)
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

#load the Raspimons you want to animate
open_eyes = [
    k, k, d, d, d, d, k, k,
    k, d, d, w, d, w, d, k,
    d, d, d, k, d, k, d, d,
    d, d, r, d, d, d, r, d,
    p, p, d, d, k, d, d, p,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ]        

closed_eyes =[
    k, k, d, d, d, d, k, k,
    k, d, d, d, d, d, d, k,
    d, d, d, d, d, d, d, d,
    d, d, r, d, d, d, r, d,
    p, p, d, d, k, d, d, p,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ]
    
pi_logo=[
    g, g, g, w, w, g, g, g,
    w, g, g, g, g, g, g, w,
    w, w, g, g, g, g, w, w,
    w, w, r, r, r, r, w, w,
    w, r, r, r, r, r, r, w,
    r, r, r, r, r, r, r, r,
    w, r, r, r, r, r, r, w,
    w, w, r, r, r, r, w, w,
    ]
    
face_smile= [
    k, k, k, k, k, k, k, k,
    k, k, k, k, k, k, k, k,
    k, w, k, k, k, k, w, k,
    k, k, k, k, k, k, k, k,
    k, k, k, k, k, k, k, k,
    k, w, k, k, k, k, w, k,
    k, k, w, w, w, w, k, k,
    k, k, k, k, k, k, k, k,
    ]
    
creeper_face= [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, k, k, g, g, k, k, g,
    g, k, k, g, g, k, k, g,
    g, g, g, k, k, g, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, g, g, k, g, g,
    ]
 
 

for i in range(20):
  #animate your raspimon!
    sense.set_pixels(open_eyes)
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.5)
  
  
while True:
    sense.set_pixels(open_eyes)
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.5)
    #danceforever!
    
while True:
    for i in range(8):
          sense.set_pixels(open_eyes)
          sleep(.4)
          sense.set_pixels(closed_eyes)
          sleep(.2)
          
    for i in range (10):
        sense.flip_v()
        sleep(.3)
    

