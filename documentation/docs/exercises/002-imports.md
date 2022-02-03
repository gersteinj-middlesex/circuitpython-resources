# Exercise 2 - Importing Modules

## Goals
- Open, edit, save, and run code
- Import modules to bring in additional functionality

## Preparation
- Connect your board to the computer and open the `code.py` file. Delete any pre-existing code from the board. See [getting started](../getting-started.md) for help with this step.

## Concepts & Vocabulary
- import
- module
- `dir()`

## Background Info

Building on your printing exercise, let's take a look at the board the way the computer sees it.

To complete this exercise, you're going to **import** the `board` module and print out the contents of the board. The `board` module is one we'll use a lot, because it saves us a lot of work. Not all boards are set up the same way - a built in LED might be on pin 12 on one board, pin 13 on another, and pin 4 on a third board. Instead of modifying the code everytime you use a different style of board, you can use `board.LED` to refer to that pin *no matter what microcontroller pin it's actually on*.

The `dir()` function (which stands for *directory*) will **return** (not print) a list all the contents of a folder or any other object in Python. Because it returns the list as a value, it can be used as an argument for another function, like the print function.

## Try It

Look at the list that is printed out. Can you tell what any of these terms mean?

**code**
```python
import board

print(dir(board))
```

**output**
```
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20', 'GP21', 'GP22', 'GP23', 'GP24', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28', 'GP28_A2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'LED', 'SMPS_MODE', 'VBUS_SENSE', 'VOLTAGE_MONITOR', 'board_id']

Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.
```

## Show me your code in action

To get credit for this exercise, I will need to see your code running. This will be scored for completion. If I am not available to check your work when you're ready, make sure you use `Save As` to save a copy on your computer (not only on the board!) so you can continue on and show me the code running later.

--8<-- "includes/glossary.md"