# Review

## Goals
- Practice identifying and correcting common code problems

## Directions
For each example, tell me what the problems are and how to correct them. This can be done in one of a few ways:

1. Create corrected versions of the code, with brief notes on what the differences are
2. Give me a document that describes changes needed and what lines need to be changed
3. Take screenshots and use editing tools to mark up the screenshots

Submit in the "Review 2" assignment in classroom. I'll also go over these with you

## Code Samples

### Example 1
[Link to sample circuit](https://wokwi.com/projects/327560256355828306) in case you want to run the code

```python
n = 0

while n < 10:
  print(n)
```

**Additional info**

- no electronics involved, this is pure Python
- desired behavior: count from 0 to 9, printing out each number, then stop
- current behavior: code runs successfully, but prints 0 forever

### Example 2

[Link to sample circuit](https://wokwi.com/projects/327559462071042642) in case you want to run the code as you figure out the problems

```python
import board, time
import digitalio

led = digitalio(board.LED)

while True:
  led.value = True
  time.sleep(1)
  led.value = False
```

**Additional info**

- no wiring problems
- multiple coding problems
- desired behavior: LED blinks on for 1 second and off for half a second forever
- current behavior: Error messags, code fails to run
- behavior *if* you resolve the error messages without making other changes: LED turns on, but will not turn off

### Example 3

[Link to sample circuit](https://wokwi.com/projects/325661032496235091) in case you want to run the code

```python
import board, time
from analogio import AnalogIn
from pwmio import PWMOut

sensor = AnalogIn(board.GP28)
led = pwmio(board.GP0)
input_value = 0

# turn on at full brightness for a second
led.duty_cycle = 65535
sleep(1)
# turn on at about half brightness for a second
led.duty_cycle = 32000
sleep(1)
#turn off for a second
led.duty_cycle = 0
sleep(1)

while True:
  print(sensor.value)
  led.duty_cycle = input_value
```

**Additional Info**

- there are a few different ways to fix this
- wiring is correct
- correct pins (board.GP28 and board.GP0) are named in the code
- desired behavior: LED turns on for a second, goes to half brightness for a second, then turns off for a second. After that's done, it will match the potentiometer's value forever
- current behavior: errors prevent the code from running
- behavior if you fix the errors without making other changes: The first three things (on, half brightness, off) will work, but after that the LED will stay off