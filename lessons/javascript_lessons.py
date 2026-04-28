# JavaScript Lessons with Question-Based Exams

JAVASCRIPT_LESSONS = [
    # ========== LEVEL 1: BASICS (Lessons 1-7) ==========
    {
        "id": 1,
        "title": "Console Output",
        "target": "console.log('Hello World');",
        "instr": "console.log() prints text to the console."
    },
    {
        "id": 2,
        "title": "Variables (let)",
        "target": "let name = 'Ahmed';\nlet age = 25;\nconsole.log(name, age);",
        "instr": "let declares variables that can change."
    },
    {
        "id": 3,
        "title": "Constants (const)",
        "target": "const PI = 3.14;\nconst BIRTH_YEAR = 2000;\nconsole.log(PI, BIRTH_YEAR);",
        "instr": "const declares variables that cannot change."
    },
    {
        "id": 4,
        "title": "Data Types",
        "target": "let str = 'Hello';\nlet num = 42;\nlet bool = true;\nconsole.log(typeof str, typeof num, typeof bool);",
        "instr": "JavaScript has: string, number, boolean, null, undefined."
    },
    {
        "id": 5,
        "title": "Template Literals",
        "target": "let name = 'Sara';\nlet age = 25;\nconsole.log(`Hello ${name}, you are ${age} years old`);",
        "instr": "Template literals use backticks (`) and ${} for variables."
    },
    {
        "id": 6,
        "title": "Arrays Basics",
        "target": "let fruits = ['apple', 'banana', 'cherry'];\nconsole.log(fruits[0]);\nfruits.push('date');\nconsole.log(fruits);",
        "instr": "Arrays store multiple values. push() adds to end."
    },
    {
        "id": 7,
        "title": "Array map() Method",
        "target": "let numbers = [1, 2, 3, 4];\nlet doubled = numbers.map(n => n * 2);\nconsole.log(doubled);",
        "instr": "map() creates a new array by transforming each element."
    },

    # ========== 🎯 EXAM 1 (After Lesson 7) ==========
    {
        "id": 8,
        "title": "📝 EXAM 1: JavaScript Basics",
        "is_exam": True,
        "pass_score": 70,
        "exam_number": 1,
        "covers_lessons": "1-7",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write JavaScript code to declare a variable called 'studentName' with value 'Ahmed'",
                "answer": "let studentName = 'Ahmed';"
            },
            {
                "question": "Write JavaScript code to declare a constant called 'BIRTH_YEAR' with value 2005",
                "answer": "const BIRTH_YEAR = 2005;"
            },
            {
                "question": "Write JavaScript code to print 'Hello World' to the console",
                "answer": "console.log('Hello World');"
            },
            {
                "question": "Write JavaScript code to create an array called 'colors' with values 'red', 'green', 'blue'",
                "answer": "let colors = ['red', 'green', 'blue'];"
            },
            {
                "question": "Write JavaScript code to add 'yellow' to the colors array using push()",
                "answer": "colors.push('yellow');"
            },
            {
                "question": "Write JavaScript code to use map() to double all numbers in [1, 2, 3, 4]",
                "answer": "let numbers = [1, 2, 3, 4];\nlet doubled = numbers.map(n => n * 2);"
            }
        ]
    },

    # ========== LEVEL 2: ADVANCED ARRAYS & OBJECTS (Lessons 9-14) ==========
    {
        "id": 9,
        "title": "Array filter()",
        "target": "let numbers = [1, 2, 3, 4, 5, 6];\nlet evens = numbers.filter(n => n % 2 === 0);\nconsole.log(evens);",
        "instr": "filter() creates a new array with elements that pass a condition."
    },
    {
        "id": 10,
        "title": "Array reduce()",
        "target": "let numbers = [10, 20, 30];\nlet sum = numbers.reduce((a, b) => a + b, 0);\nconsole.log(sum);",
        "instr": "reduce() combines array elements into a single value."
    },
    {
        "id": 11,
        "title": "Objects",
        "target": "let person = { name: 'Ali', age: 30, city: 'Riyadh' };\nconsole.log(person.name);\nconsole.log(person.age);",
        "instr": "Objects store key-value pairs. Use dot notation."
    },
    {
        "id": 12,
        "title": "Object Destructuring",
        "target": "let person = { name: 'Nora', age: 25 };\nlet { name, age } = person;\nconsole.log(name, age);",
        "instr": "Destructuring extracts properties from objects."
    },
    {
        "id": 13,
        "title": "Spread Operator",
        "target": "let arr1 = [1, 2, 3];\nlet arr2 = [4, 5, 6];\nlet combined = [...arr1, ...arr2];\nconsole.log(combined);",
        "instr": "Spread operator (...) copies or merges arrays."
    },
    {
        "id": 14,
        "title": "Rest Parameters",
        "target": "function sumAll(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}\nconsole.log(sumAll(1, 2, 3, 4));",
        "instr": "Rest parameters collect remaining arguments into an array."
    },

    # ========== 🎯 EXAM 2 (After Lesson 14) ==========
    {
        "id": 15,
        "title": "📝 EXAM 2: Arrays & Objects",
        "is_exam": True,
        "pass_score": 75,
        "exam_number": 2,
        "covers_lessons": "9-14",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write code to filter numbers greater than 10 from [5, 12, 8, 15, 3]",
                "answer": "let numbers = [5, 12, 8, 15, 3];\nlet big = numbers.filter(n => n > 10);"
            },
            {
                "question": "Write code to sum all numbers in [10, 20, 30] using reduce()",
                "answer": "let nums = [10, 20, 30];\nlet sum = nums.reduce((a, b) => a + b, 0);"
            },
            {
                "question": "Create an object called 'user' with properties name='Hind' and age=28",
                "answer": "let user = { name: 'Hind', age: 28 };"
            },
            {
                "question": "Use destructuring to extract name and age from the user object",
                "answer": "let { name, age } = user;"
            },
            {
                "question": "Use spread operator to combine [1,2] and [3,4] into one array",
                "answer": "let combined = [...[1, 2], ...[3, 4]];"
            },
            {
                "question": "Create a function using rest parameters that sums all arguments",
                "answer": "function sumAll(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}"
            }
        ]
    },

    # ========== LEVEL 3: FUNCTIONS & CONTROL FLOW (Lessons 16-21) ==========
    {
        "id": 16,
        "title": "Function Declaration",
        "target": "function greet(name) {\n    return `Hello ${name}`;\n}\nconsole.log(greet('World'));",
        "instr": "Functions are reusable blocks of code."
    },
    {
        "id": 17,
        "title": "Arrow Functions",
        "target": "const add = (a, b) => a + b;\nconst square = x => x * x;\nconsole.log(add(5, 3), square(4));",
        "instr": "Arrow functions provide concise syntax."
    },
    {
        "id": 18,
        "title": "Default Parameters",
        "target": "function multiply(a, b = 1) {\n    return a * b;\n}\nconsole.log(multiply(5), multiply(5, 3));",
        "instr": "Default parameters allow preset values."
    },
    {
        "id": 19,
        "title": "If/Else Statements",
        "target": "let score = 85;\nif (score >= 70) {\n    console.log('Pass');\n} else {\n    console.log('Fail');\n}",
        "instr": "if/else statements control program flow."
    },
    {
        "id": 20,
        "title": "For Loop",
        "target": "let sum = 0;\nfor (let i = 1; i <= 5; i++) {\n    sum += i;\n}\nconsole.log(sum);",
        "instr": "for loops repeat code with an index."
    },
    {
        "id": 21,
        "title": "While Loop",
        "target": "let i = 1;\nwhile (i <= 3) {\n    console.log(i);\n    i++;\n}",
        "instr": "while loops continue while condition is true."
    },

    # ========== 🎯 EXAM 3 (After Lesson 21) ==========
    {
        "id": 22,
        "title": "📝 EXAM 3: Functions & Loops",
        "is_exam": True,
        "pass_score": 80,
        "exam_number": 3,
        "covers_lessons": "16-21",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write a function declaration called 'double' that takes x and returns x * 2",
                "answer": "function double(x) {\n    return x * 2;\n}"
            },
            {
                "question": "Rewrite the double function as an arrow function",
                "answer": "const double = x => x * 2;"
            },
            {
                "question": "Write a function called 'greet' with default parameter name='Guest'",
                "answer": "function greet(name = 'Guest') {\n    return `Hello ${name}`;\n}"
            },
            {
                "question": "Write an if/else statement that prints 'Adult' if age >= 18 else 'Minor'",
                "answer": "if (age >= 18) {\n    console.log('Adult');\n} else {\n    console.log('Minor');\n}"
            },
            {
                "question": "Write a for loop that prints numbers 1 to 5",
                "answer": "for (let i = 1; i <= 5; i++) {\n    console.log(i);\n}"
            },
            {
                "question": "Write a while loop that prints numbers 1 to 3",
                "answer": "let i = 1;\nwhile (i <= 3) {\n    console.log(i);\n    i++;\n}"
            }
        ]
    },

    # ========== LEVEL 4: ADVANCED CONCEPTS (Lessons 23-26) ==========
    {
        "id": 23,
        "title": "Promises",
        "target": "const p = new Promise((resolve) => {\n    setTimeout(() => resolve('Done'), 100);\n});\np.then(result => console.log(result));",
        "instr": "Promises handle asynchronous operations."
    },
    {
        "id": 24,
        "title": "Async/Await",
        "target": "async function getData() {\n    return 'Data loaded';\n}\ngetData().then(console.log);",
        "instr": "async/await makes promises easier to write."
    },
    {
        "id": 25,
        "title": "Classes",
        "target": "class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    speak() {\n        console.log(`${this.name} makes sound`);\n    }\n}\nlet dog = new Animal('Rex');\ndog.speak();",
        "instr": "Classes create blueprints for objects."
    },
    {
        "id": 26,
        "title": "Class Inheritance",
        "target": "class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n}\nclass Dog extends Animal {\n    bark() {\n        console.log(`${this.name} says Woof`);\n    }\n}\nlet d = new Dog('Rex');\nd.bark();",
        "instr": "extends creates inheritance, super() calls parent."
    },

    # ========== 🏆 FINAL EXAM 4 (After Lesson 26) ==========
    {
        "id": 27,
        "title": "🏆 FINAL EXAM 4: Advanced JS",
        "is_exam": True,
        "pass_score": 85,
        "exam_number": 4,
        "covers_lessons": "23-26",
        "exam_type": "question",
        "questions": [
            {
                "question": "Create a Promise that resolves with 'Success' after 100ms",
                "answer": "let p = new Promise((resolve) => {\n    setTimeout(() => resolve('Success'), 100);\n});"
            },
            {
                "question": "Write an async function called 'fetchData' that returns 'Data loaded'",
                "answer": "async function fetchData() {\n    return 'Data loaded';\n}"
            },
            {
                "question": "Create a class called 'Car' with constructor taking 'brand' parameter",
                "answer": "class Car {\n    constructor(brand) {\n        this.brand = brand;\n    }\n}"
            },
            {
                "question": "Create a class 'ElectricCar' that extends 'Car' with method 'charge()'",
                "answer": "class ElectricCar extends Car {\n    charge() {\n        console.log('Charging...');\n    }\n}"
            },
            {
                "question": "Write code to create an instance of ElectricCar and call charge()",
                "answer": "let tesla = new ElectricCar('Tesla');\ntesla.charge();"
            },
            {
                "question": "Write a complete async function that uses await with a Promise",
                "answer": "async function getData() {\n    let result = await new Promise(resolve => setTimeout(() => resolve('Done'), 100));\n    return result;\n}"
            }
        ]
    }
]

TOTAL_JS_LESSONS = len(JAVASCRIPT_LESSONS)
