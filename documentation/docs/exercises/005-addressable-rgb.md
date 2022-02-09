# Exercise 5 - Addressable RGB LEDs

## Goals
- Work with the dotstar or neopixel library
- Work with more complex data types
- Comment out code to control which sections of code run
- Utilize loops to accomplish repetitive tasks

## Preparation
- Connect your board to the computer and open the `main.py` file. Please make sure you're opening the one on your board, not a copy saved on your computer! See [getting started](../getting-started.md) for help with this step. 
- We'll be running code from a python file today
- To make sure you're working with the correct file, add a print function to your code (for instance, `print("It's time to play with LEDs")`) and make sure it runs
- After you've done that, please copy and paste the sample code below to your `main.py` file

## Concepts & Vocabulary
- tuple
- addressable RGB LED
- commenting out code

## Starting Code

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

while True: #(3)
    led[0] = (255, 0, 0) #(4)
    time.sleep(0.5)
    led[0] = (0, 255, 0)
    time.sleep(0.5)
    led[0] = (0, 0, 255)
    time.sleep(0.5)

```

1.  You're going to need to comment out one of the two pairs of lines here, depending on which board you have
2.  You can set this to any value from 0 to 1. Try other values!
3.  This loop will run forever. Could you change it to run 5 times? Try it!
4.  This sets the first LED in the chain to red. Could you make it orange instead?

## Try It

Modify the code above to change the pattern of colors it shows

## Show me your code in action

Today, I'm just checking for completion. You'll have another assignment to show me more advanced usage

--8<-- "includes/glossary.md"