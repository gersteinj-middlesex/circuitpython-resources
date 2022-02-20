---
layout: base.njk
title: Setup Checklist
---

Created by request of a student who had trouble remembering the process.

## Connecting the Board

- Get a board & connect it to your computer with a USB cable.
- Go to the [online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/). If it's already open from another day, make sure you refresh your browser tab.
- Click the <button>connect</button> button and choose your board.
- If the board has connected properly, you should see the serial console update with something like what's below. If you see that, you can move on to the next section of the checklist. There might be additional output from whatever code is on the board. If nothing changes, check the [troubleshooting steps !NEED LINK!](#) for help!

```pycon
*******************************************
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
```

## Working with Python Files

- To edit a python file, click the <button>open</button> button and make sure you open the `main.py` or `code.py` file that's on the drive called `CIRCUITPY`.
- Be *really* certain you've opened the file that's on the `CIRCUITPY` drive, because the IDE can open a file that's saved to your computer, but the board can't run it! If you're not sure how to see where a file is saved, please ask for help.
- To make sure your code is working, each exercise starts with a test file. Please make sure you run the test code *at the start of each class*. I often find that when students struggle to get their code to work, it's because of a problem that they could have caught quickly with the test code.

## Connecting to the REPL

- f you need to connect to the REPL to use Python interactively, assumingi you can see the same thing as in the code block I showed earlier, you can click in the white text box at the bottom of the serial console and press <kbd>enter</kbd>. Ifyou don't see the same message I showed above, please go to the [troubleshooting steps !NEED LINK!](#) for help!