# Development Environment

The IDE is the program in which you will write your code. An IDE is an all-in-one program that lets you write and run code, often with many other features included. For working with microcontrollers, an IDE should have a serial console. You don't technically need an IDE - you can write your code in any text editor (like Notepad on Windows) and run your code separately, but an IDE is a lot more convenient.

For work in this class, we'll be using the [CircuitPython Online IDE](https://urfdvw.github.io/CircuitPython-online-IDE/) because it works on Chromebooks.

## Entering the REPL

For this, you'll be working in the serial console.

As soon as the board starts up, it will run the `code.py` or `main.py` file saved on it (if present). After the code is finished running, you'll see the following in the serial console:

```
*******************************************
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
```

!!! question "Help, I don't see that!"
    Remember how I said that the board will immediately start running the code that's saved on it? The lines above will only show after the code is done running, but sometimes you'll have code on your board that has an infinite loop. If that happens, the code will never stop running so it'll never get to that point. You can spot this happening if your code is constantly showing you some output (either printing or doing something on the board itself), or even if the board is connected but you don't see anything - sometimes the code will be doing things you can't see!

    If this happens to you, force stop the board and you should get the lines above so you can continue on with these directions

At this point, you can click in the Command Window and press ++enter++ to open up the REPL.

```


Adafruit CircuitPython 7.1.1 on 2022-01-14; Adafruit ItsyBitsy M0 Express with samd21g18
>>> 
```

If you've successfully entered the REPL, you'll see something similar to the lines above appear in the serial console right above the command window. You may see a different version of CircuitPython or a different board listed, but that's okay, it depends on what you're using.

The `>>>` line is the command prompt. It shows you that the board is waiting for you to give it an input. You can do that in the command window.

Congratulations, you're now in the REPL

## Editing Code Files

With your board connected to the Online IDE, click the `Open` button and select your file.

Now you can edit the file in the Editor window. Each time you click `Save and Run`, your code will be saved and the board will restart and run the code.

Don't forget to use `Save As` before class ends to save a copy to your computer!

## CircuitPython Online IDE Interface

![screenshot of the online IDE](img/online-ide-annotated.png)

`1 - Connect`
:   This button will let you connect the board to the IDE so you can interact with it from your computer. When connected, it will show `connected` instead of `connect`, but watch out - if the board gets disconnected accidentally, the online IDE doesn't know so it'll still say `connected` and you'll need to reload the page

`2 - Open`
:   This button will let you open files from your board. If you don't see your files, make sure you're looking in the right folder!

`3 - Save and Run`
:   This button will save your code and reboot the board so the code runs

`4 - Save As`
:   This will let you save a copy of the file you're currently editing. Don't forget to save your work to your computer. There's no guarantee it will still be on the board when you get it back!

`5 - Editor Window`
:   This is the window where you'll edit your code

`6 - Serial Console`
:   This window contains the serial console so you can interact with the board

`7 - Command Window`
:   This is where you'll type inputs for the serial console

`8 - Force Stop`
:   This button will use the serial console's ++ctrl++ + ++c++ shortcut to force stop whatever's running. You can also do this from the keyboard, but watch out for the change to the shortcut. In the online IDE, you'll need to use ++ctrl++ + ++shift++ + ++c++ and may still run into issues because it may bring up the browser's developer tools

`9 - Reboot`
:   This button will use the serial console's ++ctrl++ + ++d++ shortcut to reboot the board. You can also do this from the keyboard, but watch out for the change to the shortcut. In the online IDE, you'll need to use ++ctrl++ + ++shift++ + ++d++ or you'll end up bookmarking the website instead

--8<-- "includes/glossary.md"