# JavaScript Lessons

JAVASCRIPT_LESSONS = [
    {
        "id": 1,
        "title": "Console Output",
        "target": "console.log('Hello World');",
        "instr": "console.log() prints to the browser console."
    },
    {
        "id": 2,
        "title": "Variables (let)",
        "target": "let name = 'Alice';\nlet age = 25;\nconsole.log(name, age);",
        "instr": "let declares variables that can change."
    },
    {
        "id": 3,
        "title": "Constants (const)",
        "target": "const PI = 3.14159;\nconsole.log(PI);",
        "instr": "const declares variables that cannot change."
    },
    {
        "id": 4,
        "title": "Data Types",
        "target": "let str = 'Hello';\nlet num = 42;\nlet bool = true;\nconsole.log(typeof str, typeof num, typeof bool);",
        "instr": "JavaScript has string, number, boolean types."
    },
    {
        "id": 5,
        "title": "Template Literals",
        "target": "let name = 'Bob';\nlet greeting = `Hello ${name}!`;\nconsole.log(greeting);",
        "instr": "Template literals use backticks and ${} for variables."
    },
    {
        "id": 6,
        "title": "Arrays",
        "target": "let fruits = ['apple', 'banana', 'cherry'];\nconsole.log(fruits[0]);\nfruits.push('date');\nconsole.log(fruits);",
        "instr": "Arrays store multiple values. push() adds items."
    },
    {
        "id": 7,
        "title": "Objects",
        "target": "let person = { name: 'Alice', age: 30 };\nconsole.log(person.name);\nconsole.log(person['age']);",
        "instr": "Objects store key-value pairs."
    },
    {
        "id": 8,
        "title": "If Statements",
        "target": "let score = 85;\nif (score >= 70) {\n    console.log('Pass');\n} else {\n    console.log('Fail');\n}",
        "instr": "if/else statements control program flow."
    },
    {
        "id": 9,
        "title": "For Loop",
        "target": "for (let i = 0; i < 5; i++) {\n    console.log(`Number ${i}`);\n}",
        "instr": "for loops repeat code with an index variable."
    },
    {
        "id": 10,
        "title": "While Loop",
        "target": "let count = 0;\nwhile (count < 3) {\n    console.log(count);\n    count++;\n}",
        "instr": "while loops continue while condition is true."
    },
    {
        "id": 11,
        "title": "Functions",
        "target": "function greet(name) {\n    return `Hello ${name}`;\n}\n\nconsole.log(greet('World'));",
        "instr": "Functions are reusable blocks of code."
    },
    {
        "id": 12,
        "title": "Arrow Functions",
        "target": "const add = (a, b) => a + b;\nconsole.log(add(5, 3));",
        "instr": "Arrow functions provide a concise syntax."
    },
    {
        "id": 13,
        "title": "Array Methods: map",
        "target": "let numbers = [1, 2, 3, 4];\nlet doubled = numbers.map(n => n * 2);\nconsole.log(doubled);",
        "instr": "map() transforms each array element."
    },
    {
        "id": 14,
        "title": "Array Methods: filter",
        "target": "let numbers = [1, 2, 3, 4, 5];\nlet evens = numbers.filter(n => n % 2 === 0);\nconsole.log(evens);",
        "instr": "filter() selects elements that match a condition."
    },
    {
        "id": 15,
        "title": "Array Methods: reduce",
        "target": "let numbers = [1, 2, 3, 4];\nlet sum = numbers.reduce((acc, curr) => acc + curr, 0);\nconsole.log(sum);",
        "instr": "reduce() combines array elements into one value."
    },
    {
        "id": 16,
        "title": "Spread Operator",
        "target": "let arr1 = [1, 2, 3];\nlet arr2 = [...arr1, 4, 5];\nconsole.log(arr2);",
        "instr": "Spread operator (...) copies or expands arrays."
    },
    {
        "id": 17,
        "title": "Destructuring",
        "target": "let [a, b] = [10, 20];\nlet {name, age} = {name: 'Bob', age: 25};\nconsole.log(a, b, name, age);",
        "instr": "Destructuring extracts values from arrays/objects."
    },
    {
        "id": 18,
        "title": "Promises",
        "target": "let promise = new Promise((resolve, reject) => {\n    resolve('Success!');\n});\npromise.then(result => console.log(result));",
        "instr": "Promises handle asynchronous operations."
    },
    {
        "id": 19,
        "title": "Async/Await",
        "target": "async function fetchData() {\n    return 'Data loaded';\n}\n\nfetchData().then(console.log);",
        "instr": "async/await makes promises easier to write."
    },
    {
        "id": 20,
        "title": "Classes",
        "target": "class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    \n    speak() {\n        return `${this.name} makes noise`;\n    }\n}\n\nlet dog = new Animal('Rex');\nconsole.log(dog.speak());",
        "instr": "Classes create blueprints for objects."
    }
]