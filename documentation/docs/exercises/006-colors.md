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

#### Everything above this line is setup code that won't change when you do the assignment below ####

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

### How the NeoPixel and DotStar modules read colors

When working with these two modules, you will always give colors as a set of RGB values, but you *also* need to make them a single value. That's where tuples come in! A tuple is a lot like a list, in that it is a single value that has multiple values inside it. The difference is that unlike a list, it can't be changed once it's created. It looks like `(255, 0, 0)` (the spaces in between the comma and number are optional). You can also use hex values, which look like `#ff0000`. Either way, the range you'll use is 0-255 (or the hexadecimal equivalent if you're using hex values, which would be `#00` to `#ff`). You can use a [color picker](https://g.co/kgs/W1QAdB) to figure out what values you want for a color, although you may have to tweak them to get them to look right on the LED.

### Constants

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

In some languages, you can define a variable that isn't allowed to change, and this is called a *constant*. You probably know constants from math or science classes. For instance: pi or the speed of light are known values that we can refer to by a name, but they don't change. This can be useful in your code too. If you wanted to define what "red" is, you might create a constant because the value of red shouldn't be changing while the program runs.

In Python, you can't create a true constant, but the convention in Python is to make the name of a variable that is being used as a constant in ALL CAPS.

For instance, you might have a color defined like this:

```python
RED = (255,0,0)
```
### Why?

It's going to start getting hard to maintain your code if you're writing the colors in manually every time you need them, especially when we start doing some longer examples. Using variables to represent colors will make your life easier, and will also help you get ready to work with lists of colors and fading between colors

## Try It

Modify the sample code below so it works. You'll need to define variables/constants for colors. You may change the patern of colors it shows. Don't forget to uncomment the right section of code for your particular board! If you want to change the pattern it's showing, that's fine

```python
import time
import board

# For Trinket M0, Gemma M0, ItsyBitsy M0 Express, and ItsyBitsy M4 Express # (1)
# import adafruit_dotstar
# led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
# For Feather M0 Express, Metro M0 Express, Metro M4 Express, Circuit Playground Express, QT Py M0
# import neopixel
# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3 #(2)

#### Everything above this line is setup code that works exactly the same as the test code ####
#### You can just copy and paste the code below this line to replace the loop in the test code ####

# Define your colors #(3)
# Don't forget to define variables for the colors! This would be a good place to do that.



# Have you defined your colors yet?

while True: 
    led[0] = RED 
    time.sleep(0.5)
    led[0] = ORANGE
    time.sleep(0.5)
    led[0] = YELLOW
    time.sleep(0.5)
    led[0] = GREEN
    time.sleep(0.5)
    led[0] = BLUE
    time.sleep(0.5)
    led[0] = PURPLE
    time.sleep(0.5)
    led[0] = PINK
    time.sleep(0.5)

```

1.  You're going to need to comment out one of the two pairs of lines here, depending on which board you have
2.  You can set this to any value from 0 to 1. Try other values!
3.  Remember you can define them just like any other variable. See above for an example

## Show me your code in action

Today, I'm just checking for completion. You'll have another assignment to show me more advanced usage

--8<-- "includes/glossary.md"