# Exercise 4 - Blink Pattern

## Goals
- Work with the digitalio library
- Utilize digital outputs to control an LED
- Utilize loops to accomplish repetitive tasks

## Preparation
- Connect your board to the computer and open the `code.py` or `main.py` file. Whichever one you have is fine but I'll be referring to it as `code.py`. Delete any pre-existing code from the board. See [getting started](../getting-started.md) for help with this step.
- We'll be running code from a python file today

## Concepts & Vocabulary
- for loop
- while loop
- setup
- `range()`

## New Programming Syntax

```python
# range(max)
range(5)
# outputs a range of numbers => 0, 1, 2, 3, 4

# range(min, max)
range(-3, 3)
# outputs a range of numbers => -3, -2, -1, 0, 1, 2

# range(min, max, step)
range(-200, 100, 50)
# outputs (returns) a range of numbers => -200, -150, -100, -50, 0, 50
```
The range function is used to generate a series of numbers, and is often combined with a for loop

```python
# for loops will repeat a set number of times, or for a set of objects
for n in range(5):
    # inside the loop, we have a variable called n
    # n is going to be assigned 0 at first, then 1 on the next loop, and so on until 4
    # after n = 4, the loop will not continue running, because we've reached the end of the range
    print(n)
```
The for loop above will print the following in the serial console:

```
0
1
2
3
4
```


## Background Info

For this one, we're going to create a blinking pattern. Using the for loop we covered in class, create a pattern of blinking lights that changes over time. For instance, you might have it turn on for 1 second, then 2 seconds, then 3 seconds, and so on.

## Try It

All of the code you need for this comes from exercise 3 and from the for loops above. We'll go over it in class too.

## Show me your code in action

Total of 5 points

- 5 points: You created a for loop to blink in a pattern utilizing the variable that controls the loop
- 4 points: You created a for loop to blink your LED, but didn't utilize the variable
- 3 points: You set up your LED but didn't blink it
- 0 points: You didn't get a meaningful amount of this code completed

--8<-- "includes/glossary.md"