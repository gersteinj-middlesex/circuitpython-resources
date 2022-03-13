---
title: Getting Started
layout: base.njk
eleventyNavigation:
    key: Getting Started
    order: 1
---

Having trouble remembering how to get started? Follow these steps to hook up your board

- Get a board & connect it to your computer with USB cable
- Navigate to the [online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/). If it's already open from another day, refresh your browser tab to ensure it can connect to the board
- Click the `connect` button and choose your board
- Check to see if the following pops up in the serial console:

```shell
*******************************************
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
*******************************************
```

## I don't see the message

That's okay! If you don't see it, one of two things is almost certainly happening.

1. The board is still running code
2. You didn't actually connect

The first is the easiest to check for, so we'll check that now. If the board is still running code, you will probably either see text being printed to the console over and over *or* you'll see absolutely nothing. We went over why that is in class. We'll check now:

- Go into the serial console and use <kbd>ctrl</kbd> + <kbd>c</kbd> to force stop the code. Remember that if you're using the online IDE, you should use the matching button on the screen instead.
- Hopefully, you'll get a message about a keyboard interrupt, followed by the message we were looking for before. If so, great! You can move on to the next section

- [ ] To edit a python file, remember to click the `open` button, and make sure you open the `main.py` (or `code.py`) file that's on the drive called `CIRCUITPY`. If the file is on your computer, the IDE will open it just like a file on the board, but it won't run on the board. So please be careful about what file you're opening!
- [ ] To make sure everything is working, each exercise starts with a test file. Please make sure you run the test code *even if the board appears to be doing the same thing*. I often find that when students struggle to get their code to work, it's because the code they're editing isn't the code on the board.
- [ ] If you need to connect to the REPL, assuming you see the same thing as in the code block below, you can click in the serial console and press ++enter++. If you don't see that, scroll down to the "Interactive Programming with the REPL" section


## Detailed Board Setup

### What You Need
- A development board. For right now, we're using the Adafruit ItsyBity M0 Express, but there are lots of options
- A suitable USB cable. All the boards we have at the school use a micro-USB cable. If you're using your own cable, make sure that it can be used for data - some USB cables are only for power!
- A computer to work with. A Chromebook is fine

### Connecting the Board to the Computer
1. Connect the board to a computer using a USB cable
2. Make sure the board shows up in your computer's file system. It should show up as a removable drive (like plugging in a flash drive) and will usually be called `CIRCUITPY`
3. Open your development environment. For the Chromebooks, we're using [URFDVW's CircuitPython Online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/). If you want to keep working with this outside of class and you have a computer with a full operating system, there are lots of other options you can use
4. Make a software connection between the board and computer. The [online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/) won't work if you do this. To make the connection, click the `connect` button and select your board
5. At this point, you should be able to enter the REPL or open/edit/save files on the board's internal storage

!!! Warning "About USB cables"
    Some USB cables can only be used for charging! These cables don't have the necessary wires to send data back and forth, but they don't look any different from a USB cable that does. If the computer doesn't recognize the board, sometimes this is the reason. I will always give you USB cables that can transmit data, but if you're using your own you may run into this problem

!!! Warning "Connected isn't always connected"
    If you disconnect your board (or put it into boot mode), it will disconnect from the online IDE, but the button in the IDE will still show `connected` because it doesn't check on its own. If you run into this problem, refresh the page and redo step 4

## Interactive Programming with the REPL

For this, you'll be working in the serial console. It's the right side of the [online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/)

As soon as the board starts up, it will run the `code.py` or `main.py` file saved on it (if present). After the code is finished running, you *should* see an output similar to what's below. If you don't, take a look at the box below that for more information about what's happening!



!!! question "Help, I don't see that!"
    Remember how I said that the board will immediately start running the code that's saved on it? The serial console will only be ready for you to load the REPL after the code finishes running, but sometimes you'll have code on your board that has an infinite loop. If that happens, the code will never stop running so it'll never get to that point. You can spot this happening if your code is constantly showing you some output (either printing or doing something on the board itself), or even if the board is connected but you don't see anything - sometimes the code will be doing things you can't see!
<!-- 
    If this happens to you, force stop the board and you should get the lines above so you can continue on with these directions -->

At this point, you can click in the Command Window and press ++enter++ to open up the REPL. If you're successful, you'll see something similar to the lines below. Your version of CircuitPython and your board may be different from mine, but the `>>>` is called the command prompt, and it shows that you are in (Circuit)Python and the board is waiting for you to give an input. 


<!-- ```pycon
Adafruit CircuitPython 7.1.1 on 2022-01-14; Adafruit ItsyBitsy M0 Express with samd21g18
>>> 
``` -->

To make sure everything's working, do that now! I like to type a math expression like ```5 * 3``` into the command window and press ++enter++, which should output ```15```

## Opening, Editing, Saving, and Running .py Files

With your board connected to the Online IDE, click the `Open` button and select your file.

Now you can edit the file in the Editor window. Each time you click `Save and Run`, your code will be saved and the board will restart and run the code.

Don't forget to use `Save As` before class ends to save a copy to your computer!

--8<-- "includes/glossary.md"