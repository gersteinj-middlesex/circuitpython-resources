# Exercise 8 - Digital Inputs

## Goals
- Enhance understanding of the digtialio library
- Create and use digital inputs
- Work with additional electronic components

## Preparation
- Go to [Wokwi](https://wokwi.com/) and create a new CircuitPython project by clicking the <button style="color:white;background-color:purple;padding:.5em;border-radius:.5em;">+ More Options</button> button, then choosing `CircuitPython on Raspberry Pi Pico`

## Concepts & Vocabulary
- Digital Input
- Object
- Class
- Pull up resistor
- Input Signal

## Demo Code

This assumes you have a button hooked up to Ground and GP28. Please note that the name of the pin is different from what you would use on the physical boards

```python title="Demo Code"
import board, time

# We're only imporing a subset of the digitalio module
# This means we don't have access to the rest of it
# The good thing is that we can use these three objects from digitalio without putting 'digitalio' before them
from digitalio import DigitalInOut, Direction, Pull

# Create a digitalio object like we did with LED
# This one is called button because... it's a button
button = DigitalInOut(board.GP28)

# Before we used Direction.OUTPUT so we could send a signal
# Now we're using Direction.INPUT so we can read a signal coming in
button.direction = Direction.INPUT

# This creates a voltage difference when the other leg is connected to ground
button.pull = Pull.UP

# Can you set up the LED to be able to control it?
# You don't need to import anything new
# The legs of the LED are already hooked up to pin 0 (board.GP0) and ground

while True:
  # because the button is an input, we can't assign it a value like we did for the LED
  # we can read the value it's getting from the outside world though
  print(button.value)

  # can you use button.value to control an LED?
```

1.  You're going to need to comment out one of the two pairs of lines here, depending on which board you have
2.  You can set this to any value from 0 to 1. Try other values!
3.  Please make sure you change what this is printing! This line is a diagnostic line to make sure that the code running on your board is the code you think it is

## Code Snippets from the presentation

## Try It

Based on what we covered in class, demonstrate that you can use a button to control an LED

## Show me your code in action

- 5 points: You successfully control an LED with a button. This should be based on programming, not directly hooking the LED up to the button
- 4 points: You can successfully read values from a button
- Anything less than reading values from a button will not be considered successful completion of this exercise

--8<-- "includes/glossary.md"