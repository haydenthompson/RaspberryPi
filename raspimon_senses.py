from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#declare a temperature variable and assign it the value of sense.get_temperature()
temperature = sense.get_temperature()
temperature = temperature * 9/5 +32
temperature = int(temperature)

#print out type statements:
print(type(temperature)) #prints <class 'float>
print(type("Hello!")) #prints <class 'str>
print(type(12)) #prints <class 'int>'

sense.show_message(str(temperature)) #a nested function
    #print(type("Hello!"))
    #sense.show_message(temperature) -> this will only work for Strings. The temperature value is a float, or a number

#Create humidity
humidity = sense.get_humidity()
humidity = int(humidity)

#humidity print statement
print(type(humidity)) #prints <class 'float>
print(type("Hello!")) #prints <class 'str>
print(type(12)) #prints <class 'int>'

sense.show_message(str(humidity))


#Establish all variables for temp color changes
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

raspimon_hot = [
  k, k, k, k, k, k, k, k,
  k, r, r, r, r, r, r, k,
  k, r, k, k, k, k, r, k,
  k, r, r, k, r, k, r, k,
  k, r, k, k, k, k, r, k,
  k, r, r, r, r, r, r, k,
  k, k, r, k, r, k, k, k,
  k, k, r, k, r, k, k, k
]

raspimon_fine = [
  k, k, k, k, k, k, k, k,
  k, w, w, w, w, w, w, k,
  k, w, k, k, k, k, w, k,
  k, w, r, k, r, k, w, k,
  k, w, k, k, k, k, w, k,
  k, w, w, w, w, w, w, k,
  k, k, w, k, w, k, k, k,
  k, k, w, k, w, k, k, k
]

raspimon_cold = [
  k, k, k, k, k, k, k, k,
  k, c, c, c, c, c, c, k,
  k, c, k, k, k, k, c, k,
  k, c, r, k, r, k, c, k,
  k, c, k, k, k, k, c, k,
  k, c, c, c, c, c, c, k,
  k, k, c, k, c, k, k, k,
  k, k, c, k, c, k, k, k
]

#Create loops
#make a while True loop    
    #add conditional statements to test
while True:
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    if temperature > 70:
        sense.set_pixels(raspimon_hot)   
    elif temperature >= 50:
        sense.set_pixels(raspimon_cold)
    else:
        sense.set_pixels(raspimon_fine)

