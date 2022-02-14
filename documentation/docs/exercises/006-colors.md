# Exercise 6 - Working With Colors

## Goals
- Work with the dotstar or neopixel library
- Work with more complex data types
- Create variables/constants to make code more managable
- Work with RGB Color

## Preparation
- Connect your board to the computer and open the `main.py` file. Please make sure you're opening the one on your board, not a copy saved on your computer! See [getting started](../getting-started.md) for help with this step. 
- We'll be running code from a python file today
- Please start off by configuring and running the test code below to check that you have red-green-blue flashing lights

## Concepts & Vocabulary
- tuple
- RGB color
- constants

## Test Code

```python
"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

# For Trinket M0, Gemma M0, ItsyBitsy M0 Express, and ItsyBitsy M4 Express # (1)
# import adafruit_dotstar
# led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
# For Feather M0 Express, Metro M0 Express, Metro M4 Express, Circuit Playground Express, QT Py M0
# import neopixel
# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3 #(2)

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

## Defining Colors

For today's exercise, you're going to need to make a pattern of *at least* 5 colors. That's going to start getting hard to read, though, so let's look at how we can improve this a bit.

You already know about variables. For instance, `a = 5` is an assignment statement that assigns the value `5` to the variable `a`. After that, you can use a to represent the value assigned to it. You can also modify the value assigned to a. For instance:

```python
a = 5
b = 6
c = a + b

print("a is:", a)
print ("b is:", b)
print("c is:", c)
print(f"{a} + {b} = {c}")

a = 7

print("a is:", a)
print ("b is:", b)
print("c is:", c)
print(f"{a} + {b} = {c}")
```

When run in CircuitPython, the code above should produce:

```pycon
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
a is: 5
b is: 6
c is: 11
5 + 6 = 11
a is: 7
b is: 6
c is: 11
7 + 6 = 11

Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.
```

## Try It

Modify the code above to change the pattern of colors it shows

## Show me your code in action

Today, I'm just checking for completion. You'll have another assignment to show me more advanced usage

--8<-- "includes/glossary.md"