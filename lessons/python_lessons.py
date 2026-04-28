PYTHON_LESSONS = [

   
    # ========== LEVEL 1: BASICS (Lessons 1–7) ==========

    {
        "id": 1,
        "title": "What is Python?",
        "target": "print('Python was created by Guido van Rossum')",
        "instr": "Python is a popular programming language created by Guido van Rossum and released in 1991."
    },
    {
        "id": 2,
        "title": "Why Python?",
        "target": "print('Python has a simple syntax similar to English')",
        "instr": "Python works on many platforms and has simple syntax."
    },
    {
        "id": 3,
        "title": "The Interpreter System",
        "target": "print('Python runs on an interpreter system')",
        "instr": "Python executes code line-by-line using an interpreter."
    },
    {
        "id": 4,
        "title": "Python Syntax",
        "target": "if 5 > 2:\n    print('Five is greater than two!')",
        "instr": "Python uses indentation to define code blocks."
    },
    {
        "id": 5,
        "title": "Python Statements",
        "target": "print('Python is fun!')\nprint('Hello World!')",
        "instr": "A statement is an instruction. Python ends statements by newline."
    },
    {
        "id": 6,
        "title": "Output and Quotes",
        "target": "print(\"Double Quotes\")\nprint('Single Quotes')",
        "instr": "Text must be inside quotes. print() outputs text."
    },
    {
        "id": 7,
        "title": "Outputting Numbers",
        "target": "print(358)\nprint(3 + 3)\nprint(2 * 5)",
        "instr": "Numbers do not need quotes. You can do math inside print()."
    },

    # ========== 📝 EXAM 1: After Level 7 ==========

    {
        "id": 8,
        "title": "📝 EXAM 1: Python Basics",
        "is_exam": True,
        "exam_number": 1,
        "pass_score": 70,
        "covers_lessons": "1-7",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write Python code to print 'Hello World'",
                "answer": "print('Hello World')"
            },
            {
                "question": "Create a variable name='Razan' and print it",
                "answer": "name = 'Razan'\nprint(name)"
            },
            {
                "question": "Write code that prints the result of 5 + 10",
                "answer": "print(5 + 10)"
            },
            {
                "question": "Write code that prints both text and number in one line",
                "answer": "print('Age:', 20)"
            },
            {
                "question": "Write code that prints the second item in ['a','b','c']",
                "answer": "lst = ['a','b','c']\nprint(lst[1])"
            }
        ]
    },

    # ========== LEVEL 2: DATA TYPES & LISTS (Lessons 8–14) ==========
{
        "id": 9,
        "title": "Mixing Text and Numbers",
        "target": "print('I am', 35, 'years old.')",
        "instr": "You can mix text and numbers using commas."
    },
    {
        "id": 10,
        "title": "Python Comments",
        "target": "# This is a comment\nprint('Comments are ignored')",
        "instr": "Comments start with # and are ignored by Python."
    },
    {
        "id": 11,
        "title": "Creating Variables",
        "target": "x = 5\ny = 'John'\nprint(x)\nprint(y)",
        "instr": "Variables are created when assigned a value."
    },
    {
        "id": 12,
        "title": "Variable Naming Rules",
        "target": "myvar = 'John'\n_my_var = 'John'\nmyVar2 = 'John'",
        "instr": "Variable names must start with a letter or underscore."
    },
    {
        "id": 13,
        "title": "Assigning Multiple Values",
        "target": "x, y, z = 'Orange', 'Banana', 'Cherry'\nprint(x, y, z)",
        "instr": "You can assign multiple variables in one line."
    },
    {
        "id": 14,
        "title": "Built-in Data Types",
        "target": "x = 5\nprint(type(x))\ny = 'Hello'\nprint(type(y))",
        "instr": "Python has many built-in data types."
    },
    {
        "id": 15,
        "title": "Python Numbers",
        "target": "x = 1\ny = 1.1\nz = -325",
        "instr": "Python has int, float, and complex numbers."
    },

    # ========== 📝 EXAM 2: After Level 14 ==========

    {
        "id": 16,
        "title": "📝 EXAM 2: Data Types & Variables",
        "is_exam": True,
        "exam_number": 2,
        "pass_score": 75,
        "covers_lessons": "8-14",
        "exam_type": "question",
        "questions": [
            {
                "question": "Create variables a=10, b='Hello' and print both",
                "answer": "a = 10\nb = 'Hello'\nprint(a, b)"
            },
            {
                "question": "Write code to check the type of 3.14",
                "answer": "print(type(3.14))"
            },
            {
                "question": "Assign x='A', y='B', z='C' in one line",
                "answer": "x, y, z = 'A', 'B', 'C'"
            },
            {
                "question": "Write a comment in Python",
                "answer": "# This is a comment"
            },
            {
                "question": "Write code to print the third item in ['red','green','blue']",
                "answer": "colors = ['red','green','blue']\nprint(colors[2])"
            }
        ]
    },

    # ========== LEVEL 3: LISTS & LOOPS (Lessons 15–21) ==========

    {
        "id": 17,
        "title": "Multiline Strings",
        "target": "a = '''Hello\nWorld'''\nprint(a)",
        "instr": "Triple quotes allow multiline strings."
    },
    {
        "id": 18,
        "title": "Boolean Evaluation",
        "target": "print(10 > 9)\nprint(10 == 9)\nprint(10 < 9)",
        "instr": "Booleans return True or False."
    },
    {
        "id": 19,
        "title": "Arithmetic Operators",
        "target": "x = 15\ny = 4\nprint(x + y)\nprint(x % y)\nprint(x ** y)",
        "instr": "Python supports many arithmetic operators."
    },
    {
        "id": 20,
        "title": "The Walrus Operator",
        "target": "numbers = [1, 2, 3, 4, 5]\nif (n := len(numbers)) > 3:\n    print(n)",
        "instr": "The := operator assigns inside expressions."
    },
    {
        "id": 21,
        "title": "Python Lists",
        "target": "thislist = ['apple', 'banana', 'cherry']\nprint(thislist)\nprint(thislist[1])",
        "instr": "Lists store multiple items."
    },
    {
        "id": 22,
        "title": "Add and Remove List Items",
        "target": "thislist = ['apple', 'banana']\nthislist.append('orange')\nthislist.remove('apple')",
        "instr": "append() adds, remove() deletes."
    },
    {
        "id": 23,
        "title": "Sorting Lists",
        "target": "thislist = [100, 50, 65]\nthislist.sort()\nthislist.sort(reverse=True)",
        "instr": "sort() arranges items ascending or descending."
    },
