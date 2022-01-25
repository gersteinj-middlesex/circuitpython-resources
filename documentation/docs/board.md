# Development Board

The microcontrollers we're using for this class run [CircuitPython](https://circuitpython.org/). This is a small version of Python that works on lower-powered hardware.

## Basic Setup

1. Connect the board to a computer using a USB cable (see warning above)
2. Make sure the board shows up in your computer's filesystem. It should show up as a removable drive (like plugging in a flash drive) and will generally be called `CIRCUITPY`
3. Open your development environment. For the Chromebooks, we're using [URFDVW's CircuitPython Online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/). If you want to keep working with this outside of class and you have a computer with a full operating system, there are lots of other options you can use
4. Make a software connection between the board and computer if needed. You must do this to use the [online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/). To make the connection, click the `connect` button and select your board
5. At this point, you should be able to enter the REPL or open/edit/save files on the board's internal storage

!!! Tip "USB cable warning"
    Some USB cables can only be used for charging! These cables don't have the necessary wires to send data back and forth, but they don't look any different from a USB cable that does. If the computer doesn't recognize the board, sometimes this is the reason. I will always give you USB cables that can transmit data, but if you're using your own you may run into this problem

!!! Warning "Connected isn't always connected"
    If you disconnect your board (or put it into boot mode), it will disconnect from the online IDE, but the button in the IDE will still show `connected` because it doesn't check on its own. If you run into this problem, refresh the page and redo step 4

## Troubleshooting

### Reinstalling/Updating CircuitPython

!!! Warning 
    This is **not** something you'll need to do every time you work with the board. In class, you should only do this if told to do so. Everything on the board will be erased, so make sure you've saved everything you want to keep!

Sometimes we need to update or reinstall CircuitPython. This is a lot like doing a factory reset on your phone when things aren't working right.

1. Download the correct version of [CircuitPython](https://circuitpython.org/downloads). Make sure you choose the correct board. The name of the board is written on the board itself.
2. Plug your board into the computer with a USB cable you know works. It should show up in the filesystem as `CIRCUITPY` or another similar name.
3. Double click the `reset` button. The `CIRCUITPY` drive will go away and be replaced by a drive called `ITSYBOOT`, `CPLAYBOOT`, or something similar. Different boards will show up with different names, but the important thing is it will *always* include the word `BOOT`. This puts your board into boot mode so you can install CircuitPython. It's a lot like putting your phone into rescue mode to do a factory reset, and like rescue mode, is something you won't do most of the time. Boards that have an RGB indicator light and a regular built in LED will have the built in LED light up red and the RGB indicator light up in bright green.
4. Drag the .uf2 file you downloaded in step one into the `ITSYBOOT` (or whatever it's called) drive.
5. The boot drive will go away as the board restarts. It will return as `CIRCUITPY`.
6. Your board is ready to use.

--8<-- "includes/glossary.md"