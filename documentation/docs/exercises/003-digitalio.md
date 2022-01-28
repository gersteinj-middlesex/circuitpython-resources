# Exercise 3 - DigitalIO

## Goals
- Import modules to bring in additional functionality
- Work with the digitalio library
- Utilize digital outputs to control an LED

## Preparation
- Connect your board to the computer and open the `code.py` or `main.py` file. Whichever one you have is fine but I'll be referring to it as `code.py`. Delete any pre-existing code from the board. See [getting started](../getting-started.md) for help with this step.
- We'll be running code from a python file today

## Concepts & Vocabulary
- `board` (module)
- `time` (module)
- `digitalio` (module)
- input
- output
- dot notation

## Background Info

Okay, we're finally going to make something happen that you can see in the real world!

We have several different boards in use right now, but all of them have a bulit in LED - that's an LED that's soldered directly onto the board and already connected correctly to the microcontroller. These are great for troubleshooting, because there's no chance of you wiring things up wrong.

We'll do this in a few stages.

## Try It

### Part 1 - Imports

Save and run this version of the code. There's an explanation below!

```python
# Import necessary libaries
import board
import digitalio
import time
```

**What you should see:**
The board should reboot, run the code, and print out a message that it's done running. Make sure you don't get any errors, though! The reason we're running this code a little at a time is because I want you to go through the process in the right way - if you write the code all at once, it's harder to spot errors and harder to formulate what to do.

**What this does:**
This imports modules for working with the board, working with digital inputs and outputs, and working with time into the code.

### Part 2 - Creating a Digital Output

Save and run this version of the code. Only the code below the line of asterisks `******` is new. There's an explanation below!

```python
# Import necessary libaries
import board
import digitalio
import time

# ************************************** #

# create a new DigitalIO object connected to whatever pin the board's built in LED is attached to.
# Assign this to a variable so we can refer to it again
led = digitalio.DigitalInOut(board.LED)
# Set our new DigitalIO object to be an output
led.direction = digitalio.Direction.OUTPUT
# Print the value of the LED
print(led.value)

```

**What you should see:**
The board should reboot, run the code, and print out a message that it's done running. In the serial console, you should see it print either `True` or `False`. Make sure you don't have any errors. Nothing will light up yet.

**What this does:**
The comments explain this too, but here you go:
- The first new line of code creates a DigitalIO object. We have to tell it what pin we're using, but instead of giving it a pin number (which we could do, but will vary between boards), we tell it to go look up the definition in the `board` module and use whatever pin the built in LED is attached to
- The second new line of code sets this DigitalIO object to be an OUTPUT so it can send signals
- The third new line of code will print out the value assigned to the LED. True will turn it on, False will turn it off


### Part 3 - Turning on the LED

Save and run this version of the code. Only the code below the line of asterisks `******` is new. There's an explanation below!

```python
# Import necessary libaries
import board
import digitalio
import time

# create a new DigitalIO object connected to whatever pin the board's built in LED is attached to.
# Assign this to a variable so we can refer to it again
led = digitalio.DigitalInOut(board.LED)
# Set our new DigitalIO object to be an output
led.direction = digitalio.Direction.OUTPUT
# Print the value of the LED
print(led.value)

# ************************************** #
# Set the LED's value to True to turn it on
led.value = True
# Print the value of the LED
print(led.value)

```

**What you should see:**
In the serial console, you should see it print either `True` or `False`, and then on the next line, it should print `True`, which is the value we assigned to led.value. Make sure you don't have any errors. You won't see anything lighting up, though!

**What this does:**
We set the LED's value to True to turn it on

!!! Question
    Why do you think you didn't see the LED turn on?

### Part 4 - Delay!

Save and run this version of the code. Only the code below the line of asterisks `******` is new. There's an explanation below!

```python
# Import necessary libaries
import board
import digitalio
import time

# create a new DigitalIO object connected to whatever pin the board's built in LED is attached to.
# Assign this to a variable so we can refer to it again
led = digitalio.DigitalInOut(board.LED)
# Set our new DigitalIO object to be an output
led.direction = digitalio.Direction.OUTPUT
# Print the value of the LED
print(led.value)

# Set the LED's value to True to turn it on
led.value = True
# Print the value of the LED
print(led.value)

# ************************************** #
time.sleep(5)
```

**What you should see:**
In the serial console, you should see it print either `True` or `False`, and then on the next line, it should print `True`, which is the value we assigned to led.value. Make sure you don't have any errors. You should also see the LED light up for 5 seconds!

**What this does:**
We told the board to pause for 5 seconds after turning the LED on

!!! Question
    How could you turn the LED off and on again?



## Show me your code in action

Total of 5 points

- 5 points: You made your LED blink repeatedly
- 4.5 points: You made your LED change at least twice
- 4 points: Your LED turns on
- 3 points: You set up your LED but it doesn't turn on
- 0 points: You didn't get a meaningful amount of htis code completed