# Python Review
This is brief a one-page review of everything you've already learned. You can think of it as a cheat sheet to refer back to when you forget how to do something. If you want further explanations, check out the [*Introduction to Python* page](http://www.eecs.ucf.edu/JuniorKnights/material/), or [Rachael's slides](https://github.com/rsera/Junior-Knights).

## Input/Output
###     Printing to the screen
To output something to the screen, we simply use the `print()` function.

```Python
print("Hello World")
```
We can also insert variables as arguments to the function.

```Py
name = "Aaron"
age = 24

print("My name is", name, "\n I am ", age, "years old.")
```

###     Getting input from the user
To get input, we use the `input()` function. `input()` takes an optional string as an argument. This string will be used as a prompt for your user.

```Py
a = input("Enter a number.")
print(a)
```

---

## Data Types
###     Numeric Types
####        Integers
Integers are positive and Negative whole numbers.

```Py
i = 0
j = -48
k =  2147483647
```
Integers can be expressed in decimal, or hexadecimal notation.
To use hexadecimal, simply preface the number with `0x`.
Hexadecimal is strange to look at at first, and if you find it 
difficult to understand, you shouldn't worry too much. We won't be using it a lot.

The basic idea is this:

0-9 represent the same numbers that they do in decimal.

    0x1 = 1, 0x2 = 2, ...

However, once we get past 9, we go to the letters A-F (these can be upper or lower case.)

    0xA = 10, 0xB = 11, ... , 0xF = 15

Once we reach F, we go to

    0x10 = 16, 0x11 = 17, ..., 0x1F = 31, ...

```Py
# What is the output of the following code?
# note: A review of if-else statements is given below.
h = 0x123abc
g = 0xF
f = 10

print(h, g, f)
print(f + g)
print(hex(f))

if f == 15:
    print(15)

elif f == 10:
    print(10)

elif f == 16:
    print(16)

else:
    print("none")
```

###     Strings
A string is a list (or array) of [ascii](https://www.w3schools.com/charsets/ref_html_ascii.asp) characters. These allow computers to represent letters, words, and sentences in a convenient way. To specify a string, we can use double or single quotes.

```Py
# What is the output of the following code?
name = "Aaron"
Aaron = 'Awesome'

print("My name is ", name)
print(name, " is Awesome!")
print(name, " is ", Aaron + "!")
```

###     Booleans
Boolean types can  only have one of two values, ```True``` or ```False```.
```Py
a = True
b = False
```

---

## Aritmetic Operations
Adding and subtracting numbers is very intuitive in Python.

```Py
# adding integers
a = 18
b = 2
c = a - b   # c == 20

# adding floats
f = 2.5
g = f + f   # g == 5

# What happens when we add/subtract a float to an int?
result = b + f
print(result)

# We can also make use of the += and -= operations
print(f += a)
print(b -= c)
```

Multiplication and division are just as easy, but there's a catch.
```Python
a = 5
b = 2

print(a * b)

# How do we want to handle division? We have two ways:
#   The first is floating point division. This is just like punching numbers into your
# calculator.

print(a / b)

# Sometimes we don't want a decimal value, so we use integer division. Integer division
# is just like performing "long division" and ignoring the remainder. We specify this by
# using two slashes "//".

print(a // b)

# 2 goes into 5 exactly 2 times, and leaves a remainder of 1.
# What if we want the remainder?
# Then we use the mod operator "%".

print(a % b)

# Exponentiation

a = 2
b = 3

# Exponentiation is the term for repeated multiplication. We say that 2 to the third power
# is equal to 2 * 2 * 2. To do this in Python, we use "**".

print(2**3)
```

---

## Conditional Logic (if-else)
The format for an if statement is 
```Py
if <boolean expression>:
    statement_1
    statement_2
    ...
    statement_n

# Otherwise, go here

elif <boolean expression>:  # These are optional and you can have as many as you like.
    statement_1
    statement_2
    ...
    statement_n

else:   #You can only have one of these. Note that there is no boolean expression.

...
...
```
If the boolean expression is a true statement, then the body of the if statement will execute. Otherwise, it will skip to the end of it.

###     Example

```Py
b = 5
a = input("Enter a number.")


if a > b:
    print("WOOHOO!")

elif a == b:
    print("YEEHAW!")

else:
    print("GUHA!")
```

Boolean expressions don't have to be just one statement. We can also use `and`, `or`, and `not` to make more complicated conditions.

```Py
a = input("Enter a number.")
b = input("Now do it again.")

if a == 5 or b == 5:
    print("Python is fun!")

elif a < 5 or a >= 5:
    print("This will always print.")

elif not(b == 4 and a > 6) and False:
    print("This will never print")
```

---

## Loops
###     while loops
While loops are a lot like if statements, but with a key difference. After the body of an if statement, the program simply goes to the next line. The general format looks like this.

```Py
while <boolean expressions>:
    statement_1
    statement_2
    ...
    statement_n
```

### for loops
for loops allow us to easily create *count controlled* loops. Count controlled means the loop runs a certain number of times.  
We can do this by taking advantage of the `range()` function. `range()` takes a number, and generates a sequence of numbers counting up to that. For example, `range(5)` represents the sequence {0, 1, 2, 3, 4}. It also takes optional parameters that allow us to further customize this sequence. The format is 

```Py
range(<start>*, <stop>, <step>*)
``` 
where * indicates an optional parameter.  

\<start\> indicates the beginning of the sequence (inclusive), \<stop\> indicates the end of a sequence (non-inclusive), and \<step\> indicates the distance between each number in the sequence. For example, `range(2, 10, 2)` represents the sequence {2, 4, 6, 8}.  
So to create a loop that runs `n` times, we simply write,  

```Py
for <variable> in range(n):
    statement_1
    statement_2
    ...
    statement_n
```

\<variable\> is a temporary variable that can be used throughout the loop. Here's an example.

```Py
# This prints every number from 10 to 20 on a separate line.
for i in range(10, 21):
    print(i)
```

---

## Functions
In math, we have functions that might look something like this.

f(x) = 2x<sup>2</sup> + 5

If you're familiar with this notation, functions in Python should also look familiar.  

```Py
def function_name(<arguments>)
    statement_1
    statement_2
    ...
    statement_n

    return <value>
```
The `def` keyword is short for *define* and signifies to the interpereter that you're about to define a function.  
<Arguments> is one or more variables that the function will use.  
The body of the function is a series of steps that the function will carry out. Finally, we see the `return` keyword followed by a return value.  
This is the final value that a funtion might put into a variable.  
Let's see an example.

```Py
def my_function(x, y)
    r = x+y
    r *= 2

    return r

x = my_function(3, 4)
print(x)

print(my_function(3, 4) + 5)
```
1. First, we define a function called `my_function`. It takes two arguments, `x` and `y`, adds them, then doubles them and returns the result.
2. Next, we  pass 3 and 4 to `my_function`.
3. Then we create a variable `x` and we put the return value of `my_function` in `x`, and print x.
4. In the last line, we can see that a function can behave just as a regular variable. We pass 3 and 4 to the function, add 5 to the result, and print it, all in one line.

---

## Lists
We'll talk more about lists today, but here's a quick rundown. You can declare a list by using square brackets with zero or more values, separated by commas.

```Py
a1 = []
a2 = [1]
a3 = [1, 2, 3]
a4 = [3, "a", True, a2, my_function(3,4)]
```

The things inside the list are called members. To access a specific member of a list, type the name of the list, followed by the index of the desired member. Remember, we start counting from 0!

Try to determine the output of this program.
```Py
a1 = []
a2 = [1]
a3 = [1, 2, 3]
a4 = [3, "a", True, a2, my_function(3,4)]

x = a2[0]
print(x)

print(a3[3])
```

## Exercises
###     **fizzbuzz**
fizzbuzz is a classic problem that every programmer should be able to solve.
- Have the user enter a number.
- If the number is divisible by 3, print "fizz".
- If the number is divisible by 5, print "buzz".
- If the number is divisible by 15, print "fizzbuzz".

---

###     **Hex**
- Have the user enter a number.
- Print the number in hexadecimal notation.

*note*  
Implement the solution yourself. Do not use Python's `hex()` function.  

*hint*   
153 = 100 + 50 + 3  
0x12F = 0x100 + 0x20 + 0xF

---

###     **Rock, Paper, Scissors**
Build a two player rock paper scissors game. Rock beats scissors, scissors beats paer, paper beats rock.

- Ask player for their move. Valid moves are "rock", "paper", or "scissors".
- Have the computer make its choice randomly
- Compare the user's choice with the computer's choice.
- If the player wins, print "You win! :)"
- If the player loses, print "You lose. :("
- Do this repeatedly until the player types "exit", and keep track of the player's score.

*hint*  
Generate random numbers with the `rand()` function