# ========== 📝 EXAM 3: After Level 21 ==========

    {
        "id": 24,
        "title": "📝 EXAM 3: Lists & Operators",
        "is_exam": True,
        "exam_number": 3,
        "pass_score": 80,
        "covers_lessons": "15-21",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write code to append 'kiwi' to a list fruits",
                "answer": "fruits.append('kiwi')"
            },
            {
                "question": "Write code to sort [3,1,2] ascending",
                "answer": "lst = [3,1,2]\nlst.sort()"
            },
            {
                "question": "Write code to print True if 5 > 2",
                "answer": "print(5 > 2)"
            },
            {
                "question": "Write code to print the length of [1,2,3]",
                "answer": "print(len([1,2,3]))"
            },
            {
                "question": "Write code to remove 'apple' from ['apple','banana']",
                "answer": "lst = ['apple','banana']\nlst.remove('apple')"
            }
        ]
    },

    # ========== LEVEL 4: EXTRA LESSONS TO REACH LEVEL 28 ==========

    {
        "id": 25,
        "title": "If and Elif Statements",
        "target": "a = 33\nb = 33\nif b > a:\n    print('b is greater')\nelif a == b:\n    print('equal')",
        "instr": "elif checks another condition."
    },
    {
        "id": 26,
        "title": "While Loops",
        "target": "i = 1\nwhile i < 6:\n    print(i)\n    i += 1",
        "instr": "while repeats while condition is true."
    },
    {
        "id": 27,
        "title": "Loop Control: Break",
        "target": "i = 1\nwhile i < 6:\n    if i == 3:\n        break\n    print(i)\n    i += 1",
        "instr": "break stops the loop."
    },
    {
        "id": 28,
        "title": "Defining Functions",
        "target": "def my_function():\n    print('Hello')\nmy_function()",
        "instr": "Functions run only when called."
    },

    # ========== 📝 EXAM 4: After Level 28 ==========

    {
        "id": 29,
        "title": "📝 FINAL EXAM 4: Python Level 28",
        "is_exam": True,
        "exam_number": 4,
        "pass_score": 85,
        "covers_lessons": "22-28",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write a function called greet() that prints 'Hello'",
                "answer": "def greet():\n    print('Hello')"
            },
            {
                "question": "Write a while loop that prints numbers 1 to 3",
                "answer": "i = 1\nwhile i <= 3:\n    print(i)\n    i += 1"
            },
            {
                "question": "Write code that breaks a loop when i == 5",
                "answer": "if i == 5:\n    break"
            },
            {
                "question": "Write an if/elif statement that prints 'Match' if x==10",
                "answer": "if x == 10:\n    print('Match')"
            },
            {
                "question": "Write code to sort ['b','a','c']",
                "answer": "lst = ['b','a','c']\nlst.sort()"
            }
        ]
    }

]
