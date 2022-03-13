# Exercise 7 - Stepping Between Values

## Goals
- Work with the dotstar or neopixel library
- Work with more complex data types
- Create variables/constants to make code more managable
- Work with RGB color
- Iterate through loops to change gradually from a start point to an end point

## Preparation
- Connect your board to the computer and open the `main.py` file. Please make sure you're opening the one on your board, not a copy saved on your computer! See [getting started](../getting-started.md) for help with this step. 
- We'll be running code from a python file today
- Please start off by configuring and running the test code below to check that you have red-green-blue flashing lights

## Concepts & Vocabulary
- Loops
- Iteration
- Interpolation

## Test Code

Please configure and run the test code to make sure everything is working correctly. I promise this isn't to make more work for you! We've had a lot of people run into problems like modules getting deleted by accident or editing a file on their computer instead of the one on the board, so this is a quick diagnostic exercise I'll ask you to run at the start of each class. I've also added a print function below - the purpose of this is for you to change the string inside it to something recognizable (like your name). If you don't see this line print, then this isn't the code that's running on your board!

Don't forget that the [getting started](../getting-started.md) page has a checklist you can use to help you get your board set up correctly.

```python title="Testing Code"
"""Adapted from CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

# For Trinket M0, Gemma M0, ItsyBitsy M0 Express, and ItsyBitsy M4 Express # (1)
# import adafruit_dotstar
# led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
# For Feather M0 Express, Metro M0 Express, Metro M4 Express, Circuit Playground Express, QT Py M0
# import neopixel
# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3 #(2)

#### Everything above this line is setup code that won't change when you do the assignment below ####
print("CHANGE THIS TO YOUR NAME OR SOMETHING ELSE SPECIFIC TO YOU") # (3)

while True: 
    led[0] = (255, 0, 0) 
    time.sleep(0.5)
    led[0] = (0, 255, 0)
    time.sleep(0.5)
    led[0] = (0, 0, 255)
    time.sleep(0.5)

```

1.  You're going to need to comment out one of the two pairs of lines here, depending on which board you have
2.  You can set this to any value from 0 to 1. Try other values!
3.  Please make sure you change what this is printing! This line is a diagnostic line to make sure that the code running on your board is the code you think it is

## Stepping Between Values

Often, you'll need your code to be able to go smoothly from one value to another. A few examples:
- When you're in a car, you accelerate from stopped to going full speed, and brake gradually when you come to a stop
- With LEDs, you might want to blend smoothly from one color to another
- If you had a robotic arm, you'd want to be able to have positions between fully closed and fully opened.

## Code Snippets from the Presentation

```python
start = 500 #(1)
end = 800

n = start
while n < end: #(2)
  print(n)
  n += 1
```

1.  You could change these start and end values to be whatever you wanted
2.  How could you change this so you include the end value?

```python
start = 500 #(1)
end = 800

for n in range(start, end):
  print(n)
```

1.  You could change these start and end values to be whatever you wanted

```python
############ Assume all necessary setup for the internal RGB LED has been done above this line #############
####### led refers to an object set up using the appropriate library to control the built in RGB LED ####### 

blue = (0, 0, 255)
magenta = (255, 0, 255)
red = (255, 0, 0)

# fade from blue to magenta
for n in range(0, 256, 1):
  led[0] = (n, 0, 255)
  time.sleep(.05)

# fade from magenta to red
# (255, 0, 255) => (255, 0, 0)
for n in range(255, -1, -1):
  led[0] = (255, 0, n)
  time.sleep(.1)
```

## Try It

Based on what we covered in the slides, demonstrate the ability to fade between colors. 

## Show me your code in action

- 5 points: Your RGB LED fades smoothly from `red => green => blue => red` or a pattern of similar difficulty
- 4.5 points: Your RGB LED fades smoothly between at least two different sets of colors
- 4 points: Your RGB LED is able to fade smoothly at least once
- 3 points: You can change colors in multiple steps, but it is not coded in a way that makes sense

--8<-- "includes/glossary.md"