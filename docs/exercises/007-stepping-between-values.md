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


### Why?

Will be filled in soon

## Try It

Will be filled in soon

## Show me your code in action

Today, I'm just checking for completion and for the ability to fade between colors

--8<-- "includes/glossary.md"