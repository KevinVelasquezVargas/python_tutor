# -*- coding: utf-8 -*-
# ============================================================================
# Module: globalPlugins/python_tutor/curricula/en.py
# Purpose: Accessible educational curriculum of 32 chapters with conceptual
#          foundations, practical challenges with clean code, and strict validations.
# License: GNU General Public License v3.0 (GPLv3)
# ============================================================================

CURRICULUM = [
    {
        "id": 1,
        "titulo": 'Chapter 1: Computational Thinking and Everyday Algorithms',
        "resumen": 'What does it mean to think like a programmer? Discover what an algorithm is through everyday step-by-step sequences.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: What is an algorithm?',
                "tipo": 'observar',
                "instruccion": 'An algorithm is an ordered and finite series of logical steps to solve a problem or achieve a goal. In daily life, we follow algorithms when cooking or crossing the street. In programming, the computer does not improvise: it strictly executes the sequence you command. Press Control + Enter to hear this first algorithm.',
                "codigo": "print('Step 1: Fill the kettle with water.')\\nprint('Step 2: Heat the water until boiling.')\\nprint('Step 3: Pour into a cup with a tea bag.')\\nprint('Algorithm completed!')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('completed' in res.lower() or 'completado' in res.lower()) and ('kettle' in res.lower() or 'tetera' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: The importance of order',
                "tipo": 'experimentar',
                "instruccion": "If we alter the order of instructions, the final result will make no sense. Add between step 1 and step 2 the line: print('Intermediate step: Place the tea bag.') and press Control + Enter.",
                "codigo": "print('Step 1: Heat the water.')\\n# Modify here: Add between both steps the line:\\n# print('Intermediate step: Place the tea bag.')\\n\\nprint('Step 2: Pour the hot water into the cup.')",
                "pistas": ["Write print('Intermediate step: Place the tea bag.') between the two existing lines."],
                "validar": lambda src, res, ns: ('tea bag' in res.lower() or 'bolsita' in res.lower()) and ('cup' in res.lower() or 'taza' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Hand washing algorithm',
                "tipo": 'desafio',
                "instruccion": "Write a 3-step algorithm for washing hands using three print() statements: 1. 'Turn on the tap and wet your hands', 2. 'Apply soap and scrub', 3. 'Rinse and dry'. Execute with Control + Enter to verify.",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": '1. Turn on the tap and wet your hands\\n2. Apply soap and scrub\\n3. Rinse and dry',
                "pistas": ['Use three independent print statements, each with text inside quotes.', "Example: print('1. Turn on the tap and wet your hands')"],
                "validar": lambda src, res, ns: (('soap' in res.lower() or 'jabón' in res.lower() or 'jabon' in res.lower()) and ('tap' in res.lower() or 'faucet' in res.lower() or 'grifo' in res.lower()) and ('dry' in res.lower() or 'rinse' in res.lower() or 'secar' in res.lower() or 'enjuagar' in res.lower()))
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhat is the most accurate definition of an algorithm?\\n\\nOptions:\\n\\n1. A physical computer component such as the processor.\\n\\n2. An ordered and finite series of logical instructions to solve a problem.\\n\\n3. A computer virus that alters programs.\\n\\nType your option number (1, 2, or 3) into the editor and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['Remember the tea preparation example.'],
                "pregunta": 'What is the most accurate definition of an algorithm?',
                "opciones": ['A physical computer component such as the processor.', 'An ordered and finite series of logical instructions to solve a problem.', 'A computer virus that alters programs.'],
                "correcta": 1,
                "explicacion": 'An algorithm is the logical, step-by-step sequence that describes the solution to a specific problem.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['2']
            }
        ]
    },
    {
        "id": 2,
        "titulo": 'Chapter 2: Basic Architecture: Input, Process, Memory, and Output',
        "resumen": 'Understand how information travels inside a computer: input peripherals, RAM memory, CPU processor, and output channels.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The Input-Process-Output cycle',
                "tipo": 'observar',
                "instruccion": 'Every computer program follows this cycle: Input (keyboard), RAM Memory (where temporary variables reside), CPU Processor (where calculations happen), and Output (screen and screen reader). Run the code to observe this flow in action.',
                "codigo": "# Input and Memory:\\ntool = 'NVDA'\\n# Processing:\\nmessage = 'Accessible environment assisted by: ' + tool\\n# Output:\\nprint(message)",
                "pistas": ['Press Control + Enter to see the output.'],
                "validar": lambda src, res, ns: 'nvda' in res.lower() and ('message' in ns or 'mensaje' in ns)
            },
            {
                "titulo": 'Step 2: Observation: Memory is mutable',
                "tipo": 'experimentar',
                "instruccion": "In RAM memory we can replace the content of a variable at any moment. Observe how the variable 'status' changes and execute with Control + Enter.",
                "codigo": "status = 'Loading data'\\nprint('Initial status:', status)\\n# Modify here: change the assigned value to 'Completed':\\nstatus = 'Ready to code'\\nprint('Final status:', status)",
                "pistas": ['Press Control + Enter to hear the two sequential states.'],
                "validar": lambda src, res, ns: ('completed' in res.lower() or 'completado' in res.lower()) and (ns.get('status') == 'Completed' or ns.get('estado') == 'Completado')
            },
            {
                "titulo": 'Step 3: Practical Challenge: Variables and output',
                "tipo": 'desafio',
                "instruccion": "Create a variable named 'user' with the text 'Student' and display on the console using print: Welcome, Student. Execute with Control + Enter.",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Welcome, Student',
                "pistas": ["Write user = 'Student' on the first line and then print('Welcome,', user)."],
                "validar": lambda src, res, ns: (ns.get('user') == 'Student' or ns.get('usuario') == 'Estudiante') and ('student' in res.lower() or 'estudiante' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhere are variables stored while your Python script is running?\\n\\nOptions:\\n\\n1. In the system RAM memory.\\n\\n2. In the Escape key on the keyboard.\\n\\n3. In the power cord.\\n\\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['It is the primary random-access memory.'],
                "pregunta": 'Where are variables stored while your Python script is running?',
                "opciones": ['In the system RAM memory.', 'In the Escape key on the keyboard.', 'In the power cord.'],
                "correcta": 0,
                "explicacion": 'RAM memory is the fast workspace where active data of running programs resides.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 3,
        "titulo": 'Chapter 3: Boolean Logic: True, False, and Decisions',
        "resumen": 'Learn the binary foundation of every digital decision: the values True and False and the logical operators and, or, and not.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Boolean propositions',
                "tipo": 'observar',
                "instruccion": 'A boolean proposition can only evaluate to True or False. For example: 10 > 5 is True, while 2 > 8 is False. Execute the code to hear these evaluations.',
                "codigo": "print('Is 10 greater than 5?:', 10 > 5)\\nprint('Is 2 greater than 8?:', 2 > 8)",
                "pistas": ['Press Control + Enter to hear True and False.'],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: The operators and, or, and not',
                "tipo": 'experimentar',
                "instruccion": "The 'and' operator requires both conditions to be true. The 'or' operator only requires at least one to be true. Run the code and analyze the result.",
                "codigo": "key = True\\npasscode = False\\n# Modify passcode to True so both conditions are met:\\nprint('Can enter with key AND passcode?:', key and passcode)",
                "pistas": ['Observe how or returns True but and returns False.'],
                "validar": lambda src, res, ns: (ns.get('passcode') is True or ns.get('clave') is True) and 'true' in res.lower()
            },
            {
                "titulo": 'Step 3: Practical Challenge: Access verification',
                "tipo": 'desafio',
                "instruccion": "Create a variable named 'age' with the value 20 and a variable 'has_id' with True. Then create 'authorized = (age >= 18) and has_id'. Print print('Access granted:', authorized).",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Access granted: True',
                "pistas": ['Join both conditions with the and operator.'],
                "validar": lambda src, res, ns: (ns.get('age') == 20 or ns.get('edad') == 20) and (ns.get('authorized') is True or ns.get('autorizado') is True) and 'true' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhat result does the boolean expression: not False produce?\\n\\nOptions:\\n\\n1. True\\n\\n2. False\\n\\n3. None\\n\\nType your option (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['not is the inverse negation operator.'],
                "pregunta": 'What result does the boolean expression: not False produce?',
                "opciones": ['True', 'False', 'None'],
                "correcta": 0,
                "explicacion": "The 'not' operator inverts the logical value: negating False yields True.",
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 4,
        "titulo": 'Chapter 4: Our First Instruction: The print() Function',
        "resumen": 'Learn how to output information to standard output and hear it in your screen reader.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The print() function',
                "tipo": 'observar',
                "instruccion": 'The print() function sends messages to output so the screen reader can speak them. Text must always be enclosed in single or double quotes. Press Control + Enter to hear this initial greeting.',
                "codigo": "print('Hello world from accessible Python!')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('hello world' in res.lower() or 'hola mundo' in res.lower()) and ('accessible' in res.lower() or 'accesible' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Multiple arguments separated by commas',
                "tipo": 'experimentar',
                "instruccion": 'print() can accept multiple text arguments separated by commas. Python will automatically insert a space between each one. Change some text or add a new one and press Control + Enter.',
                "codigo": "print('Python', 'is', 'easy', 'and', 'accessible')\\n# Change 'accessible' to 'powerful' and execute:",
                "pistas": ['Modify or add an argument inside quotes.'],
                "validar": lambda src, res, ns: ('powerful' in res.lower() or 'potente' in res.lower()) and ('easy' in res.lower() or 'fácil' in res.lower() or 'facil' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Your own greeting',
                "tipo": 'desafio',
                "instruccion": "Write a print() instruction that displays exactly the message: 'Learning Python with NVDA'. Press Control + Enter to validate.",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Learning Python with NVDA',
                "pistas": ["Write: print('Learning Python with NVDA') paying attention to quotes and parentheses."],
                "validar": lambda src, res, ns: 'learning python with nvda' in res.lower() or 'aprendiendo python con nvda' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhich function in Python is used to send data to the output and screen reader?\\n\\nOptions:\\n\\n1. print()\\n\\n2. input()\\n\\n3. exit()\\n\\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which function in Python is used to send data to the output and screen reader?',
                "opciones": ['print()', 'input()', 'exit()'],
                "correcta": 0,
                "explicacion": 'print() is the standard output function par excellence.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 5,
        "titulo": 'Chapter 5: Memory Storage: Variables and Assignment',
        "resumen": 'Learn how to store values in memory by assigning them a name with the equals sign (=).',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Creating and assigning variables',
                "tipo": 'observar',
                "instruccion": 'A variable is a name that points to data saved in memory. The equals sign (=) is used to assign. Run the code to observe how text and numbers combine.',
                "codigo": "name = 'Kevin'\\nage = 25\\nprint(name, 'is', age, 'years old')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: (ns.get('age') == 25 or ns.get('edad') == 25) and 'kevin' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Updating a variable value',
                "tipo": 'experimentar',
                "instruccion": 'We can add points to an existing variable and reassign it. Change the value added (50) to another number and press Control + Enter.',
                "codigo": "points = 100\\nprint('Initial score:', points)\\n# Modify here: add 100 instead of 50 to reach 200 points:\\npoints = points + 50\\nprint('Final score:', points)",
                "pistas": ['Change the number 50 to the value you prefer and execute.'],
                "validar": lambda src, res, ns: (ns.get('points') == 200 or ns.get('puntos') == 200) and '200' in res
            },
            {
                "titulo": 'Step 3: Practical Challenge: Language variable',
                "tipo": 'desafio',
                "instruccion": "Create a variable named 'language' with the text 'Python' and then display in the console: print('I am coding in:', language). Press Control + Enter.",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'I am coding in: Python',
                "pistas": ["Assign language = 'Python' and then pass it to print."],
                "validar": lambda src, res, ns: (ns.get('language') == 'Python' or ns.get('lenguaje') == 'Python') and 'python' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhich symbol is used in Python to assign a value to a variable?\\n\\nOptions:\\n\\n1. The equals sign (=)\\n\\n2. The plus sign (+)\\n\\n3. The semicolon (;)\\n\\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['The assignment operator is =.'],
                "pregunta": 'Which symbol is used in Python to assign a value to a variable?',
                "opciones": ['The equals sign (=)', 'The plus sign (+)', 'The semicolon (;)'],
                "correcta": 0,
                "explicacion": 'The single equals sign (=) assigns whatever is on the right into the variable on the left.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 6,
        "titulo": 'Chapter 6: Primitive Data Types: Integers and Floats',
        "resumen": 'Work with integers (int) and floating-point numbers (float) by performing mathematical calculations.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Integers (int) and Floats (float)',
                "tipo": 'observar',
                "instruccion": 'In Python, numbers without a decimal point are integers (int) and those with a decimal point are floating-point numbers (float). Run the code to observe how they multiply.',
                "codigo": "price = 19.50\\nquantity = 3\\ntotal = price * quantity\\nprint('Total to pay:', total)",
                "pistas": ['Press Control + Enter to see the multiplication.'],
                "validar": lambda src, res, ns: (ns.get('total') == 58.5 or ns.get('total') == 58.50) and '58.5' in res
            },
            {
                "titulo": 'Step 2: Observation: Operations with decimals',
                "tipo": 'experimentar',
                "instruccion": 'The ** operator computes exponents (radius squared). Change the radius value to 5 and press Control + Enter to see how the area changes.',
                "codigo": "# Modify the radius to 5 instead of 4:\\nradius = 4\\npi = 3.1416\\narea = pi * (radius ** 2)\\nprint('Area of circle:', round(area, 2))",
                "pistas": ['Change radius = 4 to radius = 5.'],
                "validar": lambda src, res, ns: (ns.get('radius') == 5 or ns.get('radio') == 5) and '78.54' in res
            },
            {
                "titulo": 'Step 3: Practical Challenge: Triangle area calculation',
                "tipo": 'desafio',
                "instruccion": "Create the variables base = 10 and height = 5. Calculate area = (base * height) / 2 and print: print('Triangle area:', area). Execute with Control + Enter.",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Triangle area: 25.0',
                "pistas": ['Remember to use the forward slash / for division.'],
                "validar": lambda src, res, ns: (ns.get('base') == 10) and (ns.get('height') == 5 or ns.get('altura') == 5) and ns.get('area') == 25.0 and '25' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhat is the Python numeric data type with a decimal part called?\\n\\nOptions:\\n\\n1. float\\n\\n2. int\\n\\n3. bool\\n\\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ["Short for 'floating point'."],
                "pregunta": 'What is a number with a decimal point called in Python?',
                "opciones": ['float', 'int', 'bool'],
                "correcta": 0,
                "explicacion": 'float represents floating-point numbers (decimals).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 7,
        "titulo": 'Chapter 7: Strings: Quotes and Concatenation',
        "resumen": 'Manipulate text in Python using single quotes, double quotes, and modern formatted strings (f-strings).',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Concatenation with + and f-strings',
                "tipo": 'observar',
                "instruccion": "Strings (str) can be joined with the + operator or by using f-strings by placing an 'f' before the quotes and inserting variables inside curly braces {}. Run to see both methods.",
                "codigo": "name = 'Laura'\\ngreeting = f'Hello {name}, welcome to Python.'\\nprint(greeting)",
                "pistas": ['Press Control + Enter to see text interpolation.'],
                "validar": lambda src, res, ns: 'laura' in res.lower() and ('welcome' in res.lower() or 'bienvenida' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Text repetition with *',
                "tipo": 'experimentar',
                "instruccion": 'When multiplying text by a number, Python repeats it. Change the multiplier 3 to 5 and press Control + Enter.',
                "codigo": "cheer = 'Bravo! '\\n# Modify the multiplier 3 to 5:\\nprint(cheer * 3)",
                "pistas": ['Change * 3 to * 5.'],
                "validar": lambda src, res, ns: res.lower().count('bravo') >= 5
            },
            {
                "titulo": 'Step 3: Practical Challenge: Creating an f-string',
                "tipo": 'desafio',
                "instruccion": "Create a variable city = 'Bogota' and country = 'Colombia'. Use an f-string to print exactly: print(f'Location: {city}, {country}').",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Location: Bogota, Colombia',
                "pistas": ['Place f before the quotes and the variables inside {city} and {country}.'],
                "validar": lambda src, res, ns: (('bogotá' in res.lower() or 'bogota' in res.lower()) and 'colombia' in res.lower() and ('location' in res.lower() or 'ubicación' in res.lower() or 'ubicacion' in res.lower()))
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhich letter precedes the quotes to create a modern formatted string in Python?\\n\\nOptions:\\n\\n1. The letter f\\n\\n2. The letter p\\n\\n3. The letter s\\n\\nType your option (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ["f stands for 'format'."],
                "pregunta": 'Which letter precedes the quotes to create an f-string?',
                "opciones": ['The letter f', 'The letter p', 'The letter s'],
                "correcta": 0,
                "explicacion": 'The letter f turns a string into an f-string (formatted string literal).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 8,
        "titulo": 'Chapter 8: User Interaction: Input with input()',
        "resumen": 'Learn how to capture data typed by the user on the keyboard and convert it using int() or float().',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The input() function',
                "tipo": 'observar',
                "instruccion": 'input() allows receiving data from the user. Remember that input() ALWAYS returns a string (str). If you need to perform mathematical calculations, you must convert it with int(). Run the code to observe the conversion.',
                "codigo": "age_text = '25'\\nage_number = int(age_text)\\nprint('Converted numeric age:', age_number)\\nprint('Double your age is:', age_number * 2)",
                "pistas": ['Press Control + Enter to see the conversion.'],
                "validar": lambda src, res, ns: (ns.get('age_number') == 25 or ns.get('edad_numero') == 25) and '25' in res
            },
            {
                "titulo": 'Step 2: Observation: input with prompt',
                "tipo": 'experimentar',
                "instruccion": "Observe how informative text is passed to input(). Modify the greeting to say 'Welcome, Anna!' and press Control + Enter.",
                "codigo": "name = 'Anna'\\n# Modify the greeting to say 'Welcome, Anna!':\\nprint(f'Hello {name}! Welcome to interactive learning.')",
                "pistas": ["Change the greeting text to say 'Welcome, Anna!' and execute."],
                "validar": lambda src, res, ns: ('welcome' in res.lower() or 'bienvenida' in res.lower()) and ('anna' in res.lower() or 'ana' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Conversion and calculation',
                "tipo": 'desafio',
                "instruccion": "You have the variable age_text = '20'. Convert it to an integer using int(age_text) and save the result in 'age'. Then display: print('Next year you will be:', age + 1).",
                "codigo": '# Write your code here to solve the challenge:\\n\\n',
                "salida_esperada": 'Next year you will be: 21',
                "pistas": ['Use int(age_text) for the conversion.'],
                "validar": lambda src, res, ns: (ns.get('age') == 20 or ns.get('edad') == 20) and ('21' in res or ns.get('next') == 21 or ns.get('proximo') == 21 or ns.get('next_age') == 21)
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\\n\\nWhat data type does the Python input() function return by default?\\n\\nOptions:\\n\\n1. Always a string (str)\\n\\n2. An integer (int)\\n\\n3. A boolean (bool)\\n\\nType your option (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\\n',
                "pistas": ['Everything entered through the keyboard is initially read as text.'],
                "pregunta": 'What data type does input() return by default?',
                "opciones": ['Always a string (str)', 'An integer (int)', 'A boolean (bool)'],
                "correcta": 0,
                "explicacion": 'input() always returns a string (str), which is why int() or float() is required for numerical operations.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 9,
        "titulo": 'Chapter 9: Comparison Operators and Conditional Expressions',
        "resumen": 'Compare values using >, <, >=, <=, ==, and != to make decisions in your programs.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Relational operators',
                "tipo": 'observar',
                "instruccion": 'Relational operators compare two values: > (greater than), < (less than), >= (greater or equal), <= (less or equal), == (equal), and != (not equal). Run the code to observe their boolean results.',
                "codigo": "x = 15\ny = 20\nprint('Is x less than y?:', x < y)\nprint('Is x equal to y?:', x == y)\nprint('Is x different from y?:', x != y)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'true' in res.lower() and 'false' in res.lower() and ns.get('x') == 15
            },
            {
                "titulo": 'Step 2: Observation: Comparing strings',
                "tipo": 'experimentar',
                "instruccion": 'You can also compare text strings with ==. If you change the entered password to match the real password exactly, the result will change to True. Modify and execute.',
                "codigo": "entered_pass = 'test'\nreal_pass = 'secret'\n# Modify entered_pass to match real_pass exactly:\nprint('Correct password?:', entered_pass == real_pass)",
                "pistas": ["Change entered_pass to 'secret' and press Control + Enter."],
                "validar": lambda src, res, ns: (ns.get('entered_pass') == 'secret' or ns.get('clave_ingresada') == 'secreta' or ns.get('clave_ingresada') == 'secret') and 'true' in res.lower()
            },
            {
                "titulo": 'Step 3: Practical Challenge: Passing grade',
                "tipo": 'desafio',
                "instruccion": "Create a variable score = 85. Print in the console: print('Passed with 70 or more?:', score >= 70). Press Control + Enter.",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Passed with 70 or more?: True',
                "pistas": ['Use the >= (greater than or equal to) operator.', "Example: score = 85 followed by print('Passed with 70 or more?:', score >= 70)"],
                "validar": lambda src, res, ns: (ns.get('score') == 85 or ns.get('puntos') == 85) and 'true' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich operator is used in Python to compare if two values are exactly equal?\n\nOptions:\n\n1. Double equals sign (==)\n\n2. Single equals sign (=)\n\n3. Exclamation mark (!)\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Do not confuse assignment (=) with equality comparison.'],
                "pregunta": 'Which operator compares if two values are equal in Python?',
                "opciones": ['Double equals sign (==)', 'Single equals sign (=)', 'Exclamation mark (!)'],
                "correcta": 0,
                "explicacion": 'The double equals sign (==) checks for equality, while the single equals sign (=) assigns values.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 10,
        "titulo": 'Chapter 10: Basic Branching: The if Statement and PEP 8 Indentation',
        "resumen": 'Execute code blocks conditionally using if and mandatory 4-space indentation.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The if statement and 4 spaces',
                "tipo": 'observar',
                "instruccion": 'The if statement evaluates a condition ending with a colon (:). Indented lines underneath must have 4 spaces of indentation (Tab key). Run the code to observe how the condition is met.',
                "codigo": "temperature = 30\nif temperature > 25:\n    print('It is hot, turn on the fan.')\nprint('End of analysis.')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('fan' in res.lower() or 'ventilador' in res.lower()) and (ns.get('temperature') == 30 or ns.get('temperatura') == 30)
            },
            {
                "titulo": 'Step 2: Observation: When the condition is not met',
                "tipo": 'experimentar',
                "instruccion": 'If the condition is False, the indented block is skipped. Change temperature to 15 and press Control + Enter to hear how the block is bypassed.',
                "codigo": "# Modify temperature to 15 to check that the if block does not execute:\ntemperature = 30\nif temperature > 25:\n    print('It is hot.')\nprint('End of program.')",
                "pistas": ['Change temperature = 15 and press Control + Enter.'],
                "validar": lambda src, res, ns: (ns.get('temperature') == 15 or ns.get('temperatura') == 15) and ('hot' not in res.lower() and 'calor' not in res.lower()) and ('end' in res.lower() or 'fin' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Time-based greeting with if',
                "tipo": 'desafio',
                "instruccion": "Create a variable hour = 14. Write an if block that checks if hour >= 12, and inside prints with 4 spaces of indentation: print('Good afternoon').",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Good afternoon',
                "pistas": ['Do not forget the colon (:) at the end of the if line.', 'Use 4 spaces or press Tab for indentation.'],
                "validar": lambda src, res, ns: (ns.get('hour') == 14 or ns.get('hora') == 14) and ('good afternoon' in res.lower() or 'buenas tardes' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nHow many spaces does the official PEP 8 style guide recommend for each indentation level in Python?\n\nOptions:\n\n1. 4 spaces\n\n2. 1 space\n\n3. 10 spaces\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['It is the universal Python standard.'],
                "pregunta": 'How many spaces does PEP 8 recommend for indentation?',
                "opciones": ['4 spaces', '1 space', '10 spaces'],
                "correcta": 0,
                "explicacion": 'PEP 8 specifies a standard of 4 spaces per indentation level.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 11,
        "titulo": 'Chapter 11: Multiple Alternatives: elif and else Blocks',
        "resumen": 'Handle multiple possible paths by chaining conditions with elif and providing a default case with else.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The elif and else blocks',
                "tipo": 'observar',
                "instruccion": 'When you have more than two branches, use elif for subsequent conditions and else as the catch-all fallback. Run the code to observe the logic.',
                "codigo": "grade = 7\nif grade >= 9:\n    print('Excellent')\nelif grade >= 5:\n    print('Passed')\nelse:\n    print('Failed')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('passed' in res.lower() or 'aprobado' in res.lower()) and (ns.get('grade') == 7 or ns.get('nota') == 7)
            },
            {
                "titulo": 'Step 2: Observation: Modifying the grade',
                "tipo": 'experimentar',
                "instruccion": "Modify the grade to 10 so that the 'Excellent' condition triggers, and press Control + Enter.",
                "codigo": "# Modify grade to 10 so that the 'Excellent' condition triggers:\ngrade = 4\nif grade >= 9:\n    print('Excellent')\nelif grade >= 5:\n    print('Passed')\nelse:\n    print('Needs improvement')",
                "pistas": ['Change grade = 10 and press Control + Enter.'],
                "validar": lambda src, res, ns: (ns.get('grade', 0) >= 9 or ns.get('nota', 0) >= 9) and ('excellent' in res.lower() or 'excelente' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Interactive grade classifier',
                "tipo": 'desafio',
                "instruccion": "Create a variable grade = 8. Write an if/elif/else structure: if grade >= 9 print 'Excellent', elif grade >= 5 print 'Passed', and else print 'Failed'.",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Passed',
                "pistas": ['Create grade = 8 first.', "Check elif grade >= 5: print('Passed')"],
                "validar": lambda src, res, ns: (ns.get('grade') == 8 or ns.get('nota') == 8) and ('passed' in res.lower() or 'aprobado' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich conditional block executes if none of the preceding conditions were true?\n\nOptions:\n\n1. The else block\n\n2. The if block\n\n3. The while block\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['It is the default catch-all branch.'],
                "pregunta": 'Which conditional block executes if none of the preceding conditions were true?',
                "opciones": ['The else block', 'The if block', 'The while block'],
                "correcta": 0,
                "explicacion": 'else executes as the default fallback when all preceding if and elif conditions evaluate to False.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 12,
        "titulo": 'Chapter 12: Ordered Collections: Introduction to Lists',
        "resumen": 'Store multiple items in an ordered sequence using square brackets [] and access them via zero-based indices.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Creating and indexing lists',
                "tipo": 'observar',
                "instruccion": 'Lists store multiple items in order. Elements are enclosed in square brackets [] and accessed by their index starting at 0. Run the code to observe.',
                "codigo": "fruits = ['apple', 'pear', 'banana']\nprint('First fruit:', fruits[0])\nprint('Second fruit:', fruits[1])",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('apple' in res.lower() or 'manzana' in res.lower()) and ('pear' in res.lower() or 'pera' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Modifying a list element',
                "tipo": 'experimentar',
                "instruccion": "Lists are mutable. You can replace an element at any index. Modify index 0 to 'strawberry' and press Control + Enter.",
                "codigo": "fruits = ['apple', 'pear', 'banana']\n# Modify the element at index 0 by assigning 'strawberry':\nfruits[0] = 'strawberry'\nprint('Modified fruit:', fruits[0])",
                "pistas": ["Change fruits[0] = 'strawberry' and press Control + Enter."],
                "validar": lambda src, res, ns: (('strawberry' in res.lower() or 'fresa' in res.lower()) and ((ns.get('fruits') and ns.get('fruits')[0] in ('strawberry', 'fresa')) or (ns.get('frutas') and ns.get('frutas')[0] in ('strawberry', 'fresa'))))
            },
            {
                "titulo": 'Step 3: Practical Challenge: Shopping list',
                "tipo": 'desafio',
                "instruccion": "Create a list named 'groceries' with 'bread', 'milk', and 'eggs'. Print the first element using groceries[0].",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'bread',
                "pistas": ["Create groceries = ['bread', 'milk', 'eggs'] and print(groceries[0])."],
                "validar": lambda src, res, ns: ((isinstance(ns.get('groceries'), list) and len(ns.get('groceries')) >= 3) or (isinstance(ns.get('compras'), list) and len(ns.get('compras')) >= 3)) and ('bread' in res.lower() or 'pan' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the index of the first element of a list in Python?\n\nOptions:\n\n1. Index 0\n\n2. Index 1\n\n3. Index -1\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Python uses zero-based indexing.'],
                "pregunta": 'What is the index of the first element of a list in Python?',
                "opciones": ['Index 0', 'Index 1', 'Index -1'],
                "correcta": 0,
                "explicacion": 'In Python, sequence indexing always starts at zero (0).',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 13,
        "titulo": 'Chapter 13: Essential List Methods (append, remove, pop, len)',
        "resumen": 'Add, remove, and count elements in dynamic Python lists.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: append() and len()',
                "tipo": 'observar',
                "instruccion": 'append() adds an element to the end of a list, and len() returns the total count of elements. Run the code to observe.',
                "codigo": "tasks = ['read', 'code']\ntasks.append('relax')\nprint('Total tasks:', len(tasks))\nprint('List:', tasks)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('relax' in res.lower() or 'descansar' in res.lower()) and (len(ns.get('tasks', [])) == 3 or len(ns.get('tareas', [])) == 3)
            },
            {
                "titulo": 'Step 2: Observation: remove()',
                "tipo": 'experimentar',
                "instruccion": "remove() searches for an item by value and deletes its first occurrence. Modify the code to remove 'relax' instead of 'read' and press Control + Enter.",
                "codigo": "tasks = ['read', 'code', 'relax']\n# Modify to remove 'relax' instead of 'read':\ntasks.remove('relax')\nprint('Remaining tasks:', tasks)",
                "pistas": ["Change tasks.remove('read') to tasks.remove('relax')."],
                "validar": lambda src, res, ns: ('relax' not in (ns.get('tasks') or []) and 'read' in (ns.get('tasks') or [])) or ('descansar' not in (ns.get('tareas') or []) and 'leer' in (ns.get('tareas') or []))
            },
            {
                "titulo": 'Step 3: Practical Challenge: Adding colors',
                "tipo": 'desafio',
                "instruccion": "Create a list colors = ['red', 'green']. Add 'blue' with append() and display the total count with print('Total colors:', len(colors)).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Total colors: 3',
                "pistas": ["Create colors = ['red', 'green'], call colors.append('blue'), then print('Total colors:', len(colors))."],
                "validar": lambda src, res, ns: (isinstance(ns.get('colors'), list) and 'blue' in ns.get('colors') and ('3' in res or len(ns.get('colors')) == 3)) or (isinstance(ns.get('colores'), list) and 'azul' in ns.get('colores') and ('3' in res or len(ns.get('colores')) == 3))
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich method adds a new element to the end of a list in Python?\n\nOptions:\n\n1. append()\n\n2. delete()\n\n3. add()\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which method adds a new element to the end of a list?',
                "opciones": ['append()', 'delete()', 'add()'],
                "correcta": 0,
                "explicacion": 'append() appends an element to the end of the list.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 14,
        "titulo": 'Chapter 14: Repetition and Automation: The for Loop and range()',
        "resumen": 'Automate repetitive tasks by iterating through number sequences and lists with for.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The for loop with range()',
                "tipo": 'observar',
                "instruccion": 'The for loop repeats a block of code for each item in a sequence. range(1, 4) produces numbers 1, 2, and 3. Run the code to observe.',
                "codigo": "for i in range(1, 4):\n    print('Number:', i)\nprint('End of loop')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and ('end of loop' in res.lower() or 'fin del bucle' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Iterating over a list',
                "tipo": 'experimentar',
                "instruccion": "You can iterate directly over list elements. Modify by adding 'canary' to the list so it iterates 4 times, and press Control + Enter.",
                "codigo": "pets = ['dog', 'cat', 'parrot']\n# Modify by adding 'canary' to the list to iterate 4 times:\nfor pet in pets:\n    print('Pet:', pet)",
                "pistas": ["Add 'canary' to the pets list."],
                "validar": lambda src, res, ns: ('canary' in res.lower() and len(ns.get('pets', [])) >= 4) or ('canario' in res.lower() and len(ns.get('animales', [])) >= 4)
            },
            {
                "titulo": 'Step 3: Practical Challenge: Counting loop',
                "tipo": 'desafio',
                "instruccion": "Write a for loop that iterates through range(1, 6) and prints each number: print('Counting:', number).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Counting: 1\nCounting: 2\nCounting: 3\nCounting: 4\nCounting: 5',
                "pistas": ['Use for number in range(1, 6): and print with 4 spaces of indentation.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in range(1, 6))
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat numbers does the function range(1, 5) produce in a for loop?\n\nOptions:\n\n1. Numbers from 1 to 4\n\n2. Numbers from 1 to 5\n\n3. An empty list\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['The stop value is exclusive.'],
                "pregunta": 'What numbers does range(1, 5) produce in a for loop?',
                "opciones": ['Numbers from 1 to 4', 'Numbers from 1 to 5', 'An empty list'],
                "correcta": 0,
                "explicacion": 'range(start, stop) generates numbers up to stop - 1.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 15,
        "titulo": 'Chapter 15: Conditional Repetition: The while Loop',
        "resumen": 'Repeat blocks of instructions as long as a boolean condition remains true.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The while loop',
                "tipo": 'observar',
                "instruccion": 'A while loop continues running as long as its condition is True. Remember to update the variable inside the loop to avoid an infinite loop. Run the code to observe.',
                "codigo": "counter = 1\nwhile counter <= 3:\n    print('Lap:', counter)\n    counter = counter + 1\nprint('Loop finished')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and (ns.get('counter') == 4 or ns.get('contador') == 4)
            },
            {
                "titulo": 'Step 2: Observation: Modifying the initial condition',
                "tipo": 'experimentar',
                "instruccion": 'Change the initial energy to 5 instead of 3, and press Control + Enter.',
                "codigo": "# Modify initial energy to 5 instead of 3:\nenergy = 5\nwhile energy > 0:\n    print('Remaining energy:', energy)\n    energy = energy - 1\nprint('Out of energy')",
                "pistas": ['Change energy = 5 and press Control + Enter.'],
                "validar": lambda src, res, ns: '5' in res and ('out of energy' in res.lower() or 'sin energía' in res.lower() or 'sin energia' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Step counter',
                "tipo": 'desafio',
                "instruccion": "Create counter = 1. Write a while loop that while counter <= 3 prints print('Step:', counter) and increments counter by 1.",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Step: 1\nStep: 2\nStep: 3',
                "pistas": ['Initialize counter = 1.', 'In the loop body, write counter = counter + 1.'],
                "validar": lambda src, res, ns: all(str(i) in res for i in (1, 2, 3)) and (ns.get('counter', 0) > 3 or ns.get('contador', 0) > 3)
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat crucial precaution must be taken when programming a while loop?\n\nOptions:\n\n1. Ensure the condition changes to avoid an infinite loop\n\n2. Put a semicolon at the end\n\n3. Use triple quotes\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What crucial precaution must be taken when programming a while loop?',
                "opciones": ['Ensure the condition changes to avoid an infinite loop', 'Put a semicolon at the end', 'Use triple quotes'],
                "correcta": 0,
                "explicacion": 'If the loop condition never becomes False, the loop runs infinitely, freezing the program.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 16,
        "titulo": 'Chapter 16: Key-Value Collections: Dictionaries in Python',
        "resumen": 'Associate pairs of information using curly braces {} with keys and values.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Creating and accessing dictionaries',
                "tipo": 'observar',
                "instruccion": 'Dictionaries store data in key: value pairs enclosed in curly braces {}. Access values by referencing their key in square brackets. Run the code to observe.',
                "codigo": "contact = {'name': 'Carlos', 'phone': '555-1234'}\nprint('Name:', contact['name'])\nprint('Phone:', contact['phone'])",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'carlos' in res.lower() and '555-1234' in res
            },
            {
                "titulo": 'Step 2: Observation: Adding and updating keys',
                "tipo": 'experimentar',
                "instruccion": "You can add or update key-value pairs by assigning to dictionary[key]. Modify the city to 'Valencia' and press Control + Enter.",
                "codigo": "contact = {'name': 'Carlos', 'phone': '555-1234'}\n# Modify the city here to 'Valencia':\ncontact['city'] = 'Valencia'\nprint('Full contact:', contact)",
                "pistas": ["Change contact['city'] = 'Valencia' and press Control + Enter."],
                "validar": lambda src, res, ns: ((ns.get('contact', {}).get('city') == 'Valencia' or ns.get('contacto', {}).get('ciudad') == 'Valencia') and 'valencia' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Price lookup',
                "tipo": 'desafio',
                "instruccion": "Create a dictionary named 'prices' with 'apple': 2 and 'pear': 3. Print: print('Apple price:', prices['apple']).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Apple price: 2',
                "pistas": ["Define prices = {'apple': 2, 'pear': 3} and print(prices['apple'])."],
                "validar": lambda src, res, ns: ((isinstance(ns.get('prices'), dict) and ns.get('prices').get('apple') == 2) or (isinstance(ns.get('precios'), dict) and ns.get('precios').get('manzana') == 2)) and '2' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich delimiter is used to declare dictionaries in Python?\n\nOptions:\n\n1. Curly braces {}\n\n2. Square brackets []\n\n3. Parentheses ()\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which delimiter is used to declare dictionaries in Python?',
                "opciones": ['Curly braces {}', 'Square brackets []', 'Parentheses ()'],
                "correcta": 0,
                "explicacion": 'Dictionaries are declared using curly braces {} containing key: value pairs.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 17,
        "titulo": 'Chapter 17: Tuples and Sets: Immutability and Unique Elements',
        "resumen": 'Use tuples for fixed data that cannot change and sets for collections without duplicates.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Tuples',
                "tipo": 'observar',
                "instruccion": 'Tuples are ordered, immutable collections defined with parentheses (). Once created, their items cannot be modified or reordered. Run the code to observe.',
                "codigo": "point = (10, 20)\nprint('X coordinate:', point[0])\nprint('Y coordinate:', point[1])",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: '10' in res and '20' in res and (isinstance(ns.get('point'), tuple) or isinstance(ns.get('punto'), tuple))
            },
            {
                "titulo": 'Step 2: Observation: Sets and uniqueness',
                "tipo": 'experimentar',
                "instruccion": 'Sets are unordered collections with no duplicate items, defined with curly braces {}. Modify the set by adding the number 5, and press Control + Enter.',
                "codigo": "# Modify the set by adding the number 5:\nnumbers = {1, 2, 2, 3, 3, 4, 5}\nprint('Set without duplicates:', numbers)",
                "pistas": ['Add 5 into the curly braces and press Control + Enter.'],
                "validar": lambda src, res, ns: (isinstance(ns.get('numbers'), set) and 5 in ns.get('numbers')) or (isinstance(ns.get('numeros'), set) and 5 in ns.get('numeros'))
            },
            {
                "titulo": 'Step 3: Practical Challenge: Coordinate tuple',
                "tipo": 'desafio',
                "instruccion": "Create a tuple named 'coordinates' with the values (50, 100). Print: print('Coordinates:', coordinates).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Coordinates: (50, 100)',
                "pistas": ['Use parentheses () with comma-separated numbers: coordinates = (50, 100).'],
                "validar": lambda src, res, ns: ((isinstance(ns.get('coordinates'), tuple) and ns.get('coordinates') == (50, 100)) or (isinstance(ns.get('coordenadas'), tuple) and ns.get('coordenadas') == (50, 100))) and '50' in res and '100' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the main difference between a tuple and a list?\n\nOptions:\n\n1. Tuples are immutable (cannot be modified)\n\n2. Tuples cannot contain numbers\n\n3. Tuples only hold one element\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is the main difference between a tuple and a list?',
                "opciones": ['Tuples are immutable (cannot be modified)', 'Tuples cannot contain numbers', 'Tuples only hold one element'],
                "correcta": 0,
                "explicacion": 'Tuples are immutable once created, guaranteeing data integrity and safety.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 18,
        "titulo": 'Chapter 18: Custom Functions: Declaration with def and Parameters',
        "resumen": 'Package reusable instructions by giving them their own name with def.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Defining and calling a function',
                "tipo": 'observar',
                "instruccion": "The 'def' keyword defines a function followed by its name, parameter parentheses, and a colon (:). Run the code to observe.",
                "codigo": "def greet(name):\n    print(f'Hello, {name}! Welcome to functions.')\n\ngreet('Elena')\ngreet('Marcus')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: (callable(ns.get('greet')) or callable(ns.get('saludar'))) and ('elena' in res.lower() or 'marcus' in res.lower() or 'lucía' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Parameters and calculations',
                "tipo": 'experimentar',
                "instruccion": "Modify the call to calculate double of 15, and press Control + Enter.",
                "codigo": "def double(num):\n    print('The double is:', num * 2)\n\n# Modify the call to calculate the double of 15:\ndouble(15)",
                "pistas": ['Change the argument from 8 to 15 and press Control + Enter.'],
                "validar": lambda src, res, ns: '30' in res or 'the double is: 30' in res.lower() or 'el doble es: 30' in res.lower()
            },
            {
                "titulo": 'Step 3: Practical Challenge: Adding numbers function',
                "tipo": 'desafio',
                "instruccion": "Define a function named 'add_numbers(a, b)' that prints: print('Result:', a + b). Then call it with add_numbers(5, 7).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Result: 12',
                "pistas": ["Define def add_numbers(a, b):, indent 4 spaces, print('Result:', a + b), and call add_numbers(5, 7)."],
                "validar": lambda src, res, ns: (callable(ns.get('add_numbers')) or callable(ns.get('sumar'))) and ('12' in res or 'result: 12' in res.lower() or 'resultado: 12' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich keyword is used to define a new function in Python?\n\nOptions:\n\n1. def\n\n2. function\n\n3. fn\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Short for define.'],
                "pregunta": 'Which keyword is used to define a new function in Python?',
                "opciones": ['def', 'function', 'fn'],
                "correcta": 0,
                "explicacion": "The keyword 'def' (short for define) declares a function in Python.",
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 19,
        "titulo": 'Chapter 19: Returning Results: The return Statement and Scope',
        "resumen": 'Return computed values to the caller code and understand the local scope of variables.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The return statement',
                "tipo": 'observar',
                "instruccion": "The 'return' statement terminates a function execution and sends the calculated value back to the caller. Run the code to observe.",
                "codigo": "def multiply(a, b):\n    return a * b\n\nresult = multiply(4, 5)\nprint('Result obtained with return:', result)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: (ns.get('result') == 20 or ns.get('resultado') == 20) and (callable(ns.get('multiply')) or callable(ns.get('multiplicar')))
            },
            {
                "titulo": 'Step 2: Observation: Returning boolean values',
                "tipo": 'experimentar',
                "instruccion": "Functions can return boolean True or False. Modify the tested age to 16 and press Control + Enter.",
                "codigo": "def is_adult(age):\n    return age >= 18\n\n# Modify the tested age to 16:\nprint('Can vote?:', is_adult(16))",
                "pistas": ['Change the tested age to 16.'],
                "validar": lambda src, res, ns: 'false' in res.lower() and (callable(ns.get('is_adult')) or callable(ns.get('es_mayor_de_edad')))
            },
            {
                "titulo": 'Step 3: Practical Challenge: Square function',
                "tipo": 'desafio',
                "instruccion": "Define a function 'square(n)' that returns n * n using return. Store square(6) in variable 'res' and print: print('The square is:', res).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'The square is: 36',
                "pistas": ["def square(n): return n * n, then res = square(6), print('The square is:', res)"],
                "validar": lambda src, res, ns: ((callable(ns.get('square')) and ns.get('square')(6) == 36) or (callable(ns.get('cuadrado')) and ns.get('cuadrado')(6) == 36)) and '36' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat happens when a function executes the return statement?\n\nOptions:\n\n1. It finishes the function and hands the result back to the caller\n\n2. It prints the value to the screen\n\n3. It reboots the computer\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What happens when a function executes the return statement?',
                "opciones": ['It finishes the function and hands the result back to the caller', 'It prints the value to the screen', 'It reboots the computer'],
                "correcta": 0,
                "explicacion": 'return concludes the execution of a function and passes the result back to the calling code.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 20,
        "titulo": 'Chapter 20: Professional Error Handling: try, except, and finally',
        "resumen": 'Prevent unexpected crashes by intercepting and handling exceptions gracefully.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Catching ZeroDivisionError',
                "tipo": 'observar',
                "instruccion": 'When an error occurs inside a try block, execution jumps immediately to the matching except block without crashing the program. Run the code to observe.',
                "codigo": "try:\n    divisor = 0\n    result = 10 / divisor\n    print(result)\nexcept ZeroDivisionError:\n    print('Notice: Cannot divide by zero.')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('cannot divide by zero' in res.lower() or 'no se puede dividir' in res.lower() or 'no es posible dividir' in res.lower() or 'zero' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Catching ValueError',
                "tipo": 'experimentar',
                "instruccion": "Modify the text '123' to 'abc' so that int('abc') triggers a ValueError, and press Control + Enter.",
                "codigo": "try:\n    # Modify '123' to 'abc' so ValueError is triggered:\n    number = int('abc')\n    print('Converted number:', number)\nexcept ValueError:\n    print('Notice: Text does not contain valid digits.')",
                "pistas": ["Change '123' to 'abc' and press Control + Enter."],
                "validar": lambda src, res, ns: ('notice' in res.lower() or 'aviso' in res.lower()) and ('digits' in res.lower() or 'dígitos' in res.lower() or 'valid' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Safe division',
                "tipo": 'desafio',
                "instruccion": "Write a try block where you divide 20 by 0, and in the except ZeroDivisionError block print: print('Error caught successfully').",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Error caught successfully',
                "pistas": ["try:\n    x = 20 / 0\nexcept ZeroDivisionError:\n    print('Error caught successfully')"],
                "validar": lambda src, res, ns: ('caught successfully' in res.lower() or 'capturado con éxito' in res.lower() or 'capturado con exito' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the purpose of the except clause in Python?\n\nOptions:\n\n1. To catch specific errors and prevent the program from crashing\n\n2. To create loops\n\n3. To delete files\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is the purpose of the except clause in Python?',
                "opciones": ['To catch specific errors and prevent the program from crashing', 'To create loops', 'To delete files'],
                "correcta": 0,
                "explicacion": 'The except block intercepts exceptions so the program can recover and continue running safely.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 21,
        "titulo": 'Chapter 21: Decoding Tracebacks and Diagnosing Failures',
        "resumen": 'Learn how to read Python error reports to pinpoint the exact line and cause of any problem.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Understanding Tracebacks',
                "tipo": 'observar',
                "instruccion": 'A Traceback shows the file, line number, and error type. Reading from the bottom up reveals the exact cause of the crash. Run the code to observe.',
                "codigo": "# A Traceback reveals the file, line, and error type:\nprint('Analyzing Traceback...')\nerror_type = 'TypeError: unsupported operand type(s)'\nprint('Diagnostic:', error_type)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'traceback' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Fixing IndexError',
                "tipo": 'experimentar',
                "instruccion": "An IndexError occurs when trying to access an index outside the list range. Modify the index from 10 to 1 to access the valid element without error, and press Control + Enter.",
                "codigo": "try:\n    items = [1, 2]\n    # Modify index 10 to 1 to access the valid element without error:\n    print('Element:', items[1])\nexcept IndexError as err:\n    print('Caught error: Index out of range.')",
                "pistas": ['Change items[10] to items[1] and press Control + Enter.'],
                "validar": lambda src, res, ns: ('element: 2' in res.lower() or 'elemento: 2' in res.lower()) and ('caught error' not in res.lower() and 'error capturado' not in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Type conversion fix',
                "tipo": 'desafio',
                "instruccion": "Fix the error in the code: convert '5' to a number with int() before adding so that it prints: print('Correct sum:', 10 + int('5')).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Correct sum: 15',
                "pistas": ["Use int('5') to convert the string to an integer before addition."],
                "validar": lambda src, res, ns: '15' in res and ('correct sum' in res.lower() or 'suma correcta' in res.lower() or ns.get('suma') == 15 or ns.get('sum') == 15)
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich shortcut key in Python Learning with NVDA moves the cursor directly to the error line reported in the Traceback?\n\nOptions:\n\n1. F4\n\n2. F1\n\n3. F12\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which shortcut key moves the cursor directly to the error line in the Traceback?',
                "opciones": ['F4', 'F1', 'F12'],
                "correcta": 0,
                "explicacion": 'F4 immediately jumps to the line of error in the editor and speaks the diagnosis.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 22,
        "titulo": 'Chapter 22: File Input and Output: with open() for Text',
        "resumen": 'Save and read data from disk files safely and reliably using with open().',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Writing files with with open()',
                "tipo": 'observar',
                "instruccion": 'The with open() context manager ensures that the file is cleanly closed when leaving the block, even if an unexpected error occurs. Run the code to observe.',
                "codigo": "# with open guarantees the file is closed upon exiting the block:\nwith open('greeting.txt', 'w', encoding='utf-8') as f:\n    f.write('Hello from persistent file!')\nprint('File written successfully.')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('written successfully' in res.lower() or 'guardado con éxito' in res.lower() or 'escrito con éxito' in res.lower() or 'guardado' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Writing lines',
                "tipo": 'experimentar',
                "instruccion": "Modify the code to write 'Line 2' into the file and press Control + Enter.",
                "codigo": "with open('example.txt', 'w', encoding='utf-8') as f:\n    f.write('Line 2')\nprint('Completed')",
                "pistas": ['Change the text inside write() and press Control + Enter.'],
                "validar": lambda src, res, ns: 'completed' in res.lower() or 'completado' in res.lower()
            },
            {
                "titulo": 'Step 3: Practical Challenge: Writing accessible message',
                "tipo": 'desafio',
                "instruccion": "Use with open('message.txt', 'w', encoding='utf-8') as f: and write f.write('Accessible Python'). Then print: print('Save complete').",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Save complete',
                "pistas": ["Open 'message.txt' with mode 'w', write the text, and print('Save complete')."],
                "validar": lambda src, res, ns: ('save complete' in res.lower() or 'guardado listo' in res.lower() or 'guardado exitoso' in res.lower()) and 'open' in src
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": "Conceptual check question:\n\nWhy is it recommended to use 'with open()' when working with files?\n\nOptions:\n\n1. Because it automatically closes the file even if an error occurs\n\n2. Because it encrypts the data\n\n3. Because it uses no memory\n\nType your option number (1, 2, or 3) and press Control + Enter.",
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": "Why is it recommended to use 'with open()' when working with files?",
                "opciones": ['Because it automatically closes the file even if an error occurs', 'Because it encrypts the data', 'Because it uses no memory'],
                "correcta": 0,
                "explicacion": 'The with statement acts as a context manager guaranteeing that system resources are safely released.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 23,
        "titulo": 'Chapter 23: Object Paradigm: Classes, Instances, and Attributes',
        "resumen": 'Create real-world blueprints grouping data and behavior into classes.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Classes and instances',
                "tipo": 'observar',
                "instruccion": 'A class is a blueprint for creating objects. An instance is a concrete object created from that class. Attributes are the data variables stored inside. Run the code to observe.',
                "codigo": "class Book:\n    title = 'Python Learning'\n    pages = 200\n\nmy_book = Book()\nprint('Book title:', my_book.title)\nprint('Pages:', my_book.pages)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('python' in res.lower() and '200' in res)
            },
            {
                "titulo": 'Step 2: Observation: Modifying attributes',
                "tipo": 'experimentar',
                "instruccion": "You can modify an attribute of an object instance. Change the device type to 'Braille Display' and press Control + Enter.",
                "codigo": "class Device:\n    device_type = 'Screen Reader'\n\ndevice = Device()\n# Modify the attribute to 'Braille Display':\ndevice.device_type = 'Braille Display'\nprint('Device:', device.device_type)",
                "pistas": ["Change device.device_type to 'Braille Display' and press Control + Enter."],
                "validar": lambda src, res, ns: 'braille' in res.lower() or (hasattr(ns.get('device'), 'device_type') and 'braille' in ns.get('device').device_type.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Pet class',
                "tipo": 'desafio',
                "instruccion": "Create a class named 'Pet' with a class attribute species = 'Dog'. Create an object dog = Pet() and print: print('Species:', dog.species).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Species: Dog',
                "pistas": ["Define class Pet:, indent 4 spaces species = 'Dog', create dog = Pet(), and print('Species:', dog.species)."],
                "validar": lambda src, res, ns: ((hasattr(ns.get('Pet'), 'species') and ns.get('Pet').species in ('Dog', 'dog', 'Perro', 'perro')) or (hasattr(ns.get('Mascota'), 'especie'))) and ('dog' in res.lower() or 'perro' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is a class in object-oriented programming?\n\nOptions:\n\n1. A blueprint or template for creating objects with data and functions\n\n2. A numeric variable\n\n3. A repetition loop\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is a class in object-oriented programming?',
                "opciones": ['A blueprint or template for creating objects with data and functions', 'A numeric variable', 'A repetition loop'],
                "correcta": 0,
                "explicacion": 'A class is the structural blueprint from which concrete objects are instantiated.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 24,
        "titulo": 'Chapter 24: The __init__ Constructor and the self Parameter',
        "resumen": 'Initialize objects with unique attribute values at the exact moment of their creation.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The __init__ constructor',
                "tipo": 'observar',
                "instruccion": 'The __init__ method is the constructor in Python. It runs automatically when creating a new object instance. The self parameter refers to the specific instance being created. Run the code to observe.',
                "codigo": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\np1 = Person('Sophia', 28)\nprint(f'{p1.name} is {p1.age} years old.')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('sophia' in res.lower() or 'sofía' in res.lower() or 'ana' in res.lower()) and '28' in res
            },
            {
                "titulo": 'Step 2: Observation: Custom attribute values',
                "tipo": 'experimentar',
                "instruccion": "Modify the starting balance to 500 and press Control + Enter.",
                "codigo": "class Account:\n    def __init__(self, owner, balance):\n        self.owner = owner\n        self.balance = balance\n\n# Modify the starting balance to 500:\na = Account('Carlos', 500)\nprint('Owner:', a.owner, 'Balance:', a.balance)",
                "pistas": ['Change balance argument from 100 to 500 and press Control + Enter.'],
                "validar": lambda src, res, ns: (getattr(ns.get('a'), 'balance', 0) == 500 or getattr(ns.get('c'), 'saldo', 0) == 500) and '500' in res
            },
            {
                "titulo": 'Step 3: Practical Challenge: User class constructor',
                "tipo": 'desafio',
                "instruccion": "Create a class User with def __init__(self, username): that assigns self.username = username. Create u = User('Programmer') and print: print('Username:', u.username).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Username: Programmer',
                "pistas": ["Define class User:, def __init__(self, username): self.username = username, u = User('Programmer'), print('Username:', u.username)."],
                "validar": lambda src, res, ns: ('User' in ns or 'Usuario' in ns) and ('programmer' in res.lower() or 'programador' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the purpose of the special __init__ method in Python?\n\nOptions:\n\n1. It is the constructor that initializes object attributes upon creation\n\n2. It is a function to delete an object\n\n3. It is a for loop\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is the purpose of the special __init__ method in Python?',
                "opciones": ['It is the constructor that initializes object attributes upon creation', 'It is a function to delete an object', 'It is a for loop'],
                "correcta": 0,
                "explicacion": '__init__ executes automatically whenever a new object instance is created.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 25,
        "titulo": 'Chapter 25: Instance Methods and Encapsulation',
        "resumen": 'Define actions that each object can perform independently using instance methods.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Instance methods',
                "tipo": 'observar',
                "instruccion": "Instance methods are functions defined inside a class that take 'self' as their first parameter. They can read and modify the object's attributes. Run the code to observe.",
                "codigo": "class Player:\n    def __init__(self, song):\n        self.song = song\n    def play(self):\n        print(f'Playing track: {self.song}')\n\nplayer = Player('Accessible Symphony')\nplayer.play()",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'playing' in res.lower() or 'reproduciendo' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Modifying state via methods',
                "tipo": 'experimentar',
                "instruccion": 'Methods can update object attributes. Call t.increase() twice so the temperature reaches 22, and press Control + Enter.',
                "codigo": "class Thermostat:\n    def __init__(self, temp):\n        self.temp = temp\n    def increase(self):\n        self.temp += 1\n\nt = Thermostat(20)\n# Call t.increase() twice:\nt.increase()\nt.increase()\nprint('Current temperature:', t.temp)",
                "pistas": ['Invoke t.increase() two times before printing.'],
                "validar": lambda src, res, ns: (getattr(ns.get('t'), 'temp', 0) >= 22) and ('22' in res or 'temperature' in res.lower() or 'temperatura' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Greeting method',
                "tipo": 'desafio',
                "instruccion": "Create a class Greeting with def __init__(self, name): and a method say_hello(self) that prints: print(f'Hello, {self.name}'). Create g = Greeting('Friend') and call g.say_hello().",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Hello, Friend',
                "pistas": ["Define class Greeting, __init__(self, name), say_hello(self), g = Greeting('Friend'), g.say_hello()."],
                "validar": lambda src, res, ns: ('Greeting' in ns or 'Saludo' in ns) and ('hello' in res.lower() or 'hola' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": "Conceptual check question:\n\nWhat does the first parameter 'self' represent in class methods?\n\nOptions:\n\n1. The reference to the specific object instance that called the method\n\n2. A reserved Windows keyword\n\n3. An integer number\n\nType your option number (1, 2, or 3) and press Control + Enter.",
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": "What does the first parameter 'self' represent in class methods?",
                "opciones": ['The reference to the specific object instance that called the method', 'A reserved Windows keyword', 'An integer number'],
                "correcta": 0,
                "explicacion": 'self allows methods to access and modify the specific attributes of that individual object.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 26,
        "titulo": 'Chapter 26: Class Inheritance: Code Reuse with super()',
        "resumen": 'Create specialized child classes that inherit attributes and methods from a parent class.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Inheritance',
                "tipo": 'observar',
                "instruccion": 'Inheritance allows a child class to inherit attributes and methods from a parent class. Run the code to observe how Dog inherits from Animal.',
                "codigo": "class Animal:\n    def __init__(self, name):\n        self.name = name\n\nclass Dog(Animal):\n    def bark(self):\n        print(f'{self.name} says: Woof woof!')\n\nmy_dog = Dog('Toby')\nmy_dog.bark()",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: ('woof' in res.lower() or 'guau' in res.lower()) and ('toby' in res.lower() or 'boby' in res.lower())
            },
            {
                "titulo": 'Step 2: Observation: Modifying inherited attributes',
                "tipo": 'experimentar',
                "instruccion": "Modify the salary to 2500 and press Control + Enter.",
                "codigo": "class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n\n# Modify salary to 2500:\ne = Employee('Martha', 2500)\nprint('Employee:', e.name, 'Salary:', e.salary)",
                "pistas": ['Change 1800 to 2500 and press Control + Enter.'],
                "validar": lambda src, res, ns: (getattr(ns.get('e'), 'salary', 0) == 2500 or getattr(ns.get('e'), 'sueldo', 0) == 2500) and '2500' in res
            },
            {
                "titulo": 'Step 3: Practical Challenge: Vehicle inheritance with super()',
                "tipo": 'desafio',
                "instruccion": "Create class Vehicle with __init__(self, make). Create class Car(Vehicle) whose __init__(self, make, model) uses super().__init__(make) and self.model = model. Create c = Car('Toyota', 'Corolla') and print: print(c.make, c.model).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Toyota Corolla',
                "pistas": ['Use super().__init__(make) inside Car.__init__ to call the parent constructor.'],
                "validar": lambda src, res, ns: (('Car' in ns and issubclass(ns.get('Car'), ns.get('Vehicle', object))) or ('Coche' in ns and issubclass(ns.get('Coche'), ns.get('Vehiculo', object)))) and 'toyota' in res.lower() and 'corolla' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich function allows calling the constructor or methods of the parent class from a child class?\n\nOptions:\n\n1. super()\n\n2. parent()\n\n3. base()\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which function allows calling the constructor or methods of the parent class?',
                "opciones": ['super()', 'parent()', 'base()'],
                "correcta": 0,
                "explicacion": 'super() provides access to the parent class, enabling clean inheritance and code extension.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 27,
        "titulo": 'Chapter 27: Polymorphism and Special Methods (__str__)',
        "resumen": 'Customize how screen readers and print() display your objects by implementing __str__.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The __str__ special method',
                "tipo": 'observar',
                "instruccion": 'The __str__ special method defines the human-readable string representation of an object. Whenever print(obj) or str(obj) is called, Python executes __str__. Run the code to observe.',
                "codigo": "class Student:\n    def __init__(self, name, course):\n        self.name = name\n        self.course = course\n    def __str__(self):\n        return f'Student: {self.name}, Course: {self.course}'\n\nstudent = Student('David', 'Python')\nprint(student)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'david' in res.lower() and 'python' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Customizing string output',
                "tipo": 'experimentar',
                "instruccion": "Modify the product price to 25 and press Control + Enter.",
                "codigo": "class Product:\n    def __init__(self, item, price):\n        self.item = item\n        self.price = price\n    def __str__(self):\n        return f'{self.item}: ${self.price}'\n\n# Modify the price to 25:\np = Product('Keyboard', 25)\nprint(p)",
                "pistas": ['Change price from 15 to 25 and press Control + Enter.'],
                "validar": lambda src, res, ns: '25' in res and ('keyboard' in res.lower() or 'teclado' in res.lower())
            },
            {
                "titulo": 'Step 3: Practical Challenge: Point string representation',
                "tipo": 'desafio',
                "instruccion": "Create class Point with __init__(self, x, y) and special method __str__(self) that returns f'Point({self.x}, {self.y})'. Create p = Point(3, 7) and print it with print(p).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Point(3, 7)',
                "pistas": ["Define __str__(self): return f'Point({self.x}, {self.y})', create p = Point(3, 7), and print(p)."],
                "validar": lambda src, res, ns: ('Point' in ns or 'Punto' in ns) and ('3' in res and '7' in res)
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the purpose of implementing the __str__ special method in a class?\n\nOptions:\n\n1. To define the readable text representation when printing the object with print()\n\n2. To delete the object from memory\n\n3. To convert the class into a list\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is the purpose of implementing the __str__ special method in a class?',
                "opciones": ['To define the readable text representation when printing the object with print()', 'To delete the object from memory', 'To convert the class into a list'],
                "correcta": 0,
                "explicacion": '__str__ returns a friendly, accessible text representation of the object for screen readers and logging.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 28,
        "titulo": 'Chapter 28: Standard Library Modules (math, random, datetime)',
        "resumen": 'Leverage Python built-in batteries for mathematics, randomness, and dates without installing third-party packages.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: The math module',
                "tipo": 'observar',
                "instruccion": 'The Python standard library comes built-in. The math module provides powerful math functions. Run the code to observe math.isqrt and math.pi.',
                "codigo": "import math\nprint('Square root of 64:', math.isqrt(64))\nprint('Rounded Pi value:', round(math.pi, 4))",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: '8' in res and '3.14' in res
            },
            {
                "titulo": 'Step 2: Observation: The random module',
                "tipo": 'experimentar',
                "instruccion": "Modify the random range to generate numbers between 100 and 200, and press Control + Enter.",
                "codigo": "import random\n# Modify the range to generate numbers between 100 and 200:\nrandom_num = random.randint(100, 200)\nprint('Random number:', random_num)",
                "pistas": ['Change random.randint(1, 10) to random.randint(100, 200).'],
                "validar": lambda src, res, ns: (100 <= ns.get('random_num', 0) <= 200) or (100 <= ns.get('azar', 0) <= 200)
            },
            {
                "titulo": 'Step 3: Practical Challenge: Calculating square roots',
                "tipo": 'desafio',
                "instruccion": "Import the math module and calculate the integer square root of 144 with math.isqrt(144). Print: print('Square root of 144:', math.isqrt(144)).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Square root of 144: 12',
                "pistas": ["Write import math, then print('Square root of 144:', math.isqrt(144))."],
                "validar": lambda src, res, ns: '12' in res and '144' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich keyword is used to load modules from the Python standard library?\n\nOptions:\n\n1. import\n\n2. load\n\n3. include\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which keyword is used to load modules from the Python standard library?',
                "opciones": ['import', 'load', 'include'],
                "correcta": 0,
                "explicacion": 'The import keyword loads modules and packages into your current script namespace.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 29,
        "titulo": 'Chapter 29: Structured Persistence: JSON Format and Serialization',
        "resumen": 'Save and exchange structured dictionaries using the universal JSON text format.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: json.dumps()',
                "tipo": 'observar',
                "instruccion": 'JSON is a universal text format for exchanging data between applications. json.dumps() converts a Python dictionary into a JSON formatted string. Run the code to observe.',
                "codigo": "import json\ndata = {'user': 'Elena', 'level': 3, 'active': True}\njson_text = json.dumps(data)\nprint('JSON formatted text:', json_text)",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'elena' in res.lower() and 'json' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: json.loads()',
                "tipo": 'experimentar',
                "instruccion": "json.loads() parses JSON text back into a Python dictionary. Modify the duration to 60 hours and press Control + Enter.",
                "codigo": 'import json\n# Modify duration to 60 hours:\ntext = \'{"course": "Python", "hours": 60}\'\nobj = json.loads(text)\nprint(\'Course:\', obj[\'course\'], \'Hours:\', obj[\'hours\'])',
                "pistas": ['Change 40 to 60 inside the JSON string and press Control + Enter.'],
                "validar": lambda src, res, ns: (ns.get('obj', {}).get('hours') == 60 or ns.get('objeto', {}).get('duracion_horas') == 60) and '60' in res
            },
            {
                "titulo": 'Step 3: Practical Challenge: Configuration dictionary to JSON',
                "tipo": 'desafio',
                "instruccion": "Import json. Create a dictionary config = {'theme': 'dark', 'font': 14}. Convert it to JSON text with json.dumps(config) and print: print('JSON:', json.dumps(config)).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'JSON: {"theme": "dark", "font": 14}',
                "pistas": ["Import json, create config, and print('JSON:', json.dumps(config))."],
                "validar": lambda src, res, ns: ('dark' in res.lower() or 'oscuro' in res.lower()) and '14' in res
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich function in the json module converts a Python dictionary into a JSON formatted string?\n\nOptions:\n\n1. json.dumps()\n\n2. json.loads()\n\n3. json.parse()\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['dumps stands for dump string.'],
                "pregunta": 'Which function in the json module converts a Python dictionary into a JSON string?',
                "opciones": ['json.dumps()', 'json.loads()', 'json.parse()'],
                "correcta": 0,
                "explicacion": 'json.dumps() serializes Python data structures into JSON formatted text.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 30,
        "titulo": 'Chapter 30: Relational Databases with SQLite: Tables and Queries',
        "resumen": 'Manage tabular relational data using SQL and Python built-in sqlite3 module.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Creating tables and querying in SQLite',
                "tipo": 'observar',
                "instruccion": 'SQLite is a lightweight SQL database built into Python. You can create in-memory databases with sqlite3.connect(":memory:"). Run the code to observe creating a table and inserting a note.',
                "codigo": "import sqlite3\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE notes (id INTEGER, title TEXT)')\ncur.execute(\"INSERT INTO notes VALUES (1, 'My first note in SQLite')\")\ncon.commit()\ncur.execute('SELECT title FROM notes')\nprint('Database note:', cur.fetchone()[0])\ncon.close()",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'sqlite' in res.lower() or 'note' in res.lower() or 'nota' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Fetching multiple rows',
                "tipo": 'experimentar',
                "instruccion": "Add a second row with Subject 'Python' and Grade 10, then press Control + Enter.",
                "codigo": "import sqlite3\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE grades (subject TEXT, score INT)')\ncur.execute(\"INSERT INTO grades VALUES ('Math', 8)\")\n# Add a second row with 'Python' and 10:\ncur.execute(\"INSERT INTO grades VALUES ('Python', 10)\")\ncur.execute('SELECT * FROM grades')\nrows = cur.fetchall()\nprint('Table rows:', rows)",
                "pistas": ['Insert the Python row and press Control + Enter.'],
                "validar": lambda src, res, ns: 'python' in res.lower() or len(ns.get('rows', [])) >= 2 or len(ns.get('filas', [])) >= 2
            },
            {
                "titulo": 'Step 3: Practical Challenge: Inserting and selecting products',
                "tipo": 'desafio',
                "instruccion": "Create an in-memory SQLite database with con = sqlite3.connect(':memory:'), create a table products (name TEXT), insert 'Keyboard', and query with SELECT to print the product.",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'Keyboard',
                "pistas": ["cur.execute('CREATE TABLE products (name TEXT)'), cur.execute(\"INSERT INTO products VALUES ('Keyboard')\"), cur.execute('SELECT name FROM products'), print(cur.fetchone()[0])"],
                "validar": lambda src, res, ns: 'keyboard' in res.lower() or 'teclado' in res.lower() or 'laptop' in res.lower()
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich SQL statement is used to query and retrieve rows from a database table?\n\nOptions:\n\n1. SELECT\n\n2. INSERT\n\n3. DELETE\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which SQL statement is used to query and retrieve rows from a table?',
                "opciones": ['SELECT', 'INSERT', 'DELETE'],
                "correcta": 0,
                "explicacion": 'SELECT is the fundamental SQL statement for querying records.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 31,
        "titulo": 'Chapter 31: Consuming Web Services: HTTP Requests and JSON Responses',
        "resumen": 'Communicate with web servers over the internet to fetch dynamic online data.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: REST API responses',
                "tipo": 'observar',
                "instruccion": 'REST APIs communicate over HTTP returning structured JSON data. A status code of 200 means success. Run the code to observe an API response simulation.',
                "codigo": "# Structured REST API response simulation:\napi_response = {\n    'status': 200,\n    'data': {'temperature': 22, 'weather': 'Clear'}\n}\nif api_response['status'] == 200:\n    weather = api_response['data']['weather']\n    print(f'API Weather Report: {weather}')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'clear' in res.lower() or 'despejado' in res.lower() or 'api' in res.lower()
            },
            {
                "titulo": 'Step 2: Observation: Modifying API payloads',
                "tipo": 'experimentar',
                "instruccion": "Modify the user list by adding 'Marcus' and press Control + Enter.",
                "codigo": "response = {\n    'code': 200,\n    'users': ['Andrea', 'Paul', 'Lucy', 'Marcus']\n}\nprint('Received users list:', response['users'])",
                "pistas": ["Add 'Marcus' into the users list and execute."],
                "validar": lambda src, res, ns: 'marcus' in res.lower() or 'marcos' in res.lower() or len(ns.get('response', {}).get('users', [])) >= 4
            },
            {
                "titulo": 'Step 3: Practical Challenge: Checking API status',
                "tipo": 'desafio',
                "instruccion": "Given the response resp = {'status': 'OK', 'message': 'Service available'}, check if resp['status'] == 'OK' and print: print('API:', resp['message']).",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'API: Service available',
                "pistas": ["Check if resp['status'] == 'OK': and print('API:', resp['message'])."],
                "validar": lambda src, res, ns: ('service available' in res.lower() or 'servicio disponible' in res.lower() or 'disponible' in res.lower() or 'api' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhich standard HTTP status code indicates that a web request succeeded?\n\nOptions:\n\n1. 200 (OK)\n\n2. 404 (Not Found)\n\n3. 500 (Internal Error)\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'Which standard HTTP status code indicates a successful web request?',
                "opciones": ['200 (OK)', '404 (Not Found)', '500 (Internal Error)'],
                "correcta": 0,
                "explicacion": 'Status code 200 indicates that the HTTP request was successful.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    },
    {
        "id": 32,
        "titulo": 'Chapter 32: Software Quality: Unit Testing with unittest',
        "resumen": 'Automatically verify that each part of your code behaves exactly as expected without errors.',
        "pasos": [
            {
                "titulo": 'Step 1: Foundation: Automated assertions',
                "tipo": 'observar',
                "instruccion": "Unit tests verify individual functions with assertions. The 'assert' statement verifies that an expression is True; if not, it raises an AssertionError. Run the code to observe.",
                "codigo": "def multiply(a, b):\n    return a * b\n\n# Manual assertion check:\nassert multiply(3, 4) == 12\nprint('Unit test passed: 3 * 4 = 12')",
                "pistas": ['Press Control + Enter to execute.'],
                "validar": lambda src, res, ns: 'passed' in res.lower() or 'superada' in res.lower() or '12' in res
            },
            {
                "titulo": 'Step 2: Observation: Modifying test assertions',
                "tipo": 'experimentar',
                "instruccion": "Modify the assertion to verify that subtract(20, 5) == 15, and press Control + Enter.",
                "codigo": "def subtract(a, b):\n    return a - b\n\n# Modify the assertion to verify that subtract(20, 5) == 15:\nassert subtract(20, 5) == 15\nprint('Subtract test passed')",
                "pistas": ['Change the assertion to subtract(20, 5) == 15 and press Control + Enter.'],
                "validar": lambda src, res, ns: 'subtract(20, 5)' in src or 'subtract(20,5)' in src or 'restar(20, 5)' in src or 'restar(20,5)' in src or ('passed' in res.lower() and '15' in src) or ('superada' in res.lower() and '15' in src)
            },
            {
                "titulo": 'Step 3: Practical Challenge: Testing is_even()',
                "tipo": 'desafio',
                "instruccion": "Define a function is_even(number) that returns number % 2 == 0. Write assert is_even(4) == True and then print: print('All tests passed successfully').",
                "codigo": '# Write your code here to solve the challenge:\n\n',
                "salida_esperada": 'All tests passed successfully',
                "pistas": ["Define is_even(number): return number % 2 == 0, write assert is_even(4) == True, and print('All tests passed successfully')."],
                "validar": lambda src, res, ns: ((callable(ns.get('is_even')) and ns.get('is_even')(4) is True and ns.get('is_even')(5) is False) or (callable(ns.get('es_par')) and ns.get('es_par')(4) is True and ns.get('es_par')(5) is False)) and ('passed' in res.lower() or 'éxito' in res.lower() or 'exito' in res.lower() or 'superada' in res.lower() or 'success' in res.lower())
            },
            {
                "titulo": 'Step 4: Conceptual Check',
                "tipo": 'quiz',
                "instruccion": 'Conceptual check question:\n\nWhat is the primary purpose of writing unit tests in software engineering?\n\nOptions:\n\n1. To automatically verify that each small part of the code works as expected\n\n2. To make the program run faster\n\n3. To change the editor color\n\nType your option number (1, 2, or 3) and press Control + Enter.',
                "codigo": '# Write your answer here (1, 2 or 3):\n',
                "pistas": ['Read the 3 options carefully.'],
                "pregunta": 'What is the primary purpose of writing unit tests?',
                "opciones": ['To automatically verify that each small part of the code works as expected', 'To make the program run faster', 'To change the editor color'],
                "correcta": 0,
                "explicacion": 'Unit tests automatically guarantee that individual units of code meet requirements and prevent future regressions.',
                "validar": lambda src, res, ns: [l.strip() for l in src.splitlines() if l.strip() and not l.strip().startswith("#")] == ['1']
            }
        ]
    }
]

# ============================================================================
# Complete Technical Python Glossary (Screen-Reader-Accessible Definitions)
# ============================================================================
GLOSARIO = {
    'AttributeError': 'Exception raised when attempting to access or call an attribute or method that does not exist on an object.',
    'Exception': 'Fundamental base class from which all non-system-exiting standard Python exceptions inherit.',
    'False': 'Boolean value representing logical falsity.',
    'FileNotFoundError': 'Exception raised when attempting to open a file that does not exist at the specified path.',
    'IndentationError': 'Syntax error raised when indentation levels do not conform to Python formatting rules.',
    'IndexError': 'Exception raised when attempting to access an index that is out of range for a sequence or list.',
    'KeyError': 'Exception raised when attempting to access a dictionary key that does not exist.',
    'NameError': 'Exception raised when attempting to use a variable or function name that has not been defined.',
    'None': 'Special constant representing the absence of a value or an empty result.',
    'SyntaxError': 'Error detected by the Python parser before execution due to invalid grammar or syntax rules.',
    'Traceback': 'Detailed diagnostic report describing the active call stack and the exact line number where an exception occurred.',
    'True': 'Boolean value representing logical truth.',
    'TypeError': 'Exception raised when an operation or function is applied to an object of inappropriate data type.',
    'ValueError': 'Exception raised when a function receives an argument of the correct type but an inappropriate value.',
    'ZeroDivisionError': 'Exception raised when attempting to divide a number or perform modulo by zero.',
    '__eq__': 'Special method defining the behavior of the equality operator (==) between two objects.',
    '__init__': 'Special constructor method called automatically when creating a new class instance.',
    '__len__': 'Special method that allows an object to respond to the built-in len() function.',
    '__repr__': 'Special method returning an unambiguous formal string representation of an object.',
    '__str__': 'Special method returning a friendly, readable string representation of an object for print() and screen readers.',
    'abs': 'Built-in function returning the non-negative absolute value of a number.',
    'algorithm': 'Ordered, precise, and finite sequence of logical instructions designed to solve a specific problem.',
    'algoritmo': 'Ordered, precise, and finite sequence of logical instructions designed to solve a specific problem.',
    'all': 'Built-in function returning True if all elements of an iterable evaluate to true.',
    'and': 'Logical operator returning True only if all connected conditions evaluate to true.',
    'any': 'Built-in function returning True if at least one element of an iterable evaluates to true.',
    'as': 'Keyword used to assign an alias or target variable to an imported module, context manager, or exception.',
    'assert': 'Internal debugging statement that raises an AssertionError if the evaluated expression is false.',
    'async': 'Keyword used to declare a coroutine function or asynchronous context for non-blocking concurrent operations.',
    'attribute': 'Variable or data field directly bound to an object instance or class.',
    'atributo': 'Variable or data field directly bound to an object instance or class.',
    'await': 'Keyword pausing coroutine execution until an asynchronous operation yields its result.',
    'bin': 'Built-in function converting an integer into its binary string representation with prefix 0b.',
    'bool': 'Boolean data type representing one of two truth values: True or False.',
    'break': 'Control statement that immediately terminates the innermost enclosing for or while loop.',
    'bytes': 'Immutable sequence of byte values used for handling raw binary data.',
    'callable': 'Built-in function returning True if the provided argument can be called like a function.',
    'casting': 'Explicit conversion of a value from one compatible data type to another (for example, int("25")).',
    'chr': 'Built-in function returning the string character corresponding to a given integer Unicode code point.',
    'clase': 'Blueprint or structural definition that bundles data attributes and behaviors common to its objects.',
    'class': 'Keyword defining a new class blueprint to instantiate objects with their own attributes and methods.',
    'continue': 'Control statement that skips the remainder of the current loop iteration and proceeds to the next cycle.',
    'def': 'Keyword used to define a new function or class method along with its parameter list.',
    'del': 'Statement used to delete references to variables, list items, or dictionary keys.',
    'dict': 'Mutable associative collection of key-value pairs delimited by curly braces {}.',
    'dir': 'Built-in function returning a list of valid attributes and methods available on an object or module.',
    'docstring': 'String literal occurring as the first statement in a module, function, or class used for documentation.',
    'elif': 'Short for "else if"; evaluates an alternative condition when preceding if conditions were false.',
    'else': 'Fallback branch executing when all preceding conditional checks evaluate to false.',
    'encapsulation': 'Object-oriented principle of bundling data and methods while restricting direct external access to internal state.',
    'encapsulamiento': 'Object-oriented principle of bundling data and methods while restricting direct external access to internal state.',
    'enumerate': 'Built-in function yielding tuples containing an automatic loop counter index and the corresponding iterable item.',
    'except': 'Clause that catches and handles specific exceptions raised within an associated try block.',
    'f-string': 'Formatted string literal prefixed with f enabling expression interpolation directly inside curly braces {}.',
    'filter': 'Built-in function filtering elements from an iterable based on a boolean predicate function.',
    'finally': 'Block in a try/except statement that always executes unconditionally, ideal for cleanup actions.',
    'float': 'Numeric data type representing real numbers with decimal points (for example, 3.14).',
    'for': 'Loop statement used to iterate over items of any sequence or iterable in order.',
    'format': 'Converts a value to a formatted representation according to a format specification.',
    'from': 'Keyword used in import statements to import specific attributes or functions directly from a module.',
    'global': 'Declaration stating that a variable inside a function refers to module-level global scope.',
    'help': 'Built-in function invoking the interactive Python help utility and documentation browser.',
    'inheritance': 'Mechanism allowing a child class to inherit attributes and methods from a parent superclass.',
    'herencia': 'Mechanism allowing a child class to inherit attributes and methods from a parent superclass.',
    'hex': 'Built-in function converting an integer into a lowercase hexadecimal string prefixed with 0x.',
    'id': 'Built-in function returning the unique integer identity and memory address of an object.',
    'if': 'Fundamental conditional branching statement executing its code block when the condition evaluates to true.',
    'import': 'Keyword loading modules, libraries, or external files to use their tools in the current script.',
    'in': 'Membership operator checking whether a value exists within a sequence, also used in for loops.',
    'indentation': 'Leading whitespace characters determining the hierarchical block structure of Python source code.',
    'indentacion': 'Leading whitespace characters determining the hierarchical block structure of Python source code.',
    'immutability': 'Property of data types whose values cannot be altered in-place after creation (such as tuples and strings).',
    'inmutabilidad': 'Property of data types whose values cannot be altered in-place after creation (such as tuples and strings).',
    'input': 'Built-in function pausing script execution to prompt the user for keyboard input, always returning a str.',
    'instance': 'Concrete individual object created from a class blueprint.',
    'instancia': 'Concrete individual object created from a class blueprint.',
    'int': 'Numeric data type representing whole integers without a decimal point (positive, negative, or zero).',
    'is': 'Identity operator evaluating to True if two variables reference the exact same object in memory.',
    'isinstance': 'Built-in function testing whether an object is an instance of a specified class or tuple of classes.',
    'issubclass': 'Built-in function testing whether a class inherits from or is a subclass of another class.',
    'iterator': 'Object representing a stream of data that returns successive items one at a time using __next__().',
    'iterador': 'Object representing a stream of data that returns successive items one at a time using __next__().',
    'lambda': 'Keyword defining a small, anonymous inline function without needing a standard def block.',
    'len': 'Built-in function returning the number of items or character length of a container or sequence.',
    'list': 'Mutable, ordered sequence of elements enclosed in square brackets [] and separated by commas.',
    'map': 'Built-in function applying a specified function to each item of an iterable and returning an iterator.',
    'max': 'Built-in function returning the largest item in an iterable or among two or more arguments.',
    'method': 'Function that belongs to and is executed within the context of a class or object instance.',
    'metodo': 'Function that belongs to and is executed within the context of a class or object instance.',
    'min': 'Built-in function returning the smallest item in an iterable or among two or more arguments.',
    'mutability': 'Property of data types whose contents can be modified in-place after creation (such as lists and dicts).',
    'mutabilidad': 'Property of data types whose contents can be modified in-place after creation (such as lists and dicts).',
    'nonlocal': 'Keyword declaring that a variable belongs to an enclosing nested scope rather than local or global scope.',
    'not': 'Logical negation operator inverting truth values (converting True to False and vice versa).',
    'object': 'Base class of the Python class hierarchy, and any runtime data instance residing in memory.',
    'objeto': 'Base class of the Python class hierarchy, and any runtime data instance residing in memory.',
    'open': 'Built-in function opening a file from disk and returning a file object for reading or writing.',
    'or': 'Logical operator returning True if at least one of the connected conditions evaluates to true.',
    'ord': 'Built-in function returning the integer Unicode code point representing an individual single character.',
    'pass': 'Null operation placeholder statement used where syntax requires a statement but no action is desired.',
    'pep8': 'Official Python style guide promoting clean code readability, such as 4-space indentation per level.',
    'pip': 'Standard package management tool used to install and manage third-party Python software packages.',
    'polymorphism': 'Object-oriented capability allowing different classes to respond to the same method call appropriately.',
    'polimorfismo': 'Object-oriented capability allowing different classes to respond to the same method call appropriately.',
    'pow': 'Built-in function raising a base number to a given power (equivalent to the ** operator).',
    'print': 'Built-in function outputting formatted text to standard output for speech synthesis and display.',
    'raise': 'Statement deliberately throwing an exception to signal an error or unusual condition.',
    'range': 'Immutable sequence of numbers commonly used to specify loop iteration counts in for loops.',
    'return': 'Statement exiting a function and optionally passing back a computed result to the caller.',
    'reversed': 'Built-in function returning a reverse iterator over the elements of a sequence.',
    'round': 'Built-in function rounding a floating-point number to a specified number of decimal digits.',
    'scope': 'Visibility and lifetime region of variables (local inside functions or global across a module).',
    'self': 'Conventional first parameter of instance methods representing the specific object instance being manipulated.',
    'set': 'Mutable, unordered collection of unique elements with no duplicates, delimited by curly braces {}.',
    'sorted': 'Built-in function returning a new sorted list from elements of any iterable without mutating the original.',
    'str': 'Data type representing immutable textual character sequences enclosed in quotes.',
    'sum': 'Built-in function calculating and returning the arithmetic total of numeric items in an iterable.',
    'super': 'Built-in function giving access to inherited methods and constructor of a parent superclass.',
    'try': 'Block initiating guarded execution where potential runtime errors and exceptions can be caught.',
    'tuple': 'Immutable, ordered sequence of elements enclosed in parentheses () and separated by commas.',
    'type': 'Built-in function returning the data type or class to which an object belongs.',
    'venv': 'Tool and directory creating lightweight, isolated virtual environments with their own package sets.',
    'while': 'Loop statement repeatedly executing its body as long as a specified condition evaluates to true.',
    'with': 'Context manager statement ensuring reliable acquisition and release of external resources (like files).',
    'yield': 'Keyword pausing a generator function and returning an intermediate value while preserving execution state.',
    'zip': 'Built-in function combining corresponding elements from multiple iterables into tuples.',
}
