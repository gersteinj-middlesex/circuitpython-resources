# Getting Started

## Every Time You Use The Board

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

```
*******************************************
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
```

!!! question "Help, I don't see that!"
    Remember how I said that the board will immediately start running the code that's saved on it? The serial console will only be ready for you to load the REPL after the code finishes running, but sometimes you'll have code on your board that has an infinite loop. If that happens, the code will never stop running so it'll never get to that point. You can spot this happening if your code is constantly showing you some output (either printing or doing something on the board itself), or even if the board is connected but you don't see anything - sometimes the code will be doing things you can't see!

    If this happens to you, force stop the board and you should get the lines above so you can continue on with these directions

At this point, you can click in the Command Window and press ++enter++ to open up the REPL. If you're successful, you'll see something similar to the lines below. Your version of CircuitPython and your board may be different from mine, but the `>>>` is called the command prompt, and it shows that you are in (Circuit)Python and the board is waiting for you to give an input. 


```


Adafruit CircuitPython 7.1.1 on 2022-01-14; Adafruit ItsyBitsy M0 Express with samd21g18
>>> 
```

To make sure everything's working, do that now! I like to type a math expression like ```5 * 3``` into the command window and press ++enter++, which should output ```15```

## Opening, Editing, Saving, and Running .py Files

With your board connected to the Online IDE, click the `Open` button and select your file.

Now you can edit the file in the Editor window. Each time you click `Save and Run`, your code will be saved and the board will restart and run the code.

Don't forget to use `Save As` before class ends to save a copy to your computer!