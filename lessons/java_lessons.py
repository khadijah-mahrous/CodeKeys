# Java Lessons

JAVA_LESSONS = [
    {
        "id": 1,
        "title": "Hello World",
        "target": "System.out.println(\"Hello World\");",
        "instr": "System.out.println() prints text with a new line."
    },
    {
        "id": 2,
        "title": "Variables",
        "target": "String name = \"Alice\";\nint age = 25;\nSystem.out.println(name + \" is \" + age);",
        "instr": "Variables have explicit types like String and int."
    },
    {
        "id": 3,
        "title": "Primitive Types",
        "target": "int num = 42;\ndouble pi = 3.14159;\nboolean flag = true;\nchar letter = 'A';\nSystem.out.println(num + \", \" + pi);",
        "instr": "Java has int, double, boolean, char primitive types."
    },
    {
        "id": 4,
        "title": "Arrays",
        "target": "int[] numbers = {1, 2, 3, 4, 5};\nSystem.out.println(numbers[0]);\nSystem.out.println(numbers.length);",
        "instr": "Arrays store multiple values of the same type."
    },
    {
        "id": 5,
        "title": "If-Else",
        "target": "int score = 85;\nif (score >= 70) {\n    System.out.println(\"Pass\");\n} else {\n    System.out.println(\"Fail\");\n}",
        "instr": "if/else statements control program flow."
    },
    {
        "id": 6,
        "title": "For Loop",
        "target": "for (int i = 0; i < 5; i++) {\n    System.out.println(\"Number: \" + i);\n}",
        "instr": "for loops repeat code with an index variable."
    },
    {
        "id": 7,
        "title": "While Loop",
        "target": "int count = 0;\nwhile (count < 3) {\n    System.out.println(count);\n    count++;\n}",
        "instr": "while loops continue while condition is true."
    },
    {
        "id": 8,
        "title": "Methods",
        "target": "public static int add(int a, int b) {\n    return a + b;\n}\n\nSystem.out.println(add(5, 3));",
        "instr": "Methods define reusable code blocks."
    },
    {
        "id": 9,
        "title": "String Methods",
        "target": "String text = \"Hello World\";\nSystem.out.println(text.toUpperCase());\nSystem.out.println(text.length());\nSystem.out.println(text.substring(0, 5));",
        "instr": "Strings have many useful methods."
    },
    {
        "id": 10,
        "title": "Scanner Input",
        "target": "Scanner scanner = new Scanner(System.in);\nSystem.out.print(\"Enter name: \");\nString name = scanner.nextLine();\nSystem.out.println(\"Hello \" + name);",
        "instr": "Scanner reads user input from console."
    },
    {
        "id": 11,
        "title": "ArrayList",
        "target": "import java.util.ArrayList;\nArrayList<String> names = new ArrayList<>();\nnames.add(\"Alice\");\nnames.add(\"Bob\");\nSystem.out.println(names.get(0));",
        "instr": "ArrayList is a dynamic array that can grow."
    },
    {
        "id": 12,
        "title": "HashMap",
        "target": "import java.util.HashMap;\nHashMap<String, Integer> ages = new HashMap<>();\nages.put(\"Alice\", 25);\nages.put(\"Bob\", 30);\nSystem.out.println(ages.get(\"Alice\"));",
        "instr": "HashMap stores key-value pairs."
    },
    {
        "id": 13,
        "title": "Switch Statement",
        "target": "int day = 3;\nswitch (day) {\n    case 1:\n        System.out.println(\"Monday\");\n        break;\n    case 2:\n        System.out.println(\"Tuesday\");\n        break;\n    default:\n        System.out.println(\"Other\");\n}",
        "instr": "switch selects between multiple cases."
    },
    {
        "id": 14,
        "title": "Classes",
        "target": "class Dog {\n    String name;\n    \n    void bark() {\n        System.out.println(name + \" says Woof!\");\n    }\n}\n\nDog myDog = new Dog();\nmyDog.name = \"Rex\";\nmyDog.bark();",
        "instr": "Classes define blueprints for objects."
    },
    {
        "id": 15,
        "title": "Constructors",
        "target": "class Person {\n    String name;\n    int age;\n    \n    Person(String n, int a) {\n        name = n;\n        age = a;\n    }\n}\n\nPerson p = new Person(\"Alice\", 25);",
        "instr": "Constructors initialize new objects."
    },
    {
        "id": 16,
        "title": "Inheritance",
        "target": "class Animal {\n    void sound() {\n        System.out.println(\"Animal makes sound\");\n    }\n}\n\nclass Cat extends Animal {\n    void sound() {\n        System.out.println(\"Meow\");\n    }\n}\n\nCat c = new Cat();\nc.sound();",
        "instr": "Inheritance allows classes to extend others."
    },
    {
        "id": 17,
        "title": "Try-Catch",
        "target": "try {\n    int result = 10 / 0;\n} catch (ArithmeticException e) {\n    System.out.println(\"Cannot divide by zero!\");\n}",
        "instr": "try-catch handles exceptions gracefully."
    },
    {
        "id": 18,
        "title": "File Reading",
        "target": "import java.io.File;\nimport java.util.Scanner;\n\nFile file = new File(\"data.txt\");\nScanner reader = new Scanner(file);\nwhile (reader.hasNextLine()) {\n    System.out.println(reader.nextLine());\n}\nreader.close();",
        "instr": "Scanner can also read files."
    },
    {
        "id": 19,
        "title": "Interfaces",
        "target": "interface Drawable {\n    void draw();\n}\n\nclass Circle implements Drawable {\n    public void draw() {\n        System.out.println(\"Drawing circle\");\n    }\n}\n\nCircle c = new Circle();\nc.draw();",
        "instr": "Interfaces define contracts for classes."
    },
    {
        "id": 20,
        "title": "Static Methods",
        "target": "class MathUtils {\n    public static int square(int x) {\n        return x * x;\n    }\n}\n\nSystem.out.println(MathUtils.square(5));",
        "instr": "Static methods belong to the class, not instances."
    }
]