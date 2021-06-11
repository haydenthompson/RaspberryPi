from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Eggsy" , "Galbert" , "Bacon" , "Pancake" , "Kat-Kat"]

names.append("Another")

sense.show_message(names[0]) #scrolls the second element 

#Colors:

r = (255, 0, 0 ) # RED color, no green or blue
w = (255, 255, 255) #white, all colors maxed out
k = (0, 0, 0) # black means zero amounts of red, green and blue
g = (0,102,0) #green

#define another color. Use one letter variable names to make it easy later

raspimon = [
g, k, k, k, k, k, k, g,
k, g, k, k, k, k, g, k,
k, k, g, g, g, g, k, k,
k, g, w, g, g, w, g, k,
k, k, g, g, g, g, k, k,
g, g, g, g, g, g, g, g,
g, k, g, k, k, g, k, g,
g, k, g, g, g, g, k, g
]

#my new design up above
 
sense.set_pixels(raspimon) #set pixel will change the color of a single pixel if needed, Use 7x7 grid to dertmine values of (x,y) like graphics

#add a one-pixel mouth
#sense.set_pixel(3,4, [255,0,0])

#TODO: 8x8 pixel art options
test_raspimon = [
g, k, k, k, k, k, k, g,
k, g, k, k, k, k, g, k,
k, k, g, g, g, g, k, k,
k, g, k, g, g, k, g, k,
k, k, g, g, g, g, k, k,
g, g, g, g, g, g, g, g,
g, k, g, k, k, g, k, g,
g, k, g, g, g, g, k, g
]


#original design
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, g, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k




