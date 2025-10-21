# Multiplying two integers: 2 * 9 = 18
print(2 * 9)

# Printing a multi-line string using triple quotes (''' or """)
# Everything between triple quotes is printed as-is, including new lines and spaces.
print('''Hello
        How are You Laraib?
''')

'''
This is a multi-line comment.
It is enclosed in triple quotes and is not executed by Python.
Developers use it to describe sections of code.
'''

# Using escape sequences:
# \" allows you to include double quotes inside a string enclosed in double quotes.
print("Hello \"How are You Laraib?\"")     # Output: Hello "How are You Laraib?"

# \' allows you to include single quotes inside a string enclosed in single quotes.
print("Hello \'How are You Laraib?\'")     # Output: Hello 'How are You Laraib?'

# \n inserts a newline character (moves the text after it to a new line).
print("Hello \nHow are You Laraib?")       # Output:
# Hello
# How are You Laraib?

# \t inserts a tab space (equivalent to pressing the Tab key once).
print("Hello \tHow are You Laraib?")       # Output: Hello    How are You Laraib?



# \r moves cursor back to the start of the line (carriage return)
# Anything printed after it overwrites what came before
print("Hello \rHow are You Laraib? I am using carriage return.")
# Explanation:
# - "Hello" is printed
# - \r moves cursor to line start
# - "How are You Laraib?" overwrites from beginning
# Output (Windows console example): "How are You Laraib?"



# Another example to visualize overwriting
print("Loading... 100%\rComplete!")
# Output on console: "Complete!" (the word 'Complete!' overwrites part of 'Loading... 100%')

# Another carriage return example — dynamic line updates (used in progress bars)
from Time import time

for i in range(5):
    print(f"Processing {i+1}/5\r", end='')   # '\r' keeps overwriting the same line
    time.sleep(0.5)
print("\nDone!")  # Move to next line after loop
# Output:
# Processing 1/5
# (updates same line until Done!)

# \b is a backspace — it deletes one character before it.
print("Hello \bHow are You Laraib?")       # Output: HelloHow are You Laraib?


# \\ prints a single backslash
print("C:\\Users\\Laraib\\Documents")
# Output: C:\Users\Laraib\Documents

# Example combining multiple escape sequences
print("Name:\tLaraib\nCity:\tLahore\rCountry: Pakistan")
# \t adds tabs, \n makes new line, \r overwrites line start


# The 'sep' parameter defines what separates multiple values in print().
# By default, sep = " " (a space), but you can change it to anything like "-" or "~".
print("Hello Laraib", "How are You Laraib?", "I am using escape sequences.", sep="-")
# Output: Hello Laraib-How are You Laraib?-I am using escape sequences.
# After printing, Python automatically adds a newline at the end (because end="\n" by default).


# The 'end' parameter defines what to print AFTER the line finishes.
# By default, end = "\n" (a newline), but here we change it to "-".
print("Hello Laraib", "How are You Laraib?", "I am using escape sequences.", end="-")
# Output: Hello Laraib How are You Laraib? I am using escape sequences.-
# Note: No newline is printed here (because end="-" not "\n").
# So, the next print() statement continues on the SAME LINE.


# Combining 'sep' and 'end':
# 'sep' = "~" → separates items with a tilde (~)
# 'end' = "-" → adds a dash at the end, but does NOT move to a new line.
print("Hello Laraib", 9, 6, sep="~", end="-")
# Output (joins with previous line because previous print had no newline):
# Hello Laraib How are You Laraib? I am using escape sequences.-Hello Laraib~9~6-
