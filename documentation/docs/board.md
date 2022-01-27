# Troubleshooting

## Reinstalling/Updating CircuitPython

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