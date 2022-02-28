# Exercise 8 - Digital Inputs

## Goals
- Enhance understanding of the digtialio library
- Create and use digital inputs
- Work with additional electronic components

## Preparation
- We're going to start out with the circuit simulator where wiring will be easier, and then we'll go back to physical circuits
- Go to [Wokwi](https://wokwi.com/) and create a new CircuitPython project by clicking the <button style="color:white;background-color:purple;padding:.5em;border-radius:.5em;">+ More Options</button> button, then choosing `CircuitPython on Raspberry Pi Pico`
- Find the <button style="color:white;background-color:purple;padding:.5em;border-radius:50%"> + </button> button and add a pushbutton to your circuit. It should like something like the circuit below

![pi pico and pushbutton](/img/circuitsim-screenshots/button-screenshot-2.png)

## Concepts & Vocabulary
- Digital Input
- Object
- Class
- Pull up resistor
- Input Signal

## Wiring

### Explanation of the switch

The pushbutton switch has four legs, but that's a little misleading. There's really only a pair of wires, with a gap between them. If you look at the way the legs look like they follow through the board, you can see which ones are actually connected.

One of the nice things about using the simulator is that you can hover over the pins to get a hint of what they are. The wires on the pushbutton are labeled as `btn1:1.l` & `btn1:1.r` (these are connected) and `btn1:2.l` & `btn1:2.r` (these are connected). When the button is pushed down, a metal plate connects the two wires to close the circuit. You can also use `diagram.json` to change the name of the switch to something other than `btn1` if you want (see the image below) 

![button connected to pi pico](/img/circuitsim-screenshots/button-screenshot-3.png)

### Connecting to the board

You can create wires by clicking on one component, then clicking on the second component to make the connection. Connect one leg of the button to `GND 8` on the board, and connect one of the legs not connected to that leg to `GP28` on the board.

If you're feeling adventurous, you can also add an LED and connect the anode (says `A` when hovered over) to an I/O pin (I used GP0), and connect the cathode to a ground pin.

![button connected to pi pico](/img/circuitsim-screenshots/button-screenshot-4.png)

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

## Code snippets from the presentation

```python
############ assume setup already happened #############(1)
######## and you have a digitalio called button ########

# when button is not pushed, button.value is True
if button.value == True: #(2)
  print("The button is not pushed")
else: #(3)
  print("The button is pushed")
```

1.  This is not the full code! There is setup that would have to happen above this. You'd also probably want the if/else section running inside of a loop
2.  This line will check if the value of `button.value` is True. If it is, the line(s) indented below it will run
3.  If the if statement runs, this is skipped. If it doesn't run, then the line(s) intended below it will run

## Try It

Based on what we covered in class, demonstrate that you can use a button to control an LED

## Show me your code in action

- 5 points: You successfully control an LED with a button. This should be based on programming, not directly hooking the LED up to the button
- 4 points: You can successfully read values from a button
- Anything less than reading values from a button will not be considered successful completion of this exercise

--8<-- "includes/glossary.md"