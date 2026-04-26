# Complete Python Programming Lessons from "What is Python.docx"

PYTHON_LESSONS = [
    {
        "id": 1,
        "title": "What is Python?",
        "target": """print('Python was created by Guido van Rossum')""",
        "instr": "Python is a popular programming language created by Guido van Rossum and released in 1991. It is used for web development (server-side), software development, mathematics, and system scripting."
    },
    {
        "id": 2,
        "title": "Why Python?",
        "target": """print('Python has a simple syntax similar to English')""",
        "instr": "Python works on different platforms including Windows, Mac, Linux, and Raspberry Pi. It has a simple syntax similar to the English language that allows developers to write programs with fewer lines than some other programming languages."
    },
    {
        "id": 3,
        "title": "The Interpreter System",
        "target": """print('Python runs on an interpreter system')""",
        "instr": "Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick."
    },
    {
        "id": 4,
        "title": "Python Syntax",
        "target": """if 5 > 2:
    print('Five is greater than two!')""",
        "instr": "Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses. Python relies on indentation using whitespace to define scope. The number of spaces is up to you, but it must be at least one. The most common use is four spaces."
    },
    {
        "id": 5,
        "title": "Python Statements",
        "target": """print('Python is fun!')
print('Hello World!')""",
        "instr": "A computer program is a list of instructions to be executed by a computer. In a programming language, these programming instructions are called statements. In Python, a statement usually ends when the line ends. You do not need to use a semicolon like in many other programming languages."
    },
    {
        "id": 6,
        "title": "Output and Quotes",
        "target": """print("Double Quotes")
print('Single Quotes')""",
        "instr": "You can use the print() function to display text or output values. Each call prints text on a new line by default. Text in Python must be inside quotes. You can use either double quotes or single quotes."
    },
    {
        "id": 7,
        "title": "Outputting Numbers",
        "target": """print(358)
print(3 + 3)
print(2 * 5)""",
        "instr": "You can also use the print() function to display numbers. However, unlike text, numbers are not put inside quotes. You can also do math inside the print() function."
    },
    {
        "id": 8,
        "title": "Mixing Text and Numbers",
        "target": """print('I am', 35, 'years old.')""",
        "instr": "You can combine text and numbers in one output by separating them with a comma."
    },
    {
        "id": 9,
        "title": "Python Comments",
        "target": """# This is a comment
print('Comments are ignored')""",
        "instr": "Comments can be used to explain Python code, make the code more readable, or prevent execution when testing code. Comments start with a #, and Python will ignore them."
    },
    {
        "id": 10,
        "title": "Creating Variables",
        "target": """x = 5
y = 'John'
print(x)
print(y)""",
        "instr": "Variables are containers for storing data values. Python has no command for declaring a variable. A variable is created the moment you first assign a value to it."
    },
    {
        "id": 11,
        "title": "Variable Naming Rules",
        "target": """myvar = 'John'
_my_var = 'John'
myVar2 = 'John'""",
        "instr": "Variable naming rules: A variable name must start with a letter or the underscore character. It cannot start with a number. It can only contain alpha-numeric characters and underscores. Variable names are case-sensitive (age, Age and AGE are three different variables). A variable name cannot be any of the Python keywords."
    },
    {
        "id": 12,
        "title": "Assigning Multiple Values",
        "target": """x, y, z = 'Orange', 'Banana', 'Cherry'
print(x, y, z)""",
        "instr": "Python allows you to assign values to multiple variables in one line. Make sure the number of variables matches the number of values, or else you will get an error."
    },
    {
        "id": 13,
        "title": "Built-in Data Types",
        "target": """x = 5
print(type(x))
y = 'Hello'
print(type(y))""",
        "instr": "In programming, data type is an important concept. Variables can store data of different types. Python has built-in data types including: Text Type (str), Numeric Types (int, float, complex), Sequence Types (list, tuple, range), Mapping Type (dict), Set Types (set, frozenset), Boolean Type (bool), Binary Types (bytes, bytearray, memoryview), and None Type (NoneType). You can get the data type of any object by using the type() function."
    },
    {
        "id": 14,
        "title": "Python Numbers",
        "target": """x = 1
y = 1.1
z = -325""",
        "instr": "There are three numeric types in Python: int (integers), float (floating point numbers with decimals), and complex."
    },
    {
        "id": 15,
        "title": "Multiline Strings",
        "target": """a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit'''
print(a)""",
        "instr": "You can assign a multiline string to a variable by using three quotes. You can use either three double quotes or three single quotes."
    },
    {
        "id": 16,
        "title": "Boolean Evaluation",
        "target": """print(10 > 9)
print(10 == 9)
print(10 < 9)""",
        "instr": "Booleans represent one of two values: True or False. When you compare two values, the expression is evaluated and Python returns the Boolean answer. When you run a condition in an if statement, Python returns True or False."
    },
    {
        "id": 17,
        "title": "Arithmetic Operators",
        "target": """x = 15
y = 4
print(x + y)
print(x % y)
print(x ** y)""",
        "instr": "Operators are used to perform operations on variables and values. Arithmetic operators include: + (addition), - (subtraction), * (multiplication), / (division), % (modulus/remainder), ** (exponentiation), and // (floor division)."
    },
    {
        "id": 18,
        "title": "The Walrus Operator",
        "target": """numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:
    print(n)""",
        "instr": "Python 3.8 introduced the := operator, known as the walrus operator. It assigns values to variables as part of a larger expression."
    },
    {
        "id": 19,
        "title": "Python Lists",
        "target": """thislist = ['apple', 'banana', 'cherry']
print(thislist)
print(thislist[1])""",
        "instr": "Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data. Since lists are indexed, lists can have items with the same value. The first item has index 0."
    },
    {
        "id": 20,
        "title": "Add and Remove List Items",
        "target": """thislist = ['apple', 'banana']
thislist.append('orange')
thislist.remove('apple')""",
        "instr": "To add an item to the end of the list, use the append() method. To insert a list item at a specified index, use the insert() method. The remove() method removes the specified item. The pop() method removes the specified index, or removes the last item if no index is specified."
    },
    {
        "id": 21,
        "title": "Sorting Lists",
        "target": """thislist = [100, 50, 65]
thislist.sort()
thislist.sort(reverse=True)""",
        "instr": "List objects have a sort() method that will sort the list alphanumerically, ascending, by default. To sort descending, use the keyword argument reverse = True."
    },
    {
        "id": 22,
        "title": "If and Elif Statements",
        "target": """a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')""",
"instr": "The elif keyword is Python's way of saying 'if the previous conditions were not true, then try this condition'. Python supports equality (a == b), inequality (a != b), less than (a < b), less than or equal to (a <= b), greater than (a > b), and greater than or equal to (a >= b). You can have as many elif statements as you need."
    },
    {
        "id": 23,
        "title": "While Loops",
        "target": """i = 1
while i < 6:
    print(i)
    i += 1""",
        "instr": "With the while loop we can execute a set of statements as long as a condition is true. Remember to increment your variable, or else the loop will continue forever."
    },

   {
    "id": 24,
    "title": "Loop Control: Break",
    "target": """i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1""",
    "instr": "With the break statement we can stop the loop even if the while condition is true. With the continue statement we can stop the current iteration and continue with the next."
},
    {
        "id": 26,
        "title": "Defining Functions",
        "target": """def my_function():
    print('Hello from a function')

my_function()""",
        "instr": "A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoid code repetition. In Python, a function is defined using the def keyword, followed by a function name and parentheses. The code inside the function must be indented."
    }
]