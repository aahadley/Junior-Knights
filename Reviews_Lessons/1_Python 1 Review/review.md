# Python Review
This is brief a one-page review of everything you've already learned. You can think of it as a cheat sheet to refer back to when you forget how to do something. If you want further explanations, check out the [*Introduction to Python* page](http://www.eecs.ucf.edu/JuniorKnights/material/), or [Rachael's slides](https://github.com/rsera/Junior-Knights).  

https://docs.python.org/3/tutorial/datastructures.html

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
To get input, we use the `input()` function. `input()` takes an optional string as an argument. This string will be used as a prompt for your user. By default, this will return a string. If you want another type, you'll need to cast in with `int()`, `float()`, etc.

```Py
s = input("Enter a string.")
print(s)

a = int(input("Enter a number."))
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

Strings can be concatenated with the `+` operator, or multiply concatinated with `*`.

```Py
s = "To boldly go "
t = "A long time ago, "

w = "where no one has gone before!"
g = "in a galaxy far, far away"

print(s + w)
print(t + g)

deck = "Deck the halls with boughs of holly "
fa = "fa"

print(deck + fa + "la" * 8) 
```

###     Booleans
Boolean types can  only have one of two values, ```True``` or ```False```.
```Py
a = True
b = False
```

---

## Arithmetic Operations
Adding and subtracting numbers is very intuitive in Python.

```Py
# adding integers
a = 18
b = 2
c = a - b   # c == 20

# adding floats
f = 2.5
fsum = f + f   # g == 5

# *note* sum() is a built in function so we can't use sum as a variable name

# What happens when we add/subtract a float to an int?
result = b + f
print(result)

# We can also make use of the += and -= operations
f += a
b -= c
```

Multiplication and division are just as easy, but there's a catch.
```Python
a = 5
b = 2

product = a * b

# How do we want to handle division? We have two ways:
#   The first is floating point division. This is just like punching numbers into your
# calculator.

integer_quotient = a / b

# Sometimes we don't want a decimal value, so we use integer division. Integer division
# is just like performing "long division" and ignoring the remainder. We specify this by
# using two slashes "//".

quotient = a // b

# 2 goes into 5 exactly 2 times, and leaves a remainder of 1.
# What if we want the remainder?
# Then we use the mod operator "%".

modulus = a % b

# Exponentiation

a = 2
b = 3

# Exponentiation is the term for repeated multiplication. We say that 2 to the third power
# is equal to 2 * 2 * 2. To do this in Python, we use "**".

power = 2**3
```

---

## Conditional Logic (if-else)
The format for an if statement is 
```Py
if <boolean expression>:
    <statement>
    <statement>
    ...
    <statement>

# Otherwise, go here

elif <boolean expression>:  # These are optional and you can have as many as you like.
    <statement>
    <statement>
    ...
    <statement>

else:   # You can only have one of these. Note that there is no boolean expression.
    <statement>
...
...
```
If the result of the boolean expression is `True`, then the body of the if statement will execute. Otherwise, it will skip to the end of it.

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
While loops are a lot like if statements, but with a key difference. After the body of an if statement, the program simply goes to the next line. a `while` loop will repeat until its condition is `False`. The general format looks like this.

```Py
while <boolean expressions>:
    <statement>
    <statement>
    ...
    <statement>
```

`while True:` will repeat forever, or until it encounters a `break`. We can use `continue` to jump to the top of a loop.

```Py
a = 1
b = 0

while True:
    a += 1
    b = random.randint()

    if b == 7:
        continue
    
    if a >= 100:
        break
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
    <statement>
    <statement>
    ...
    <statement>
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
def function_name(<arguments>):
    <statement>
    <statement>
    ...
    <statement>

    return <value>
```
The `def` keyword is short for *define* and signifies to the interpereter that you're about to define a function.  
<Arguments> is one or more variables that the function will use.  
The body of the function is a series of steps that the function will carry out. Finally, we see the `return` keyword followed by a return value.  
This is the final value that a function might put into a variable.  
Let's see an example.

```Py
def my_function(x, y):
    r = x + y
    r *= 2

    return r

x = my_function(3, 4)
print(x)

print(my_function(3, 4) + 5)
```
1. First, we define a function called `my_function`. It takes two arguments, `x` and `y`, adds them, then doubles them and returns the result.
2. Next, we  pass 3 and 4 to `my_function`.
3. Then we create a variable `x` and we put the return value of `my_function` in `x`, and print `x`.
4. In the last line, we can see that a function can behave just as a regular variable. We pass 3 and 4 to the function, add 5 to the result, and print it, all in one line.

---

## Lists
A list is an *ordered*, *mutable* collection of objects. You can declare a list by using square brackets with zero or more values, separated by commas.

```Py
a1 = []
a2 = [1]
a3 = [1, 2, 3]
a4 = [3, "a", True, a2, my_function(3,4)]
```

The things inside the list are called *elements*. To access a specific element of a list, type the name of the list, followed by the index of the desired element. **Remember, we start counting from 0**

Try to determine the output of this program.

```Py
a1 = []
a2 = [1]
a3 = [1, 2, 3]
a4 = [3, "a", True, a2, my_function(3,4), print]

x = a2[0]
print(x)

print(a3[3])

a[5](my_function(a[4]))

# You can use the + operator to add elements to a list, 
# or to add all elements in one list to another.
a3 += 4
a3 += a4

print(a3)
```

---

## Tuples
Tuples are like lists, except they are immutable and a little bit faster. You declare them with `()`, and can index them just like lists, but you can't change them after they're created. Since we're using parentheses, we have to be careful about declaring tuples with one element. `t = (1)` would just assign an integer, so python provides an alternate syntax `t = 1,` for this.

```Py
t1 = ()
t2 = 1,
t3 = (1, 2, 3)
t4 = (3, "a", True, t2, my_function(3,4), my_function)

t4[3] = 5 # This will throw an error, because tuples are immutable!

# Addition works the same with tuples as it does with lists
t3 += t4

print(t3)
```

---

## Sets
Sets are another data structure used to create *unordered* collections of *distinct* elements. These behave just like sets in mathematics. We declare sets using `{}` but there's a catch. `s = {}` would create an empty dictionary, so to create an empty set, we use `s = set()`. We are also more limited with what we can add to a set, than with what we can add to lists or tuples. In particular, you can't add a list or a set to a set.

```Py
s1 = set()
s2 = {1}
s3 = {1, 2, 3}
s4 = {3, "a", True, my_function(3,4), my_function}

print({1} == {1, 1} == {1, 1, 1}) # True

a1 = [1, 2, 3]
t1 = (1, 2, 3)

s3.add(a1) # throws an error
s3.add(t1) # is fine.
```

Sets also support some very useful mathematical operations. 

These operations take two sets, `a` and `b`, and return another set `c`.

| Operation            | Meaning                        | Shorthand    |
|----------------------|--------------------------------|--------------|
| `c = a.union(b)`     | All elements in a, or in b     | `c = a | b`  |
| `c = a.intersect(b)` | All elements in both a and b   | `c = a & b`  |
| `c = a.difference(b)`| All elements in a but not in b | `c = a - b`  |
|`c = a.symmetric_difference(b)`|All elements in a or b, but not both|`c = a ^ b`|

```Py
a = {1, 2, 3}
b = {3, 4, 5}

union        = a | b # {1, 2, 3, 4, 5}
intersection = a & b # {3}
difference   = a - b # {1, 2}
xor          = a ^ b # {1, 2, 4, 5}
```

---

## Dictionaries
Dictionaries are an incredibly useful data structure that allows us to map *keys* to *values*. You can think of this as the equivalent of a hash map in other languages. We declare dictionaries with `d = {key1 : value1, key2 : value2}`. We can then access a value with `d[key]`.

```Py
d1 = {}
d2 = {"one" : 1, "two" : 2}
d3 = {3: "three", "a": 0, "Programming is fun" : True}

facts = {"Programming is fun"                     : True , 
         "Java is better than Python"             : False, 
         "Sets can contain duplicate elements"    : False, 
         "Charmander is the best starter Pokemon" : True }

print(d["one"]) # 1

# You can add to a dictionary like this
d2["three"] = 3

print(facts["Charmander is the best starter Pokemon"]) # True
```

---

## Common Keywords
These keywords work for lists, tuples, sets, and dictionaries. 


where `D` is a list, tuple, set, or dictionary

| keyword | behavior                                | example   |
|---------|-----------------------------------------|-----------|
| in      | Returns `True` if a is in D             | `a in D`  |
| del     | Delete the element at a specified index | `del D[a]`|

\* *(Exception: `del` doesn't work on sets. use `D - {n}` to delete instances of `n` instead)*

---

## Iterables
Strings, lists, tuples, and sets are all iterable, which means you can use a `for` loop to loop through all its elements. `range()` is a function that returns an iterable, which is why we use it for count controlled loops.  

```Py
lst = [1, 2, 3, 4, 5]
tpl = tuple(lst)   # returns a tuple with the same elements as l
ste = set(lst)     # returns a set with the same elements in l. **does NOT preserve order**
ltr = lst("Aaron") # Returns the letters in "Aaron" as a list

for i in lst:
    print(i**2)

for i in tpl:
    print(lst[i-1])

for letter in "Aaron":
    print(letter, ord(letter))
```

Looping through dictionaries is a bit more complicated. You can use `keys()` to return a list of all the keys in a dictionary, `values()` to return a list of all values, and `items()` to return a list of tuples of the form `(key, value)`.  

```Py
dct = {1 : "one", 2 : "two", 3 : "three"}

for i in dct.keys():  # 1 2 3
    print(i)          # this puts a space at the end instead of a newline

for i in dct.values(): # one two three (on seperate lines)
    print(i)

for k, v in dct.items(): # 1 one 2 two 3 three
    print(i, j)
```

---

## Slicing
You can use slices to get a range of indeces from a list or tuple. The general format is `lst[start:stop:step]`. `step` is optional, `start` is inclusive and defaults to zero if not provided. `stop` defaults to the end of the list if not provided.

```Py
lst = [1, 2, 3, 4, 5, 6, 7]

print( lst[2:4]   )   # [3, 4]
print( lst[2:5:2] )   # [3, 5, 7]
print( lst[:4]    )   # [1, 2, 3, 4]
print( lst[2:]    )   # [3, 4, 5, 6, 7]
print( lst[::-1]  )   # [7, 6, 5, 4, 3, 2, 1]
```

---

## Comprehensions
Let's say we want to build a list consisting of all the even numbers from 1-1000. We might do so with a `for` loop like this:

```Py
lst = []
for i in range(0, 101, 2):
    lst += i
```
This is all fine and dandy, but we're forgetting the Fundamental Theorem of Computer Science: **programmers are lazy.** Thankfully, python gives us a shorthand for this.

```Py
evens = [i for i in range(0, 101, 2)]
```

These can be quite robust. Here are a few examples.

```Py
squares = [i**2 for i in range(100)] # generates the squares of all values from 0-100

even_squares = [i for i in squares if i % 2 == 0] # generates all even values in squares

plaintext = "hello world"

salad = ["".join([chr((((ord(letter) - key) - ord('a')) % 26) + ord('a')) for letter in plaintext.lower() if letter != ' '])for key in range(1,27) if key % 2 == 0]

# Generates the caesar cipher of a plaintext for every other possible key.
# This is needlessly convoluted and is only meant to show how powerful list comprehensions can be.

```

---
---
---


## Exercises
###     **fizzbuzz**
fizzbuzz is a classic problem that every programmer should be able to solve.
- Have the user enter a number.
- If the number is divisible by 3, print "fizz".
- If the number is divisible by 5, print "buzz".
- If the number is divisible by 15, print "fizzbuzz".

---

###     **Hex**
Convert numbers from decimal to hexadecimal. It's trickier than it seems!

- Have the user enter a number.
- Print the number in hexadecimal notation.

*note*  
Implement the solution yourself. Do not use Python's `hex()` function.  

*hint*   
153 = 100 + 50 + 3  
0x12F = 0x100 + 0x20 + 0xF

Now try it the other way. Read in a string representing a hexadecimal number and print it in decimal.

---

###     **Rock, Paper, Scissors**
Build a two player rock paper scissors game. Rock beats scissors, scissors beats paer, paper beats rock.

- Ask player for their move. Valid moves are "rock", "paper", or "scissors".
- Have the computer make its choice randomly
- Compare the user's choice with the computer's choice.
- If the player wins, print `You win! :)`
- If the player loses, print `You lose. :(`
- Do this repeatedly until the player types "exit", and keep track of the player's score.

*hint*  
Generate random numbers with the `random.radint()`
