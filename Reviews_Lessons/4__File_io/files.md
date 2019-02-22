# More File I/O

Last time, we looked at some ways to get input from a file, rather than prompting 
the user to enter it.  

## Opening a file
The first thing we did was use the `open` method to open our file. This method creates 
and returns a file *object* that we put into a variable. *(We'll learn more about objects later.)*   

The function takes two arguments. The first is a string representing the name of the 
file to be opened. The second is a string representing the mode in which to open the 
file. A summary of these modes is listed below.  

| Mode | Action                                                   |  
|------|----------------------------------------------------------|  
| "r"  | reading                                                  |
| "w"  | writing. Creates a new file if "filename" doesn't exist. |
| "w+" | reading and writing. Creates a new file if "filename" doesn't exist.                                      |
| "a+" | reading and appending to the end of the file. Creates a new file if "filename" doesn't exist.            |


```Py
f = open("my_file.txt", 'r')

f.close() # Remember to close your files!
```

## Reading from a file

Once the file is open, we can start doing stuff with it.

The first method we used to do this was `f.read()`. This function returns the contents 
of the entire file as a string. It takes an optional argument that allows you to 
specify a number of bytes to read.  

```Py
input_file = open("my_file.txt", 'r')

contents = input_file.read()

f.close() # Remember to close your files!
```

We don't always want to read the whole file right away. Sometimes we only want a 
single line. For that, we use `f.readline()`. This returns a single line as a string.
```Py
input_file = open("my_file.txt", 'r')

firstline = input_file.readline()

f.close() # Remember to close your files!
```

If we want the first `n` lines in a file, we can use a count controlled loop.  

```Py
input_file = open("my_file.txt", 'r')

firstlines = []

for i in range(10):
    firstlines.append(input_file.readline())

f.close() # Remember to close your files!
```

Of course, this is only useful if you know how many lines you want.  
What if we want them all?

```Py
input_file = open("my_file.txt", 'r')

all_lines = input_file.readlines()

f.close() # Remember to close your files!
```  

## Looping Over Files
We already saw how we can use a count controlled loop to iterate over a certain number 
of lines. It turns out, just like lists or `range()`, file objects are iterable! This 
means we can iterate over lines in a file just like we would a list or range.

```Py
input_file = open("my_file.txt", 'r')

list_lines = []

for line in file:
    list_lines.append(line.strip('\n'))

f.close() # Remember to close your files!
```


## Writing to files
Writing to files is pretty simple. Use `f.write(<string>)` where `<string>` is the 
string to be written.  

```Py
output_file = open("my_file.txt", 'w')

output = ["This is the first line", "This is the second line.", 1, 2, 4]

for i in output:
    output_file.write(str(output[i]))

output_file.close()
```

We can also use `f.writelines()` to accomplish the same thing.  

```Py
output_file = open("my_file.txt", 'w')

for i in output:
    output_file.writelines(output[i])

output_file.close()
```

## Other Useful Methods
These tend to come up a lot when dealing with files.

| Method                | Description |
------------------------|-------------|
| `.strip([char])`      | Removes all occurrences of `char` from the beginning and end of a string (whitespace by default). Especially useful for newlines. |
| `.split([delimiter])` | Splits a string into a list of substrings, separated by `delimeter` (`' '` by default) |
| `.find(str)`          | Returns the index where `str` occurs in a string, -1 if not found |
| `.replace(str1, str2)`| Same as find, but replaces str1 with str2. |



---

# Exercises


## Find and Replace
- Ask the user for a filename
- Ask the user for a string to find within the file, and a string to replace it with.
- Find any occurrence of that string within the file, and replace it with the desired string.
- Write the changes to the same file and exit.  

## Login Program 2: Electric Boogaloo
A few weeks ago we wrote a program that allowed users to register and login to a system, 
but there was a huge problem. Our database of users went away whenever we closed the program. 

- Extend the program so that:
- The database is written to a file when the program closes
- The database is loaded into the program when the program is opened.
- (Optional) While the program is running, the user can specify a new file from which
to load the database. Upon closing the program, this database will be written to that same file.

If you don't have this program, you can dowload it from this repository.  


## hexdump
- Ask the user for a file name.
- Print the contents of the file as a series of hexadecimal digits in groups of 4.

### Example
- input: `somefile.txt`
- output: 
```
e6 b0 08 04 e7 9e 08 04 e7 bc 08 04 e7 d5 08 04
e7 e4 08 04 e6 b0 08 04 e7 f0 08 04 e7 ff 08 04
e8 0b 08 04 e8 1a 08 04 e6 b0 08 04 e6 b0 08 04
```
*hint: read one byte at a time and convert to integers*

## Checksum (Hard)
Sometimes, it's necessary to make sure that a file hasn't been modified, which can
happen accidentally, or maliciously. One way that we do that is with a checksum. Here's 
how it works. First, you take all the bytes in the file and add them up, modulo some 
number. (We'll use 1024 for this example), then you append that number to the end of the file. Now all you have to do to 
make sure the file is the same is calculate your own checksum and compare it with the 
sum at the end of the file.  

- Ask the user for a filename, open in 'r+'
- Have the user choose: check or append
- if append:
    - Calculate the checksum for the file.
    - Write the checksum to a new file
- if check:
    - Ask the user for a filename containing the checksum
    - Calculate the checksum for the input file and compare.

Go [here](https://github.com/aahadley/Junior-Knights/tree/master/Reviews_Lessons/4__File_io) for some sample files to use.