age = 30
print(age)

age = 40
print(age)

age_new = 50
print(age_new)

PI = 3.14
print(PI)

maths_operation = 1 + 3 * 4 / 2 - 2
print(maths_operation)
#Float Division

float_division = 12 / 3
print(float_division)

#Integer Division
integer_division = 12 // 3
print(integer_division)

#Remainder
remainder = 13 % 5
print(remainder)

#Strings

my_string = "Hello, world!"
single_quote_string = "Hello, world!"

# Strings can use either single or double quotes. It's up to you which one you use!
# Try to pick one and stick to it throughout all your code.
# If you work with others, and they prefer a specific style, you can all agree on which to use.

string_with_quotes = "Hello, it's me."
another_with_quotes = "He said \"You are amazing!\" today."

print(string_with_quotes)
print(another_with_quotes)

# If your string has quotation marks, make sure to use the other mark for the string itself
# Another option is to escape the quotation marks, but it is uglier and generally advised against:

escaped_quotes = 'He said "You are amazing!" yesterday.'
print(escaped_quotes)

# Multi-line strings are useful when you have very long ones and you want to be able to write them a bit more easily.
# Multi-line strings keep the lines in the strings!

multiline = """Hello, world.

My name is Jose. Welcome to my program.
"""
print(multiline)

## String operations

# Sring Concatenation.

name = "Jose"
greetings = "Hai, " + name

print(greetings)

# We cannot add strings and numbers this will throw error

age = 31
#print("You are " + age)

#Concatenation can be done with strings and strings only , if we wanted to add String and number the below should be done
# Turning number to String:
age = 31
age_as_string = str(34)
print("You are " + age_as_string)

#String formatting
# You can also use f-strings if you are using Python 3.6 or later.
# f-strings don't work in Python 3.5 or earlier.
# In f-strings, {name} gets replaced by the value of the variable name.

another_greeting = f"How are you, {name}"
print(another_greeting)

# It's also possible to use the format method.
name = "Bob"
name = "John"

final_greeting = "How are you, {}?".format(name)
print(final_greeting)

# The {} gets replaced by whatever is inside the brackets of the .format()

# You can also give names to variables inside a formattable string:
friend_name = "Rolf"
goodbye = "Goodbye, {name}!"
goodbye_rolf = goodbye.format(name=friend_name)
print(goodbye_rolf)

# Another example of using `.format()` on a variable:

greeting = "How are you, {}?"
print(greeting.format(name))

# Usually you will be using f-strings, just because they are shorter and more readable.
# However sometimes you may need to re-use a format string, and that is when using .format() is useful.
