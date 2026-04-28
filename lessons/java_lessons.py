# Java Lessons with Question-Based Exams

JAVA_LESSONS = [
    # ========== LEVEL 1: BASICS (Lessons 1-7) ==========
    {
        "id": 1,
        "title": "Print Output",
        "target": "System.out.println(\"Hello World\");",
        "instr": "System.out.println() prints text to the console."
    },
    {
        "id": 2,
        "title": "Variables (int, double, String)",
        "target": "int age = 20;\ndouble price = 19.99;\nString name = \"Rinad\";\nSystem.out.println(name + \" \" + age);",
        "instr": "Java variables must have a type before the name."
    },
    {
        "id": 3,
        "title": "Constants (final)",
        "target": "final double PI = 3.14;\nfinal int YEAR = 2024;\nSystem.out.println(PI);",
        "instr": "final makes a variable constant (cannot change)."
    },
    {
        "id": 4,
        "title": "Data Types",
        "target": "String text = \"Hello\";\nint num = 42;\nboolean flag = true;\nSystem.out.println(text + \" \" + num + \" \" + flag);",
        "instr": "Java has: int, double, boolean, char, String."
    },
    {
        "id": 5,
        "title": "String Concatenation",
        "target": "String name = \"Sara\";\nint age = 25;\nSystem.out.println(\"Hello \" + name + \", you are \" + age);",
        "instr": "Use + to combine strings and variables."
    },
    {
        "id": 6,
        "title": "Arrays Basics",
        "target": "String[] fruits = {\"apple\", \"banana\", \"cherry\"};\nSystem.out.println(fruits[0]);",
        "instr": "Arrays store multiple values of the same type."
    },
    {
        "id": 7,
        "title": "For-Each Loop",
        "target": "int[] nums = {1, 2, 3, 4};\nfor (int n : nums) {\n    System.out.println(n);\n}",
        "instr": "Enhanced for loop iterates through arrays."
    },

    # ========== 🎯 EXAM 1 (After Lesson 7) ==========
    {
        "id": 8,
        "title": "📝 EXAM 1: Java Basics",
        "is_exam": True,
        "pass_score": 70,
        "exam_number": 1,
        "covers_lessons": "1-7",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write Java code to declare a String variable called studentName with value \"Ahmed\"",
                "answer": "String studentName = \"Ahmed\";"
            },
            {
                "question": "Write Java code to declare a constant called BIRTH_YEAR with value 2005",
                "answer": "final int BIRTH_YEAR = 2005;"
            },
            {
                "question": "Write Java code to print Hello World",
                "answer": "System.out.println(\"Hello World\");"
            },
            {
                "question": "Write Java code to create an array called colors with values red, green, blue",
                "answer": "String[] colors = {\"red\", \"green\", \"blue\"};"
            },
            {
                "question": "Write Java code to print all numbers in an array using for-each",
                "answer": "for (int n : nums) { System.out.println(n); }"
            },
            {
                "question": "Write Java code to print the first element of an array",
                "answer": "System.out.println(arr[0]);"
            }
        ]
    },
# ========== LEVEL 2: OBJECTS & METHODS (Lessons 9-14) ==========
    {
        "id": 9,
        "title": "Methods",
        "target": "public static int add(int a, int b) {\n    return a + b;\n}",
        "instr": "Methods are reusable blocks of code."
    },
    {
        "id": 10,
        "title": "Method Overloading",
        "target": "int add(int a, int b) { return a + b; }\nint add(int a, int b, int c) { return a + b + c; }",
        "instr": "Overloading allows multiple methods with same name but different parameters."
    },
    {
        "id": 11,
        "title": "Classes",
        "target": "class Person {\n    String name;\n    int age;\n}",
        "instr": "Classes define objects with attributes and methods."
    },
    {
        "id": 12,
        "title": "Constructors",
        "target": "class Person {\n    String name;\n    int age;\n    Person(String n, int a) {\n        name = n;\n        age = a;\n    }\n}",
        "instr": "Constructors initialize object values."
    },
    {
        "id": 13,
        "title": "Objects",
        "target": "Person p = new Person(\"Nora\", 25);\nSystem.out.println(p.name);",
        "instr": "Objects are created using new keyword."
    },
    {
        "id": 14,
        "title": "Static Methods",
        "target": "class MathUtil {\n    static int square(int x) { return x * x; }\n}",
        "instr": "Static methods belong to the class, not objects."
    },

    # ========== 🎯 EXAM 2 (After Lesson 14) ==========
    {
        "id": 15,
        "title": "📝 EXAM 2: Classes & Methods",
        "is_exam": True,
        "pass_score": 75,
        "exam_number": 2,
        "covers_lessons": "9-14",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write a method called multiply that returns a * b",
                "answer": "int multiply(int a, int b) { return a * b; }"
            },
            {
                "question": "Write a constructor for a class Student with name and age",
                "answer": "Student(String n, int a) { name = n; age = a; }"
            },
            {
                "question": "Create an object of Student class",
                "answer": "Student s = new Student(\"Hind\", 28);"
            },
            {
                "question": "Write a static method called cube that returns x * x * x",
                "answer": "static int cube(int x) { return x * x * x; }"
            },
            {
                "question": "Write code to print the name of a Person object",
                "answer": "System.out.println(p.name);"
            },
            {
                "question": "Write two overloaded methods called add",
                "answer": "int add(int a, int b) { return a + b; }\nint add(int a, int b, int c) { return a + b + c; }"
            }
        ]
    },
