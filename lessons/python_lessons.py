# Python Programming Lessons

PYTHON_LESSONS = [
    {
        "id": 1,
        "title": "Hello World",
"target": "print('Hello World')",
        "instr": "The classic first program - print() outputs text."
    },
    {
        "id": 2,
        "title": "Variables",
        "target": "name = 'Alice'\nage = 25\nprint(name, age)",
        "instr": "Variables store data. Use = to assign values."
    },
    {
        "id": 3,
        "title": "User Input",
        "target": "user_name = input('Enter your name: ')\nprint(f'Hello {user_name}')",
        "instr": "input() gets user input. f-strings format text."
    },
    {
        "id": 4,
        "title": "Numbers & Math",
        "target": "x = 10\ny = 3\nresult = x + y * 2\nprint(result)",
        "instr": "Python can do math with + - * / operators."
    },
    {
        "id": 5,
        "title": "If Statements",
        "target": "age = 18\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "instr": "if/else statements control program flow."
    },
    # Make sure it looks like this (no hidden tab characters)
# Make sure it looks like this (no hidden tab characters)
{
    "id": 6,
    "title": "For Loops",
    "target": "for i in range(5):\n    print(f'Number {i}')",
    "instr": "for loops repeat code a specific number of times."
},
    {
        "id": 7,
        "title": "While Loops",
        "target": "count = 0\nwhile count < 3:\n    print(count)\n    count += 1",
        "instr": "while loops repeat until a condition is False."
    },
    {
        "id": 8,
        "title": "Lists",
        "target": "fruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(fruit)",
        "instr": "Lists store multiple items in order."
    },
    {
        "id": 9,
        "title": "List Operations",
        "target": "numbers = [1, 2, 3]\nnumbers.append(4)\nnumbers.remove(2)\nprint(numbers)",
        "instr": "Lists have methods like append() and remove()."
    },
    {
        "id": 10,
        "title": "Dictionaries",
        "target": "person = {'name': 'Bob', 'age': 30}\nprint(person['name'])",
        "instr": "Dictionaries store key-value pairs."
    },
    {
        "id": 11,
        "title": "Functions",
        "target": "def greet(name):\n    return f'Hello {name}'\n\nresult = greet('World')\nprint(result)",
        "instr": "Functions organize reusable code blocks."
    },
    {
        "id": 12,
        "title": "Function Parameters",
        "target": "def add(a, b):\n    return a + b\n\nprint(add(5, 3))",
        "instr": "Functions can take multiple parameters."
    },
    {
        "id": 13,
        "title": "String Methods",
        "target": "text = 'hello world'\nprint(text.upper())\nprint(text.title())\nprint(text.replace('world', 'python'))",
        "instr": "Strings have many useful methods."
    },
    {
        "id": 14,
        "title": "List Comprehension",
        "target": "squares = [x**2 for x in range(5)]\nprint(squares)",
        "instr": "List comprehension creates lists concisely."
    },
    {
        "id": 15,
        "title": "Try/Except",
        "target": "try:\n    num = int(input('Enter number: '))\nexcept ValueError:\n    print('That is not a number!')",
        "instr": "Try/except handles errors gracefully."
    },
    {
        "id": 16,
        "title": "File Reading",
        "target": "with open('file.txt', 'r') as f:\n    content = f.read()\n    print(content)",
        "instr": "with open() reads files safely."
    },
    {
        "id": 17,
        "title": "Writing Files",
        "target": "with open('output.txt', 'w') as f:\n    f.write('Hello File!')",
        "instr": "Write mode ('w') creates or overwrites files."
    },
    {
        "id": 18,
        "title": "Classes",
        "target": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    \n    def bark(self):\n        return f'{self.name} says Woof!'\n\nmy_dog = Dog('Rex')\nprint(my_dog.bark())",
        "instr": "Classes define blueprints for objects."
    },
    {
        "id": 19,
        "title": "Inheritance",
        "target": "class Animal:\n    def speak(self):\n        pass\n\nclass Cat(Animal):\n    def speak(self):\n        return 'Meow'\n\ncat = Cat()\nprint(cat.speak())",
        "instr": "Inheritance allows classes to reuse code."
    },
    {
        "id": 20,
        "title": "Lambda Functions",
        "target": "multiply = lambda x, y: x * y\nprint(multiply(4, 5))",
        "instr": "Lambda creates small anonymous functions."
    }
]