# ========== LEVEL 3: CONTROL FLOW (Lessons 16-21) ==========
    {
        "id": 16,
        "title": "If/Else",
        "target": "int score = 85;\nif (score >= 70) {\n    System.out.println(\"Pass\");\n} else {\n    System.out.println(\"Fail\");\n}",
        "instr": "if/else controls program decisions."
    },
    {
        "id": 17,
        "title": "Switch Statement",
        "target": "int day = 2;\nswitch(day) {\n    case 1: System.out.println(\"Mon\"); break;\n    case 2: System.out.println(\"Tue\"); break;\n}",
        "instr": "Switch selects code based on value."
    },
    {
        "id": 18,
        "title": "For Loop",
        "target": "for (int i = 1; i <= 5; i++) {\n    System.out.println(i);\n}",
        "instr": "For loops repeat code with index."
    },
    {
        "id": 19,
        "title": "While Loop",
        "target": "int i = 1;\nwhile (i <= 3) {\n    System.out.println(i);\n    i++;\n}",
        "instr": "While loops run while condition is true."
    },
    {
        "id": 20,
        "title": "Do-While Loop",
        "target": "int i = 1;\ndo {\n    System.out.println(i);\n    i++;\n} while (i <= 3);",
        "instr": "Do-while runs at least once."
    },
    {
        "id": 21,
        "title": "Break & Continue",
        "target": "for (int i = 1; i <= 5; i++) {\n    if (i == 3) continue;\n    if (i == 5) break;\n    System.out.println(i);\n}",
        "instr": "continue skips; break stops loop."
    },

    # ========== 🎯 EXAM 3 (After Lesson 21) ==========
    {
        "id": 22,
        "title": "📝 EXAM 3: Control Flow",
        "is_exam": True,
        "pass_score": 80,
        "exam_number": 3,
        "covers_lessons": "16-21",
        "exam_type": "question",
        "questions": [
            {
                "question": "Write an if/else that prints Adult if age >= 18 else Minor",
                "answer": "if (age >= 18) System.out.println(\"Adult\"); else System.out.println(\"Minor\");"
            },
            {
                "question": "Write a switch statement for grade A, B, C",
                "answer": "switch(grade) {\n case 'A': ...; break;\n case 'B': ...; break;\n case 'C': ...; break;\n}"
            },
            {
                "question": "Write a for loop that prints 1 to 5",
                "answer": "for (int i = 1; i <= 5; i++) System.out.println(i);"
            },
            {
                "question": "Write a while loop that prints 1 to 3",
                "answer": "int i = 1;\nwhile (i <= 3) { System.out.println(i); i++; }"
            },
            {
                "question": "Write a do-while loop that prints 1 to 3",
                "answer": "int i = 1;\ndo { System.out.println(i); i++; } while(i <= 3);"
            },
            {
                "question": "Write code using continue to skip number 3",
                "answer": "for (int i = 1; i <= 5; i++) { if (i == 3) continue; System.out.println(i); }"
            }
        ]
    },
# ========== LEVEL 4: OOP ADVANCED (Lessons 23-26) ==========
    {
        "id": 23,
        "title": "Inheritance",
        "target": "class Animal {\n    String name;\n}\nclass Dog extends Animal {\n    void bark() { System.out.println(\"Woof\"); }\n}",
        "instr": "extends allows a class to inherit from another."
    },
    {
        "id": 24,
        "title": "super Keyword",
        "target": "class Animal {\n    Animal() { System.out.println(\"Animal created\"); }\n}\nclass Dog extends Animal {\n    Dog() { super(); System.out.println(\"Dog created\"); }\n}",
        "instr": "super() calls parent constructor."
    },
    {
        "id": 25,
        "title": "Method Overriding",
        "target": "class Animal {\n    void sound() { System.out.println(\"Sound\"); }\n}\nclass Cat extends Animal {\n    @Override\n    void sound() { System.out.println(\"Meow\"); }\n}",
        "instr": "@Override replaces parent method."
    },
    {
        "id": 26,
        "title": "Interfaces",
        "target": "interface Animal {\n    void eat();\n}\nclass Dog implements Animal {\n    public void eat() { System.out.println(\"Eating\"); }\n}",
        "instr": "Interfaces define methods without implementation."
    },

    # ========== 🏆 FINAL EXAM 4 (After Lesson 26) ==========
    {
        "id": 27,
        "title": "🏆 FINAL EXAM 4: Advanced Java",
        "is_exam": True,
        "pass_score": 85,
        "exam_number": 4,
        "covers_lessons": "23-26",
        "exam_type": "question",
        "questions": [
            {
                "question": "Create a class Animal with attribute name",
                "answer": "class Animal { String name; }"
            },
            {
                "question": "Create a class Dog that extends Animal",
                "answer": "class Dog extends Animal {}"
            },
            {
                "question": "Write a constructor in Dog that calls super()",
                "answer": "Dog() { super(); }"
            },
            {
                "question": "Override a method called sound() in Dog",
                "answer": "@Override void sound() { System.out.println(\"Bark\"); }"
            },
            {
                "question": "Create an interface Vehicle with method drive()",
                "answer": "interface Vehicle { void drive(); }"
            },
            {
                "question": "Create a class Car that implements Vehicle",
                "answer": "class Car implements Vehicle { public void drive() { System.out.println(\"Driving\"); } }"
            }
        ]
    }
]

TOTAL_JAVA_LESSONS = len(JAVA_LESSONS)
