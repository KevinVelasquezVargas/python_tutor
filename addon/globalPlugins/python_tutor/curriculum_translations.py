# -*- coding: utf-8 -*-
"""
Traducciones pedagógicas y glosario en inglés para Learning Python with NVDA.
Garantiza localización completa y tono académico riguroso en los 40 capítulos.
"""

CHAPTER_TRANSLATIONS = {
    1: {
        'titulo_en': 'Chapter 1: Computer Architecture: Binary System, CPU, and RAM',
        'resumen_en': 'Understand what physically happens inside the computer before programming: the processor, working memory, and binary system.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Mental Model: Computer Hardware',
                'instruccion_en': 'Before writing code, it is essential to understand what a computer actually is. A computer consists of three fundamental components: 1. The CPU (Central Processing Unit): The execution engine. It does not guess, doubt, or have intuition; it simply executes millions of sequential instructions per second at electromagnetic speed. 2. The RAM (Random Access Memory): The fast, volatile working space. Picture it as a large desk holding the data your active program works with right now. If power is lost or the program closes, everything in RAM vanishes immediately. 3. Secondary Storage (Hard Drive or SSD): The permanent file cabinet. It stores your files, software, and operating system persistently, even without electricity. When you launch a program, it travels from the disk into RAM so the CPU can execute its instructions. Press Enter or Alt + Right Arrow to advance to the next concept.',
                'pistas_en': ['Read the explanation using arrow keys and press Enter or Alt + Right Arrow to continue.'],
            },
            {
                'titulo_en': 'Step 2: Mental Model: The Binary System and Bits',
                'instruccion_en': 'Humans communicate through natural languages like English or Spanish, using alphabets of dozens of letters and the decimal numeral system (digits 0 through 9). However, electronic processors consist of microscopic transistors that can only exist in two physical states: on (current passes) or off (no current). This elemental state is called a Bit (Binary Digit): a 1 represents on and a 0 represents off. Grouping 8 consecutive bits forms a Byte, capable of representing 256 distinct combinations (enough to encode any keyboard letter, numeral, or symbol in ASCII or Unicode). Everything your screen reader speaks —every word, sound, and program statement— is at its deepest level a symphony of zeros and ones coordinated by the CPU. Press Enter or Alt + Right Arrow to verify your understanding in the next step.',
                'pistas_en': ['Press Enter or Alt + Right Arrow to proceed to the conceptual check.'],
            },
            {
                'titulo_en': 'Step 3: Conceptual Check: Computer Architecture',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the analogy of the temporary workspace desk.'],
                'pregunta_en': 'What is the primary function of RAM while a program is running?',
                'opciones_en': ['Store temporary data and instructions at high speed while the program is active.', 'Permanently save files even when the computer is turned off.', 'Generate electrical audio signals for the speakers.'],
                'explicacion_en': 'RAM is the fast, volatile working area holding active data. When the computer powers down, its contents are cleared.',
            },
        ]
    },
    2: {
        'titulo_en': 'Chapter 2: Software and Programming Languages: The Human-Machine Bridge',
        'resumen_en': 'Discover what software is, why we do not speak natural language to computers, and the difference between compiled and interpreted languages.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Mental Model: Why Programming Languages Exist',
                'instruccion_en': "Hardware without software is an inert collection of silicon and copper. Software is the logical instruction set telling hardware what to execute. Why can we not simply tell the computer in plain English: 'Please calculate this month's payroll'? Because human language is full of ambiguity, metaphors, context, and implicit assumptions. Computers, conversely, demand absolute mathematical precision. In early computing, engineers programmed directly in machine code (long strings of zeros and ones) or assembly language, which was exhausting and prone to catastrophic mistakes. To solve this, computer science created 'High-Level Languages'. These use human-readable words with strict grammar to describe algorithms with crystal clarity. Press Enter or Alt + Right Arrow to proceed to the next concept.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Mental Model: Compilers versus Interpreters',
                'instruccion_en': "For the CPU to execute code written in a high-level language, that text must be translated into binary machine language. There are two primary ways this translation happens: 1. Compilation (Compiled languages like C, C++, or Rust): A special program called a 'compiler' takes the entire source code file, parses it all at once, and generates an independent binary executable (.exe on Windows). Think of a translator translating an entire book from German to English and printing it: once printed, you do not need the translator present to read it. 2. Interpretation (Interpreted languages like Python or JavaScript): A program called an 'interpreter' reads your source code line by line, translating and executing each instruction on the fly. Think of a live diplomatic interpreter: they hear a sentence, translate it instantly, and proceed to the next. Python is an interpreted language. This means we can write a statement, run it immediately, and hear the result through our screen reader without waiting for lengthy compilation passes. Press Enter or Alt + Right Arrow to proceed to the conceptual check.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 3: Conceptual Check: The Python Interpreter',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the analogy of the live simultaneous interpreter.'],
                'pregunta_en': 'How does the Python interpreter process the code we write?',
                'opciones_en': ['It reads, translates, and executes instructions line by line in real time.', 'It prints the code onto physical paper sheets before running.', 'It compiles all code into a closed .exe file that cannot be inspected.'],
                'explicacion_en': 'The Python interpreter reads and executes instructions sequentially on the fly, providing rapid, interactive feedback.',
            },
        ]
    },
    3: {
        'titulo_en': 'Chapter 3: What is Python?: History, Zen of Python Philosophy, and Ecosystem',
        'resumen_en': "Learn about Python's origins with Guido van Rossum, the core design principles that make it unique, and its impact on accessibility and industry.",
        'pasos': [
            {
                'titulo_en': "Step 1: Mental Model: Python's Origin and Purpose",
                'instruccion_en': "In late 1989, Dutch software engineer Guido van Rossum set out to design a different kind of programming language. At the time, languages like C required dozens of lines packed with curly braces, semicolons, and low-level memory mechanics for basic tasks. Guido designed Python with a revolutionary goal: prioritize human readability and productivity over mechanical complexity. The name 'Python' does not come from the snake, but from the British comedy troupe 'Monty Python', signifying that programming should not be tedious or intimidating. Today, Python is one of the most widely used languages on Earth. It powers Artificial Intelligence, space science at NASA, big data analytics, and fundamentally, it is the language in which much of the NVDA screen reader itself is built. Press Enter or Alt + Right Arrow to discover Python's philosophical design principles.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Mental Model: The Zen of Python',
                'instruccion_en': "Unlike other languages, Python is guided by an explicit set of software engineering principles known as 'The Zen of Python' (written by Tim Peters). Its most famous aphorisms include: 1. 'Beautiful is better than ugly': Code should be clean and pleasant to read and audit. 2. 'Explicit is better than implicit': Developer intentions should be clearly expressed without obscure magic. 3. 'Simple is better than complex': If a simple solution solves the problem, avoid needless complexity. 4. 'Readability counts': Code is read far more often than it is written; thus writing it with the reader (and your screen reader) in mind is a golden rule. In this learning environment, you will master coding under these exact professional standards. Press Enter or Alt + Right Arrow to advance to the verification quiz.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 3: Conceptual Check: Python Philosophy',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Consider readability and long-term maintenance.'],
                'pregunta_en': 'Which of the following is an essential guiding principle of the Zen of Python?',
                'opciones_en': ['Readability counts: code should be clear and easy for humans to understand.', 'Compress everything into a single massive line to save disk space.', 'Obscure program logic so that nobody else can understand it.'],
                'explicacion_en': "'Readability counts' is one of Python's foundational pillars, making it one of the cleanest and most accessible languages in the world.",
            },
        ]
    },
    4: {
        'titulo_en': 'Chapter 4: Accessible Programming: How a Blind Developer Codes with NVDA',
        'resumen_en': 'Demystify code: how to interact through plain text, keyboard navigation, and the spatial mental model of indentation.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Mental Model: Code is Pure Plain Text',
                'instruccion_en': "There is a common myth that software engineers work in visual environments packed with graphical icons and inaccessible visual windows. The technical reality is much simpler and profoundly accessible: a computer program is, at its core, a plain text file (like a Notepad file) ending with the '.py' extension. Writing code requires neither a mouse nor vision. A blind software engineer uses the exact same foundational tools as any top engineer: 1. A text editor to type instructions. 2. Arrow keys (up, down, left, right) to navigate line-by-line and character-by-character. 3. Control + Arrow keys to jump word-by-word. 4. The NVDA screen reader configured to announce critical punctuation symbols like quotes, parentheses, and colons. Press Enter or Alt + Right Arrow to learn the spatial concept of indentation.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Mental Model: Indentation and Tiflotechnical Perception',
                'instruccion_en': "In most programming languages like C or Java, code blocks are delimited by visual curly braces '{' and '}'. Python made an elegant architectural choice: code blocks are structured using Indentation (leading spaces at the start of a line). Under the official style guide (PEP 8), each indented block level consists of exactly 4 spaces. How does a blind developer perceive this? NVDA provides native accessibility features for code structure: - When navigating vertically with arrow keys, NVDA announces: '4 space indent', '8 space indent', or 'no indent'. - You can also configure NVDA to signal indentation with acoustic tones (NVDA Settings -> Document Formatting -> Announce indentation with tones): a higher-pitch tone signals deeper nesting, and a lower-pitch tone signals an unindent. In this add-on, we have also built acoustic indicators so you always have total certainty of code hierarchy. Press Enter or Alt + Right Arrow to advance to the verification quiz.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 3: Conceptual Check: Code Structure in Python',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the 4-space indent announced by NVDA.'],
                'pregunta_en': 'How does Python define which statements belong to an inner block?',
                'opciones_en': ['Through indentation (leading whitespace, standardly 4 spaces per nesting level).', 'By changing text colors to blue or red on screen.', 'By drawing a visual circle with the mouse around lines.'],
                'explicacion_en': 'Python uses strict indentation (4 spaces) to define logical blocks, making code structure completely measurable and audible through screen readers.',
            },
        ]
    },
    5: {
        'titulo_en': 'Chapter 5: Algorithmic Thinking, Problem Decomposition, and the Psychology of Debugging',
        'resumen_en': 'Learn to break complex problems into finite steps, master the universal software cycle, and view errors as valuable diagnostics.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Mental Model: The Algorithm and Universal Software Cycle',
                'instruccion_en': "An algorithm is an ordered, unambiguous, finite sequence of instructions designed to solve a problem or achieve a goal. Every software system on Earth, from a simple pocket calculator to a satellite navigation array, follows the 'Universal Software Cycle': 1. Input: Receiving data from outside sources (keyboard keypresses, audio streams, or network packets). 2. Memory: Temporary storage of data inside variables within RAM. 3. Processing: Mathematical and logical transformation of that data by the CPU (arithmetic, comparisons, decisions). 4. Output: Delivering the processed results externally (console text, audio speech, or files written to disk). Programming consists of explicitly designing what happens across these four phases. Press Enter or Alt + Right Arrow to learn about the psychology of debugging.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Mental Model: The Psychology of Debugging',
                'instruccion_en': "The greatest obstacle for anyone learning to code is neither mathematics nor syntax: it is frustration when encountering error messages. Beginners often think: 'An error occurred; I failed or broke the program'. In professional software engineering, an error is never a failure or lack of intellect: it is a high-precision diagnostic report. When Python cannot interpret a line, it halts execution and emits a 'Traceback' message specifying: - The exact file and line number where execution stopped. - The error type (for example, SyntaxError if you forgot a quote, or NameError if you referenced an undefined variable). In this tutor, pressing F4 places your cursor directly onto the error line so you can inspect and resolve it instantly. Experienced software engineers produce errors every few minutes; the only difference is they read the error diagnostic calmly to understand what the interpreter expects. Press Enter or Alt + Right Arrow to advance to the verification quiz.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 3: Conceptual Check: Software Cycle',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of the error as a helpful technical diagnostic.'],
                'pregunta_en': 'What is the correct mindset of a software developer when encountering an error message?',
                'opciones_en': ['Read the message calmly as a diagnostic report to identify the exact line requiring inspection.', 'Assume the computer is physically damaged and force power off.', 'Delete all written code and start over without reading the failure.'],
                'explicacion_en': 'An error message is accurate diagnostic telemetry guiding us to inspect, understand, and refine the software.',
            },
        ]
    },
    6: {
        'titulo_en': 'Chapter 6: Standard Output: Our First Communication (print)',
        'resumen_en': 'Learn to emit data to the standard output console and master the formal anatomy of a Python function call.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Anatomy of print()',
                'instruccion_en': 'Now that you understand the interpreter, you will craft your first formal instruction. To communicate from the program to the user, we send data through \'Standard Output\' (stdout). In Python, this is accomplished by invoking the built-in `print()` function. Let us dissect its anatomy: 1. The command identifier: `print` instructs the interpreter which routine to invoke. 2. The parentheses `(` and `)`: The invocation operators. Whatever is enclosed within them is the argument supplied to the routine. 3. Quotes `\'` or `"`: They inform Python that the enclosed data is a literal string. If you omit the quotes, Python attempts to locate an identifier in memory and raises a `NameError`. Press Enter or Alt + Right Arrow to inspect this code in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Emitting Your First Message',
                'instruccion_en': 'Inspect the code in the editor. Note the quotes and parentheses. Press Control + Enter to execute and hear the output through NVDA.',
                'pistas_en': ['Press Control + Enter to run the script.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Personalized Greeting',
                'instruccion_en': "Modify the string inside the quotes to include your name or profession (for example: 'Hello, programming student') and press Control + Enter.",
                'pistas_en': ['Ensure you keep the opening and closing single quotes around the text.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Two-Line Output',
                'instruccion_en': "Write two independent print() statements: the first displaying 'Starting system' and the second 'System ready'. Run with Control + Enter to verify.",
                'pistas_en': ["Use one line for print('Starting system') and the next for print('System ready')."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: String Delimiters',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Distinguish between literal text and memory variable identifiers.'],
                'pregunta_en': "Why are quotes required around the string inside print('Hola')?",
                'opciones_en': ['To inform Python it is a literal string and not an identifier in memory.', 'Because quotes accelerate CPU processing speed.', 'It is optional; quotes are never needed in Python.'],
                'explicacion_en': 'Without quotes, Python searches RAM for a variable with that identifier and raises a NameError if missing.',
            },
        ]
    },
    7: {
        'titulo_en': 'Chapter 7: Computer Memory: Variables and the Assignment Operator',
        'resumen_en': 'Understand how values are stored in RAM using variables and the official snake_case naming standard.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Variables as Memory Labels',
                'instruccion_en': "A program that only outputs fixed text lacks real utility. To process data, we must store values in RAM. A variable is a symbolic identifier referencing a specific memory location where a value lives. Picture RAM as a massive grid of lockers: creating a variable places a human-readable label onto a locker to retrieve its content whenever needed. To store a value, we employ the 'Assignment Operator', written as `=`. Critical rule: In programming, `=` does NOT signify mathematical equality; it means: 'Evaluate what is on the right and assign it to the identifier on the left'. Official convention (PEP 8): Variable names are written in lowercase with words separated by underscores (e.g. `nombre_usuario`), known as `snake_case`. Press Enter or Alt + Right Arrow to advance to the observation step.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Assigning and Accessing Variables',
                'instruccion_en': 'Observe how variable `tool` is assigned and passed to print() without quotes. Run with Control + Enter to hear the result.',
                'pistas_en': ['Notice that when printing a variable name, no quotes are used.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Changing the Stored Value',
                'instruccion_en': "Change the string assigned to `tool` to 'Accessible screen reader' and execute with Control + Enter.",
                'pistas_en': ['Keep the assignment to the variable tool.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Student Profile',
                'instruccion_en': 'Create a variable named `student` holding your name as a string. On the next line, display it using print(). Run with Control + Enter.',
                'pistas_en': ["Write: student = 'Your Name' and below print(student)."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The = Operator',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember = is assignment, not comparison.'],
                'pregunta_en': 'What action does the statement: edad = 20 perform?',
                'opciones_en': ['Assigns the value 20 to the variable named edad inside RAM.', 'Checks if variable edad is mathematically equal to 20.', 'Deletes the number 20 from the computer.'],
                'explicacion_en': 'The = operator performs an assignment: evaluating the right-hand value and storing it in the left-hand variable.',
            },
        ]
    },
    8: {
        'titulo_en': 'Chapter 8: Documentation and Readability: Comments with #',
        'resumen_en': 'Learn to document your code intentions with comments ignored by the interpreter yet vital for human understanding.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The Hash Character (#)',
                'instruccion_en': "Source code is read not only by machines, but primarily by human beings. We frequently need explanatory annotations to record why a specific routine was chosen or to guide teammates. In Python, any line or snippet beginning with the hash symbol `#` is a 'Comment'. The Python interpreter completely ignores everything to the right of `#` until the end of that line. How does NVDA interact with comments? Your screen reader will announce 'hash' or 'comment' followed by the text, allowing you to audit code purpose without affecting execution. Press Enter or Alt + Right Arrow to inspect comments in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Documented Code',
                'instruccion_en': 'Inspect the code. Note that lines starting with # produce no console output. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Adding Your Own Note',
                'instruccion_en': "Add a new line at the top with your own comment (for instance: '# Author: my name') and execute with Control + Enter.",
                'pistas_en': ['Start the line with the # character.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Commenting Out Obsolete Code',
                'instruccion_en': 'The editor contains two print() calls. Place a # symbol at the start of the first line to disable it, so only the second line executes. Press Control + Enter.',
                'pistas_en': ["Prepend # to the first line: # print('Old message...')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Behavior of Comments',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the interpreter skips these lines.'],
                'pregunta_en': 'What action does the Python interpreter take when encountering the # symbol?',
                'opciones_en': ['Ignores all remaining text on that line and proceeds to the next.', 'Raises a SyntaxError and halts the program.', 'Prints the comment to the console with a low-pitch sound.'],
                'explicacion_en': 'Comments are completely skipped by the interpreter; they exist strictly for human understanding.',
            },
        ]
    },
    9: {
        'titulo_en': 'Chapter 9: Variable Reassignment and Sequential Memory Flow',
        'resumen_en': 'Learn how the interpreter executes top-to-bottom and how reassignment updates variable states in RAM.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Top-to-Bottom Flow and Overwriting',
                'instruccion_en': 'The Python interpreter executes statements in strict sequential order: top-to-bottom and left-to-right. Variables in RAM are dynamic. If you assign a new value to an existing variable with `=`, the previous value is discarded and replaced by the new one. For example: if on line 1 you state `puntos = 10` and on line 3 you write `puntos = 20`, upon reaching line 4 `puntos` holds 20. Mentally tracking how variable values evolve as execution proceeds line-by-line is one of the most vital analytical competencies of a professional engineer. Press Enter or Alt + Right Arrow to observe reassignment in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Two States Across Time',
                'instruccion_en': 'Observe how variable `status` changes between line 1 and line 3. Press Control + Enter to hear the two successive outputs.',
                'pistas_en': ['Press Control + Enter to see the variable evolution.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Updating the Final State',
                'instruccion_en': "Modify the second assignment so `status` becomes 'Successful operation in NVDA' and run with Control + Enter.",
                'pistas_en': ['Reassign variable status on line 3.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Game Score Tracker',
                'instruccion_en': 'Create variable `puntuacion = 0`. Print its value. Then reassign `puntuacion = 100` and print its value again. Run with Control + Enter.',
                'pistas_en': ['Write puntuacion = 0, print(puntuacion), puntuacion = 100, print(puntuacion).'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Lifecycle of Reassignment',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of overwriting the memory slot content.'],
                'pregunta_en': 'If variable x holds 5 on line 1 and you assign x = 12 on line 2, what value does x hold on line 3?',
                'opciones_en': ['It holds 12, because the latest assignment overwrites the previous value.', 'It holds 17, because Python implicitly sums previous assignments.', 'It holds 5, because variables are permanently immutable.'],
                'explicacion_en': 'Variables in Python reflect the value of the most recently executed assignment statement.',
            },
        ]
    },
    10: {
        'titulo_en': 'Chapter 10: Integers (int) and Arithmetic Operators',
        'resumen_en': 'Learn to perform mathematical computations with integers and master operator precedence rules (PEMDAS).',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The int Type and Basic Arithmetic',
                'instruccion_en': 'In Python, numbers without fractional parts belong to the `int` (integer) data type. They can be positive, negative, or zero. Python provides standard arithmetic operators: - Addition: `+` - Subtraction: `-` - Multiplication: `*` (asterisk) - Exponentiation: `**` (double asterisk, e.g. `2 ** 3` evaluates to 8). Precedence Rule (PEMDAS): Just like in algebra, Python evaluates Parentheses first, then Exponents, then Multiplication and Division, and lastly Addition and Subtraction. For example: in `2 + 3 * 4`, it first computes `3 * 4 = 12` and then adds 2, resulting in 14. To compute the addition first, use parentheses: `(2 + 3) * 4 = 20`. Press Enter or Alt + Right Arrow to inspect this arithmetic in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Computation and Precedence',
                'instruccion_en': 'Inspect how `resultado` is computed and printed. Press Control + Enter to hear the output.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Parentheses for Precedence',
                'instruccion_en': 'Compute the average of three grades by summing inside parentheses and dividing: `promedio = (8 + 9 + 10) // 3`. Print the result and press Control + Enter.',
                'pistas_en': ['Use parentheses to ensure summation precedes division.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Rectangle Perimeter',
                'instruccion_en': 'Declare `ancho = 6` and `alto = 4`. Compute the perimeter using `perimetro = 2 * (ancho + alto)`. Print `perimetro` and run with Control + Enter.',
                'pistas_en': ['Define ancho = 6, alto = 4, perimetro = 2 * (ancho + alto), and print(perimetro).'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Arithmetic Precedence',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Compute 2 * 3 first.'],
                'pregunta_en': 'What is the evaluated result of: 5 + 2 * 3?',
                'opciones_en': ['11, because multiplication (2 * 3 = 6) takes precedence over addition (+ 5).', '21, because it evaluates strictly left-to-right ignoring operator ranks.', '10, because numbers round to the nearest decade.'],
                'explicacion_en': 'In Python and mathematics, multiplication executes before addition unless overridden by parentheses.',
            },
        ]
    },
    11: {
        'titulo_en': 'Chapter 11: Floating-Point Decimals (float) and Divisions',
        'resumen_en': "Differentiate integers from decimals and master Python's three division forms: true (/), floor (//), and modulo (%).",
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The float Type and the Three Division Operators',
                'instruccion_en': 'When a number includes a fractional decimal component, Python represents it as a `float` (floating-point number). Screen reader note: In international software, always use the decimal PERIOD `.` rather than a comma `,` (for instance, `3.14`). Commas are reserved for separating arguments and collection items. Python offers three distinct division operators: 1. True Division `/`: Always yields a `float`, even when dividing evenly. For example: `10 / 2` produces `5.0`. 2. Floor / Integer Division `//`: Truncates fractional digits and returns the integer quotient. For example: `10 // 3` returns `3`. 3. Modulo / Remainder `%`: Returns the remainder of floor division. For example: `10 % 3` yields `1` (since 3 goes into 10 three times with 1 left over). Modulo is critical for determining parity (odd/even) and cyclical algorithms. Press Enter or Alt + Right Arrow to hear these three operations in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Comparing the Three Divisions',
                'instruccion_en': 'Run with Control + Enter and listen closely to how each operator yields distinct results for the identical operands.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Working with Decimal Prices',
                'instruccion_en': 'Compute the final discounted price: `price = 49.99`, `discount = 10.50`, `total = price - discount`. Print `total` and run with Control + Enter.',
                'pistas_en': ['Run with Control + Enter to observe decimal subtraction.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Fair Candy Distribution',
                'instruccion_en': 'You have `candies = 23` and `children = 5`. Calculate how many whole candies each child gets (`per_child = candies // children`) and the remainder (`leftovers = candies % children`). Print both and run with Control + Enter.',
                'pistas_en': ['Use // for per_child and % for leftovers, then print(per_child) and print(leftovers).'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The Modulo Operator (%)',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Multiply 5 * 3 and determine the gap to 17.'],
                'pregunta_en': 'What does the expression 17 % 5 evaluate to?',
                'opciones_en': ['2, because 5 fits into 17 three times (15) with a remainder of 2.', '3.4, because it represents exact decimal division.', '0, because division has no remainder.'],
                'explicacion_en': 'The % operator yields strictly the integer remainder after floor division.',
            },
        ]
    },
    12: {
        'titulo_en': 'Chapter 12: Character Strings (str): Delimiters, Escape Sequences, and Newlines',
        'resumen_en': 'Master text string manipulation (str), nested quotes, and escape sequences such as \\n and \\t.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Special Characters and the Backslash',
                'instruccion_en': 'In Python, any sequence of characters enclosed in matching single `\'...\'` or double `"..."` quotes is a `str` (string) object. What happens if your text needs to contain quotation marks inside? If you delimit the outer string with double quotes, you can use single quotes inside freely: `"He said \'hello\' and smiled"`. Escape Sequences with the Backslash `\\`: The backslash `\\` is the escape character, signaling that the following character holds a special control meaning: - `\\n`: Inserts an immediate Line Break, causing screen readers to verbalize a new line. - `\\t`: Inserts a horizontal Tabulation space. - `\\\'` or `\\"`: Embeds a literal quotation mark without terminating the string delimiter. Press Enter or Alt + Right Arrow to observe newline formatting in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Line Break with \\n',
                'instruccion_en': 'Notice how a single print() outputs two distinct lines using \\n. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to hear both lines.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Nested Mixed Quotes',
                'instruccion_en': 'Print a sentence containing internal quotes using outer double quotes: `print("The language \'Python\' is accessible")`. Run with Control + Enter.',
                'pistas_en': ['Use double quotes outside and single quotes inside.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Three-Row Menu',
                'instruccion_en': "Create variable `menu` containing three options separated by `\\n`: '1. Open\\n2. Save\\n3. Exit'. Display it with print(menu). Run with Control + Enter.",
                'pistas_en': ["Write menu = '1. Open\\n2. Save\\n3. Exit' and then print(menu)."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Escape Sequences',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ["Think of 'newline' preceded by a backslash."],
                'pregunta_en': 'Which control sequence creates an immediate newline inside a string?',
                'opciones_en': ['\\n (backslash followed by letter n)', '/enter (forward slash with enter)', '#linea (hash with linea)'],
                'explicacion_en': '\\n is the universal newline sequence across C-derived languages and Python.',
            },
        ]
    },
    13: {
        'titulo_en': 'Chapter 13: Modern String Interpolation: F-Strings',
        'resumen_en': 'Learn the modern professional standard for blending text and variables smoothly without clumsy casting using f-strings.',
        'pasos': [
            {
                'titulo_en': "Step 1: Foundational Concept: The 'f' Prefix and Braces {}",
                'instruccion_en': "In legacy Python, blending variables with text required concatenating with `+` and explicitly wrapping numbers with `str()` (e.g. `'Age: ' + str(age)`), which was verbose and prone to `TypeError`. Starting with Python 3.6, the industry embraced **Formatted String Literals** or **f-strings**. How do f-strings work? 1. Place a lowercase `f` immediately preceding the opening quote: `f'...'`. 2. Inside the string, insert curly braces `{}` around any variable or expression. 3. The interpreter automatically evaluates the expression inside the braces, casts it to string, and interpolates it seamlessly. Example: If `nombre = 'Kevin'`, writing `f'Welcome, {nombre}'` produces `'Welcome, Kevin'`. F-strings represent the gold standard of readability in modern Python codebases. Press Enter or Alt + Right Arrow to observe them in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Interpolating Multiple Variables',
                'instruccion_en': 'Inspect how text, numbers, and variables blend inside a single f-string. Press Control + Enter to execute.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Mathematical Expressions Inside Braces',
                'instruccion_en': "Inside curly braces you can execute arithmetic expressions directly. Modify the code to compute double: `f'El doble de {valor} es {valor * 2}'`. Run with Control + Enter.",
                'pistas_en': ['Write the expression valor * 2 inside the second set of curly braces.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Financial Summary with F-Strings',
                'instruccion_en': "Create `producto = 'Teclado'`, `precio = 35`, and `cantidad = 2`. Output using a single f-string: 'Producto: Teclado, Total: 70' computing `precio * cantidad` inside braces. Run with Control + Enter.",
                'pistas_en': ["Use print(f'Producto: {producto}, Total: {precio * cantidad}')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: F-String Syntax',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ["It is the initial of 'format'."],
                'pregunta_en': 'Which letter must precede the opening quotation mark to enable an f-string?',
                'opciones_en': ['The letter f (lowercase or uppercase)', 'The letter p (for print)', 'The percent sign %'],
                'explicacion_en': "The prefix f tells Python's lexer to evaluate expressions enclosed in curly braces.",
            },
        ]
    },
    14: {
        'titulo_en': 'Chapter 14: Data Input (input) and Explicit Type Casting',
        'resumen_en': 'Learn to pause execution to capture user keystrokes and master type casting using int(), float(), and str().',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The Golden Rule of input() and Type Casting',
                'instruccion_en': "To receive input from the user, Python provides the built-in `input()` function. When the interpreter encounters `input('Enter something: ')`, it pauses execution and waits for keyboard input followed by the Enter key. **The Golden Rule of input():** Regardless of what the user types (even numbers like `25` or `100`), `input()` ALWAYS returns a string (`str`). Attempting arithmetic directly on an `input()` result raises a `TypeError` because Python forbids implicit string-number addition. Explicit Type Conversion (*Type Casting*): To convert data across types, we use type constructor functions: - `int('25')`: Converts string '25' to integer 25. - `float('19.99')`: Converts string '19.99' to float 19.99. - `str(100)`: Converts integer 100 to string '100'. Press Enter or Alt + Right Arrow to observe casting in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Converting String to Number',
                'instruccion_en': 'Observe how textual numeric input is cast to integer using int() prior to calculation. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Summing Two Casted Numbers',
                'instruccion_en': "Set `num1_str = '50'` and `num2_str = '25'`. Cast them to integers and compute `suma = int(num1_str) + int(num2_str)`. Print suma and press Control + Enter.",
                'pistas_en': ['Ensure you wrap both strings with int().'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Double and Half Calculator',
                'instruccion_en': "Given `entrada = '80'`, cast it to an integer `numero`. Then compute `doble = numero * 2` and `mitad = numero // 2`. Print: 'Doble: 160, Mitad: 40'. Press Control + Enter.",
                'pistas_en': ["numero = int(entrada), doble = numero * 2, mitad = numero // 2, print(f'Doble: {doble}, Mitad: {mitad}')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Return Type of input()',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the golden rule of input().'],
                'pregunta_en': "What data type is ALWAYS returned by Python's input() function?",
                'opciones_en': ['str (character string), even if the user types numeric digits.', 'int (integer) automatically whenever digits are detected.', 'bool (boolean True or False).'],
                'explicacion_en': 'input() captures keystrokes as raw textual characters; therefore casting with int() or float() is always required for calculations.',
            },
        ]
    },
    15: {
        'titulo_en': 'Chapter 15: The Boolean Type (bool) and Relational Comparison Operators',
        'resumen_en': 'Learn the two binary truth states (True and False) and master the six relational comparison operators.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Binary Truth and Relational Operators',
                'instruccion_en': "Every computational branch boils down to a logical proposition with exactly two outcomes: True or False. In Python, this data type is called `bool` (boolean, honoring mathematician George Boole) and accepts strictly two capitalized literals: `True` and `False`. To compare operands and yield a boolean value, we utilize 'Relational Operators': - `==` (double equals): Evaluates whether two values are equal. (Caution: single `=` assigns in memory; double `==` tests equality). - `!=` (exclamation equals): Evaluates whether two values are not equal. - `<` (less than) and `>` (greater than). - `<=` (less than or equal to) and `>=` (greater than or equal to). Press Enter or Alt + Right Arrow to inspect these comparisons in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Evaluating Comparisons',
                'instruccion_en': 'Run the code with Control + Enter and hear how Python evaluates each comparison to True or False.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Legal Age Verification',
                'instruccion_en': 'Create `edad = 20`. Evaluate the boolean expression `es_mayor = edad >= 18` and print `es_mayor`. Press Control + Enter.',
                'pistas_en': ['Use the >= operator to compare with 18.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Password Equality Validator',
                'instruccion_en': "Given `clave_guardada = 'python2026'` and `clave_ingresada = 'python2026'`. Compare them with `acceso_concedido = (clave_guardada == clave_ingresada)`. Print `acceso_concedido` and run with Control + Enter.",
                'pistas_en': ['acceso_concedido = (clave_guardada == clave_ingresada), then print(acceso_concedido).'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Difference Between = and ==',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember single equals assigns.'],
                'pregunta_en': 'What is the critical technical distinction between = and == in Python?',
                'opciones_en': ['= assigns a value to a variable in RAM; == evaluates equality between two values.', 'They are identical and completely interchangeable.', '= is for numeric data and == is for strings.'],
                'explicacion_en': 'Confusing assignment (=) with relational equality (==) is a common beginner pitfall; Python strictly differentiates them.',
            },
        ]
    },
    16: {
        'titulo_en': 'Chapter 16: Logical Operators (and, or, not) and Truth Tables',
        'resumen_en': 'Learn to combine compound conditions through conjunctions, disjunctions, and inversions with short-circuit evaluation.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Logical Connectors and Short-Circuiting',
                'instruccion_en': 'In real-world systems, decisions rarely depend on an isolated factor. To evaluate compound propositions, Python provides three reserved keywords: 1. `and` (Logical AND): Demands that BOTH conditions be true to yield `True`. If either operand is false, the compound expression yields `False`. 2. `or` (Logical OR): Requires AT LEAST ONE condition to be true to yield `True`. It yields `False` only if both operands are false. 3. `not` (Logical Negation): Inverts truth value. If an expression is `True`, `not True` evaluates to `False`, and vice versa. Short-Circuit Evaluation: Python optimizes execution: in `A and B`, if `A` evaluates to False, Python immediately halts further evaluation and returns False without computing `B`. Similarly, in `A or B`, if `A` is True, it immediately returns True. Press Enter or Alt + Right Arrow to observe logical operators in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Truth Tables in Action',
                'instruccion_en': "Run with Control + Enter and analyze how 'and' demands simultaneous truth while 'or' requires only one match.",
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Negation with not',
                'instruccion_en': 'Verify if a system is idle: `bloqueado = False`, `disponible = not bloqueado`. Print `disponible` and press Control + Enter.',
                'pistas_en': ['not False becomes True.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: University Scholarship Eligibility',
                'instruccion_en': 'A student qualifies for a scholarship if average is >= 90 AND attendance is >= 85%. Declare `promedio = 92`, `asistencia = 90`, and evaluate `obtiene_beca = (promedio >= 90) and (asistencia >= 85)`. Print `obtiene_beca` and run with Control + Enter.',
                'pistas_en': ['Use the and operator to join both comparisons.'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The and Operator Evaluation',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Both conditions must hold simultaneously.'],
                'pregunta_en': 'What does the boolean expression: True and False evaluate to?',
                'opciones_en': ['False, because the and operator requires both operands to be True.', 'True, because at least one operand is True.', 'None, because the logic produces an unresolved tie.'],
                'explicacion_en': 'The and operator produces True if and only if all connected operands evaluate to True.',
            },
        ]
    },
    17: {
        'titulo_en': 'Chapter 17: Conditional Branching: The if Statement and 4-Space Indentation',
        'resumen_en': "Learn to branch program execution and master Python's golden rule: colons (:) and mandatory indentation.",
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The if Statement and Colons (:)',
                'instruccion_en': "Up to this point, our programs have executed strictly linearly. Conditional branching enables a program to choose different pathways based on data. The primary branching statement in Python is `if`. Anatomy of an if block: 1. Type the keyword `if` followed by a boolean condition. 2. Terminate the header line with a mandatory Colon `:`. 3. Indent statements intended to execute ONLY when the condition is true by exactly 4 spaces. Auditing indentation with NVDA: Navigating vertically down into an `if` block, NVDA announces: '4 space indent' (or plays a higher-pitch acoustic cue). Omitting either the colon or indentation results in an `IndentationError` or `SyntaxError`. Press Enter or Alt + Right Arrow to inspect your first if block in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Conditional Execution and Indentation',
                'instruccion_en': 'Observe the 4 spaces of indentation on line 2. Run with Control + Enter to hear the authorized message.',
                'pistas_en': ['Notice the colon at the end of the if statement line.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Condition Not Met',
                'instruccion_en': 'Change `edad = 15`. Upon running with Control + Enter, `edad >= 18` evaluates to False, skipping the indented line. Verify this behavior.',
                'pistas_en': ['Run with Control + Enter and verify no output is emitted.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Temperature Alert',
                'instruccion_en': "Create `temperature = 35`. Write an if statement testing if `temperature > 30:`. Inside the 4-space indented block, print: 'Alert: High temperature'. Press Control + Enter.",
                'pistas_en': ["if temperature > 30: followed on the next line by 4 spaces and print('Alert: High temperature')."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Trailing Character on if Header',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It introduces the indented block.'],
                'pregunta_en': 'Which punctuation character is strictly required at the end of an if header line?',
                'opciones_en': ['Colon (:)', 'Semicolon (;)', 'Question mark (?)'],
                'explicacion_en': 'In Python, all compound statement headers (if, else, for, while, def, class) must terminate with a colon (:).',
            },
        ]
    },
    18: {
        'titulo_en': 'Chapter 18: The Alternative Pathway: The else Clause',
        'resumen_en': 'Learn to define fallback execution branches when conditions evaluate to false using the else block.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The Complete Binary Decision',
                'instruccion_en': "A standalone `if` acts only when true; otherwise, execution flows past it. However, most algorithms require a fallback: 'If condition A holds, do X; OTHERWISE, do Y'. We implement this using the `else:` clause. Rules for the else clause: 1. It aligns at the exact indentation level of the matching `if`. 2. It must terminate with a colon `:`. 3. Its body statements indent by 4 spaces. 4. The `else` clause NEVER takes a condition; it triggers automatically whenever the preceding `if` condition evaluates to False. Press Enter or Alt + Right Arrow to observe if/else in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: The Binary Branch',
                'instruccion_en': 'Inspect the if/else structure. Because edad is 16, the condition fails, executing the else block. Run with Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Shifting Flow to the if Branch',
                'instruccion_en': "Modify `edad = 25`. Upon running with Control + Enter, the first branch ('Access granted') triggers, skipping the else block.",
                'pistas_en': ['Change edad to 25 and press Control + Enter.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Even/Odd Parity Classifier',
                'instruccion_en': "Given `numero = 14`, use modulo `% 2 == 0` to test parity. If even print: 'The number is even'. Otherwise (else), print: 'The number is odd'. Press Control + Enter.",
                'pistas_en': ["if number % 2 == 0: print('The number is even') else: print('The number is odd')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: When else Executes',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It acts as the fallback contingency.'],
                'pregunta_en': 'When do statements enclosed in an else block execute?',
                'opciones_en': ['Only when the preceding if condition evaluated to False.', 'Always, regardless of the if condition result.', 'Only when a syntax error exists in the script.'],
                'explicacion_en': 'The else block is the automatic fallback pathway executed whenever the if test evaluates to false.',
            },
        ]
    },
    19: {
        'titulo_en': 'Chapter 19: Multi-Way Conditional Branching: elif Blocks',
        'resumen_en': 'Learn to categorize complex decision trees with mutually exclusive alternatives using elif.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The Decision Cascade with elif',
                'instruccion_en': 'What happens when we encounter more than two mutually exclusive outcomes? For example: a traffic signal can be green, yellow, or red. Instead of nesting clumsy if statements, Python provides the `elif` keyword (short for *else if*). Execution flow of an `if / elif / else` cascade: 1. Python tests the initial `if`. If true, it executes its block and EXITS the entire compound structure immediately. 2. If the initial `if` was false, it moves to the first `elif` and evaluates its condition. 3. You can chain as many `elif` blocks as your domain logic requires. 4. If no `if` or `elif` evaluated to true, the trailing `else` executes as the catch-all safety net. Press Enter or Alt + Right Arrow to observe an elif cascade.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Grade Classification',
                'instruccion_en': 'Inspect the cascade. Because puntaje is 75, the if (>= 90) fails, activating the elif (>= 70). Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Triggering the Top Branch',
                'instruccion_en': 'Modify `puntaje = 95`. Run with Control + Enter and observe how the top branch triggers without inspecting subsequent branches.',
                'pistas_en': ['Change puntaje to 95 and execute.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Three-Tier Thermal Classifier',
                'instruccion_en': "Given `temp = 22`: if `temp > 28` print 'Clima cálido'; elif `temp >= 15` print 'Clima templado'; else print 'Clima frío'. Run with Control + Enter.",
                'pistas_en': ["if temp > 28: print('Clima cálido') elif temp >= 15: print('Clima templado') else: print('Clima frío')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: elif Short-Circuit Behavior',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember only one pathway is chosen.'],
                'pregunta_en': 'If the initial if condition evaluates to True in a chain with several elif clauses, what happens to the subsequent elif blocks?',
                'opciones_en': ['They are completely skipped, and execution resumes past the compound structure.', 'All of them execute unconditionally one after the other.', 'The program reboots from line 1.'],
                'explicacion_en': 'if/elif branches are mutually exclusive: as soon as one branch evaluates to True, all alternatives are bypassed.',
            },
        ]
    },
    20: {
        'titulo_en': 'Chapter 20: Definite Iteration: The for Loop and range()',
        'resumen_en': 'Learn to automate repetitive workflows iterating across numeric sequences using for loops and range().',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Iteration and the range() Function',
                'instruccion_en': "A core strength of computing systems is their ability to repeat operations millions of times without fatigue or deviation. A 'Loop' is a construct that executes a statement block repeatedly. The `for` loop is utilized when the repetition count is predetermined or when traversing an iterable sequence. The `range()` Function: `range()` constructs an immutable arithmetic progression of integers: - `range(stop)`: Starts at 0 and stops at `stop - 1`. E.g. `range(5)` yields 0, 1, 2, 3, 4. - `range(start, stop)`: Starts at `start` and stops at `stop - 1`. E.g. `range(1, 6)` yields 1, 2, 3, 4, 5. - `range(start, stop, step)`: The third parameter specifies the step increment. E.g. `range(0, 10, 2)` produces evens: 0, 2, 4, 6, 8. Across each iteration pass, the loop variable binds to the next sequential value and executes the 4-space indented body. Press Enter or Alt + Right Arrow to inspect the for loop in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Repeating with for and range()',
                'instruccion_en': 'Observe how the loop repeats print() five times updating variable `i`. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Stepping by Two',
                'instruccion_en': 'Generate even numbers using the step argument: `range(2, 11, 2)`. Print each number and press Control + Enter.',
                'pistas_en': ['The range spans from 2 to 10 stepping by 2.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Sum Accumulator',
                'instruccion_en': 'Initialize `total = 0`. With `for n in range(1, 6):`, add each number to the accumulator via `total += n`. After the loop (unindented), print: print(total). Press Control + Enter.',
                'pistas_en': ['1 + 2 + 3 + 4 + 5 = 15. Ensure print(total) is unindented outside the loop.'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Upper Bound of range()',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['The stop integer is left out.'],
                'pregunta_en': 'What sequence of integers does range(1, 5) produce exactly?',
                'opciones_en': ['1, 2, 3, 4 (the stop bound 5 is exclusive)', '1, 2, 3, 4, 5 (inclusive of 5)', '0, 1, 2, 3, 4, 5'],
                'explicacion_en': 'In Python, ranges and slices are half-open intervals [start, stop): the stop boundary is strictly excluded.',
            },
        ]
    },
    21: {
        'titulo_en': 'Chapter 21: Conditional Iteration: The while Loop',
        'resumen_en': 'Learn to execute conditional repetition workflows governed by dynamic predicates using the while loop.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Predicate-Driven Loops',
                'instruccion_en': 'While `for` loops iterate across known intervals or containers, `while` loops execute dynamically as long as a predicate remains true. A `while` loop checks its boolean predicate prior to every pass: - If the condition evaluates to `True`, it runs the 4-space indented body. - Execution loops back up to re-evaluate the condition. - The moment the predicate becomes `False`, iteration terminates immediately. Essential anatomy of a robust while loop: 1. Initialization: Establish a loop control variable prior to entry (e.g. `contador = 1`). 2. Predicate: The condition checked on each pass (e.g. `while contador <= 5:`). 3. Step / Mutation: Mutating the control variable within the loop body (e.g. `contador += 1`). Omitting mutation results in an infinite loop. Press Enter or Alt + Right Arrow to observe the while loop in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Controlled Progressive Counter',
                'instruccion_en': 'Observe how `contador` initializes at 1, increments each pass with `contador += 1`, and exits upon reaching 4. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Countdown Timer',
                'instruccion_en': "Create a countdown starting at `cuenta = 5`, decrementing with `cuenta -= 1` while `cuenta > 0`, and printing '¡Despegue!' on exit. Press Control + Enter.",
                'pistas_en': ['Ensure you decrement cuenta on each pass.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Exponential Doubler',
                'instruccion_en': 'Start with `energia = 1`. With `while energia < 30:`, print `energia` and double it each iteration using `energia *= 2`. Run with Control + Enter.',
                'pistas_en': ['while energia < 30: print(energia) energia *= 2'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The Hazard of Infinite Loops',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Consider a condition that never changes.'],
                'pregunta_en': 'What happens if you omit updating the loop control variable inside a while loop body?',
                'opciones_en': ['The condition never evaluates to False, repeating indefinitely (infinite loop).', 'Python immediately shuts down the monitor.', 'The loop automatically converts into a for loop.'],
                'explicacion_en': 'Without control variable mutation, the predicate remains permanently true, exhausting CPU cycles.',
            },
        ]
    },
    22: {
        'titulo_en': 'Chapter 22: Infinite Loop Prevention and Process Interruption',
        'resumen_en': 'Learn to diagnose runaway infinite loops, understand execution timeouts, and safely interrupt stuck processes.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Anatomy of Runaway Loops and Safety Timeouts',
                'instruccion_en': "An infinite loop occurs when a loop's exit predicate can never be satisfied. For example: `while True:` without a break, or a counter decrementing away from its terminal bound. When this happens, the CPU spins executing billions of redundant instructions, causing the UI to freeze. Protection Mechanisms in Professional Engineering: To prevent runaway scripts from freezing NVDA or your operating system, this learning environment runs an 'Execution Timeout Watchdog'. If a script exceeds 4 seconds without returning, the execution runner safely halts the process and notifies you via speech: 'Execution timeout exceeded (possible infinite loop)'. In standard command-line shells, the universal shortcut to terminate a running script is `Control + C`. Press Enter or Alt + Right Arrow to inspect how a defective loop is corrected.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Fixing a Flawed Loop',
                'instruccion_en': 'Inspect the code. Notice how line `paso += 1` guarantees that `paso < 5` evaluates to False after 4 passes. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Adding the Missing Exit Increment',
                'instruccion_en': 'In the editor code, add `nivel += 1` inside the while body so the loop advances toward bound 4 and terminates cleanly. Run with Control + Enter.',
                'pistas_en': ['Ensure nivel += 1 is indented with 4 spaces.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Safe Battery Charge Simulation',
                'instruccion_en': "Simulate battery charging: `bateria = 70`. Using `while bateria < 100:`, increment `bateria += 10`. Outside the loop, print: print(f'Carga completa: {bateria}%'). Run with Control + Enter.",
                'pistas_en': ["while bateria < 100: bateria += 10, and unindented print(f'Carga completa: {bateria}%')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Universal Interrupt Shortcut',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It is the universal cancellation command in shells.'],
                'pregunta_en': 'Which key combination sends an interrupt signal (KeyboardInterrupt) to a running script in a terminal?',
                'opciones_en': ['Control + C', 'Alt + F4', 'Spacebar'],
                'explicacion_en': 'Control + C issues a standard KeyboardInterrupt signal halting execution across operating system shells.',
            },
        ]
    },
    23: {
        'titulo_en': 'Chapter 23: Advanced Loop Control: break, continue, and Loop else',
        'resumen_en': 'Learn to terminate searches early using break and skip selective iterations using continue.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Interruption with break and Skipping with continue',
                'instruccion_en': 'We frequently require precise control within an iteration loop rather than passively waiting for the sequence to exhaust. Python provides two vital jump statements: 1. `break`: Immediately halts and exits the loop. The instant Python executes `break`, it jumps out of the loop construct to the next unindented line. It is foundational in search algorithms: once the target is located, further CPU cycles are saved. 2. `continue`: Skips the remainder of the current iteration body and jumps straight to the next pass. The Loop `else` Clause: A unique Python idiom: loops can have an `else:` block. This block executes ONLY if the loop completed naturally without encountering a `break`. Press Enter or Alt + Right Arrow to observe these statements in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Early Exit with break',
                'instruccion_en': 'Observe how the range(1, 10) loop halts immediately upon locating 3 due to break. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Skipping Iterations with continue',
                'instruccion_en': 'Use continue to bypass odd numbers: if `n % 2 != 0: continue`. Notice only evens are printed. Run with Control + Enter.',
                'pistas_en': ['continue skips print for odd integers.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Halting on Negative Numbers',
                'instruccion_en': "Given `lecturas = [15, 22, -1, 30]`, iterate through items with `for val in lecturas:`. If `val < 0`, print 'Lectura anómala detectada' and exit with `break`. Otherwise, print `val`. Press Control + Enter.",
                'pistas_en': ["if val < 0: print('Lectura anómala detectada') break else: print(val)"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The continue Statement',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Differentiate between aborting the whole loop and skipping a single pass.'],
                'pregunta_en': 'What occurs when the interpreter encounters a continue statement inside a loop?',
                'opciones_en': ['Skips remaining statements in the active pass and jumps straight to the next iteration.', 'Terminates and destroys the loop structure permanently.', 'Emits an error log and mutes the screen reader.'],
                'explicacion_en': "continue does not abort the loop (which is break's job); it merely bypasses the remainder of the current cycle.",
            },
        ]
    },
    24: {
        'titulo_en': 'Chapter 24: Lists (list): Ordered Collections, Indexing, and Mutability',
        'resumen_en': 'Learn to store multiple ordered values using square brackets [], zero-based indexing, and negative indexing.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Lists as Mutable Sequential Containers',
                'instruccion_en': "Until now, each variable referenced a single datum (one number or string). Managing 100 students or 500 store inventory items using discrete variables would be unsustainable. A **List** (`list`) is an ordered, mutable sequence of items delimited by square brackets `[` and `]`, separated by commas. Core characteristics of Python lists: 1. Zero-Based Indexing: The first item resides at index `0`, second at `1`, third at `2`. E.g. if `frutas = ['manzana', 'pera']`, `frutas[0]` accesses `'manzana'`. 2. Negative Indexing: Python allows counting backward: index `-1` accesses the final item, `-2` the penultimate. 3. Mutability: Unlike strings, lists are mutable. You can reassign any slot in-place: `frutas[0] = 'fresa'`. Press Enter or Alt + Right Arrow to observe lists in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Positive and Negative Indexing',
                'instruccion_en': 'Inspect the language list. Notice how `lenguajes[0]` accesses the first item and `lenguajes[-1]` the last. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Mutating an Element in-Place',
                'instruccion_en': "Mutate the second item (index 1) to become 'C++': `lenguajes[1] = 'C++'`. Print the list and press Control + Enter.",
                'pistas_en': ["Use lenguajes[1] = 'C++' to replace in memory."],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Three-Tool Collection',
                'instruccion_en': "Create list `herramientas` with: 'NVDA', 'Python', 'VSCode'. Print the first and last elements: `print(herramientas[0], herramientas[-1])`. Run with Control + Enter.",
                'pistas_en': ["herramientas = ['NVDA', 'Python', 'VSCode'] and print(herramientas[0], herramientas[-1])"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Index of First Element',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Counting always begins at zero.'],
                'pregunta_en': 'Which index references the very first element of any list in Python?',
                'opciones_en': ['0 (zero)', '1 (one)', '-0'],
                'explicacion_en': 'Python employs zero-based indexing: the offset from sequence start for the initial item is 0.',
            },
        ]
    },
    25: {
        'titulo_en': 'Chapter 25: Essential List Methods (append, insert, pop, remove, len)',
        'resumen_en': 'Learn to append, insert, delete, and query list size dynamically using built-in methods.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: List Mutation Methods',
                'instruccion_en': 'A Python list has dynamic capacity; it expands and contracts dynamically as requirements evolve. To modify lists, we invoke methods using dot notation (`lista.metodo()`): - `lista.append(item)`: Appends an item to the end of the list. - `lista.insert(index, item)`: Inserts an item at a specific index, shifting subsequent items rightward. - `lista.pop()`: Removes and returns the trailing element. Passing an index (`lista.pop(0)`) removes at that position. - `lista.remove(value)`: Searches and deletes the first occurrence of the specified value (raises ValueError if absent). - `len(lista)`: Built-in function returning the total element count. Press Enter or Alt + Right Arrow to observe these methods in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Growth and Measurement with append() and len()',
                'instruccion_en': 'Observe how list tareas grows via append() and measures via len(). Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Extracting Elements with pop()',
                'instruccion_en': 'Extract the last item with `eliminado = tareas.pop()`. Print `eliminado` and the remaining list. Run with Control + Enter.',
                'pistas_en': ['pop() returns the removed item.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Dynamic Queue Simulation',
                'instruccion_en': "Initialize `cola = ['Ana', 'Bernardo']`. Add 'Carlos' with append(). Then pop the first served customer with `cola.pop(0)`. Print `cola` and run with Control + Enter.",
                'pistas_en': ["cola.append('Carlos'), cola.pop(0), print(cola)"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The append() Method',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Appending to the tail.'],
                'pregunta_en': 'At which position does append(x) place the new element?',
                'opciones_en': ['At the very end of the list, increasing length by 1.', 'At the beginning of the list at index 0.', 'At a randomized position selected by the CPU.'],
                'explicacion_en': 'append() always appends to the tail of the list in amortized O(1) constant time.',
            },
        ]
    },
    26: {
        'titulo_en': 'Chapter 26: List Traversal and Iteration (for ... in and enumerate())',
        'resumen_en': 'Learn the idiomatic pattern to iterate across list items and leverage enumerate() to pair indices with values.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The for ... in Pattern and enumerate()',
                'instruccion_en': 'In legacy languages, traversing arrays required managing counter variables `i = 0` and dereferencing `lista[i]`. Python introduced a far cleaner idiomatic construct: `for elemento in lista:`. The interpreter handles extracting elements sequentially until the collection exhausts. The `enumerate()` Function: What if your logic requires both the element AND its index position? Wrapping a sequence with `enumerate(lista, start=1)` yields a pair on each iteration: `index, item`. This is exceptionally powerful in accessible software to format numbered lists verbalized clearly by screen readers. Press Enter or Alt + Right Arrow to observe list iteration.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Clean Sequential Traversal',
                'instruccion_en': 'Inspect how `for fruta in frutas:` extracts each string directly. Press Control + Enter to hear each item verbalized on its line.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Accessible Numbering with enumerate()',
                'instruccion_en': 'Use `enumerate(canales, start=1)` to format accessible numbered channels. Run with Control + Enter.',
                'pistas_en': ['Notice how start=1 numbers starting at 1 instead of 0.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Shopping Cart Total Sum',
                'instruccion_en': "Given `precios = [12.50, 8.00, 24.50]`, initialize `total = 0.0`. Iterate through prices adding each to `total`. Outside the loop, print: print(f'Total compra: {total}'). Run with Control + Enter.",
                'pistas_en': ["for p in precios: total += p, and unindented print(f'Total compra: {total}')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The enumerate() Function',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It yields the position and the datum.'],
                'pregunta_en': 'Which two values does enumerate(iterable) yield across each loop pass?',
                'opciones_en': ['The index integer and the corresponding item.', 'The first element and the final element.', 'The data type and its byte footprint in RAM.'],
                'explicacion_en': 'enumerate() yields (index, item) pairs, eliminating manual counter variables.',
            },
        ]
    },
    27: {
        'titulo_en': 'Chapter 27: Tuples (tuple): Immutability, Data Integrity, and Unpacking',
        'resumen_en': 'Learn to safeguard critical data using read-only tuples and master elegant multi-variable unpacking.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Tuples versus Lists and Immutability',
                'instruccion_en': 'In software engineering, permitting unrestricted mutability across collections is a vulnerability risk. For instance: sensor geolocation coordinates, fixed error constants, or screen dimension bounds. A **Tuple** (`tuple`) is an ordered, IMMUTABLE sequence delimited by parentheses `(` and `)`. Critical distinction from lists: Once instantiated, a tuple is frozen: items cannot be added, removed, or reassigned. Writing `tupla[0] = 5` raises a `TypeError`. Tuple Unpacking: Python enables unpacking all tuple items into discrete variables in a single statement: `lat, lon = (4.71, -74.07)`. This yields concise, performant, and defensively secure codebases. Press Enter or Alt + Right Arrow to observe tuples in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Creation and Unpacking of Tuples',
                'instruccion_en': 'Observe how tuple `resolucion = (1920, 1080)` unpacks into `ancho, alto`. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Verifying Tuple Immutability',
                'instruccion_en': 'Access index 0 of `coordenadas = (10, 25)` and print it via `print(coordenadas[0])`. Run with Control + Enter.',
                'pistas_en': ['Tuples support indexed reading [0] but forbid reassignment.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Unpacking a User Record',
                'instruccion_en': "Given tuple `usuario = ('Elena', 'Desarrolladora', 2026)`, unpack it into: `nombre, rol, anio = usuario`. Print: 'Elena es Desarrolladora desde 2026'. Press Control + Enter.",
                'pistas_en': ["nombre, rol, anio = usuario and print(f'{nombre} es {rol} desde {anio}')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Immutability of Tuples',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Immutability protects against mutation.'],
                'pregunta_en': 'What occurs if you attempt to mutate a tuple element via assignment (e.g. mi_tupla[0] = 99)?',
                'opciones_en': ["Python raises a TypeError stating that 'tuple' object does not support item assignment.", 'The tuple mutates seamlessly without error.', 'The item is appended to the tail of the tuple.'],
                'explicacion_en': 'Tuples are immutable by design; any attempt to reassign items raises a TypeError.',
            },
        ]
    },
    28: {
        'titulo_en': 'Chapter 28: Dictionaries (dict): Key-Value Mapping',
        'resumen_en': "Master Python's primary associative structure: high-speed key lookup using braces {} and safe retrieval with get().",
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Associative Mappings and Hash Tables',
                'instruccion_en': "In lists, values are indexed by numerical positions (`lista[0]`, `lista[1]`). In real-world software, information is associated by conceptual keys: an ID number maps to a name, a term to its definition, or a config flag to its value. A **Dictionary** (`dict`) is an associative mapping enclosed in curly braces `{` and `}` storing `key: value` pairs. Core dictionary mechanics: 1. Keyed Access: Instead of numeric offsets, pass the key inside square brackets: `persona['nombre']`. 2. Unique Keys: Keys are unique; assigning to an existing key updates its value. 3. Safe Retrieval with `.get()`: Direct access `d['missing']` raises a `KeyError`. Calling `d.get('clave', 'Default')` safely prevents crashes, returning fallback data if absent. Press Enter or Alt + Right Arrow to observe dictionaries in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Dictionary Creation and Lookup',
                'instruccion_en': 'Inspect how structured user data is mapped and queried by key. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Safe Retrieval with get() and Adding Keys',
                'instruccion_en': "Add a new key `config['braille'] = True` and safely query an unmapped key with `.get()`. Press Control + Enter.",
                'pistas_en': ['get() prevents the script from raising KeyError.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Professional Profile Record',
                'instruccion_en': "Create dictionary `perfil` with keys: `'nombre': 'Elena'`, `'rol': 'Programadora'`, and `'experiencia': 3`. Print: 'Elena es Programadora con 3 años de experiencia'. Run with Control + Enter.",
                'pistas_en': ['perfil = {\'nombre\': \'Elena\', \'rol\': \'Programadora\', \'experiencia\': 3}, print(f"{perfil[\'nombre\']} es {perfil[\'rol\']} con {perfil[\'experiencia\']} años de experiencia")'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Advantage of the get() Method',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of defensive crash prevention.'],
                'pregunta_en': "Why is it preferable to call diccionario.get('clave') instead of direct diccionario['clave']?",
                'opciones_en': ['Because if the key is missing, get() returns None or a fallback default without crashing with a KeyError.', 'Because get() automatically deletes the key after query.', 'Because get() operates strictly on integer keys.'],
                'explicacion_en': 'The get() method ensures defensive fault tolerance, avoiding KeyError crashes on missing keys.',
            },
        ]
    },
    29: {
        'titulo_en': 'Chapter 29: Custom Functions with def: DRY Principle and Modularity',
        'resumen_en': 'Learn to declare custom functions using def, package reusable logic blocks, and enforce the DRY principle.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The DRY Principle and Anatomy of def',
                'instruccion_en': "As codebases grow, copying the same 10-line routine across five separate files is a software engineering anti-pattern. The cornerstone principle of software design is **DRY** (*Don't Repeat Yourself*): every piece of knowledge must have a single authoritative representation. To encapsulate and reuse logic, we define custom **Functions** using the `def` keyword. Anatomy of a function definition: 1. The `def` keyword followed by the routine identifier in `snake_case`. 2. Parentheses `(` and `)` containing parameters (formal variables the function expects). 3. A mandatory colon `:` terminating the header line. 4. The function body indented by 4 spaces. Defining a function merely registers a recipe in memory; it will not execute until explicitly invoked by name with parentheses. Press Enter or Alt + Right Arrow to observe a function in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Definition and Invocation',
                'instruccion_en': 'Inspect `saludar_usuario(nombre)`. Observe how it is declared first and then invoked twice with distinct arguments. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Multi-Parameter Function',
                'instruccion_en': 'Create a function taking two parameters `mostrar_progreso(capitulo, total)`. Invoke it and press Control + Enter.',
                'pistas_en': ['Pass the two numbers inside parentheses when calling the function.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Rectangle Area Calculator Function',
                'instruccion_en': "Define function `calcular_area(base, altura):` calculating `area = base * altura` and printing `print(f'Área calculada: {area}')`. Call it with 7 and 6. Press Control + Enter.",
                'pistas_en': ["def calcular_area(base, altura): area = base * altura print(f'Área calculada: {area}') calcular_area(7, 6)"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The def Keyword',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It is a 3-letter keyword.'],
                'pregunta_en': 'Which reserved keyword is used in Python to declare a new function?',
                'opciones_en': ['def (short for define)', 'function', 'fn'],
                'explicacion_en': 'Python exclusively uses the 3-letter keyword def to define functions and methods.',
            },
        ]
    },
    30: {
        'titulo_en': 'Chapter 30: Returning Values (return) versus print()',
        'resumen_en': 'Master the vital distinction between outputting audio/screen text via print() and delivering computed data to RAM via return.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Why return is Not print',
                'instruccion_en': 'This is the single most widespread conceptual stumbling block for beginners: confusing `print()` with `return`. Understand the distinction deeply: - `print()`: An external communication effect. It sends characters to the display and NVDA speech synthesizer. But that datum is not captured in program state; the function hands nothing back to the caller (implicitly returning `None`). - `return`: An internal memory handover. It immediately terminates function execution and delivers the computed payload to the call site, allowing it to be assigned to a variable or chained into further computations. Rule of thumb: If human ears need to hear information, use `print()`; if downstream software needs to compute with the result, use `return`. Press Enter or Alt + Right Arrow to observe return in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Capturing the return Payload',
                'instruccion_en': 'Notice how function `cuadrado(x)` returns its payload via return and stores it in variable `res`. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Chaining Functions with return',
                'instruccion_en': "Observe how a function's return value passes directly into another arithmetic expression: `resultado = cuadrado(5) + 10`. Press Control + Enter.",
                'pistas_en': ['cuadrado(5) returns 25 and adds 10 = 35.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Legal Age Boolean Function',
                'instruccion_en': 'Define `es_adulto(edad):` returning the boolean `edad >= 18`. Store `es_adulto(21)` in `autorizado` and print(autorizado). Run with Control + Enter.',
                'pistas_en': ['def es_adulto(edad): return edad >= 18, autorizado = es_adulto(21), print(autorizado)'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Implicit Return Value',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ["Think of the English word for 'nothing'."],
                'pregunta_en': 'What value does a Python function return in memory if it only contains print() and lacks return?',
                'opciones_en': ["None (Python's singleton representing the absence of a value)", 'The number 0', "An empty string ''"],
                'explicacion_en': 'Any function without an explicit return statement implicitly returns None upon completion.',
            },
        ]
    },
    31: {
        'titulo_en': 'Chapter 31: Variable Scope: Local versus Global (The LEGB Rule)',
        'resumen_en': 'Learn the lifecycle and visibility of variables: why local identifiers exist strictly within their enclosing function.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Lexical Scope and Memory Isolation',
                'instruccion_en': "Scope defines the program region where an identifier is visible and resolved. Python divides scope into two fundamental tiers: 1. Local Scope: Any variable assigned within a function body is LOCAL to that function. It is born upon invocation and destroyed when the function returns. The outer program CANNOT inspect or mutate this local variable. 2. Global Scope: Variables assigned at the top-level script (unindented) are GLOBAL and can be read anywhere. Why does memory isolation exist? If all variables were global, different routines utilizing a variable named `contador` would overwrite each other's memory, causing catastrophic side effects. Python's LEGB Rule: Resolving names checks Local, Enclosing, Global, and Built-in scopes sequentially. Press Enter or Alt + Right Arrow to observe scope isolation.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Protected Local Variables',
                'instruccion_en': 'Notice how `mensaje_local` exists strictly inside the function and is returned outwards. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Global versus Local Variables',
                'instruccion_en': 'Inspect how global `version = 3` is safely read inside the routine without conflict. Run with Control + Enter.',
                'pistas_en': ["Functions can read global variables as long as they don't reassign them."],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Clean Parameter Passing',
                'instruccion_en': 'Avoid global state. Create function `calcular_iva(subtotal)` returning `subtotal * 0.19`. Store IVA of 200 in `iva` and print `iva`. Run with Control + Enter.',
                'pistas_en': ['def calcular_iva(subtotal): return subtotal * 0.19, iva = calcular_iva(200), print(iva)'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Lifecycle of Local Variables',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Local variables have ephemeral lifetimes.'],
                'pregunta_en': 'What occurs to a variable instantiated inside a function when that function concludes execution?',
                'opciones_en': ['It is destroyed and deallocated from RAM automatically.', 'It is saved permanently to secondary disk storage.', 'It automatically elevates to a globally accessible variable across the file.'],
                'explicacion_en': "Python's garbage collector deallocates local scope variables upon function frame completion.",
            },
        ]
    },
    32: {
        'titulo_en': 'Chapter 32: Professional Exception Handling: try, except, finally, and Tracebacks',
        'resumen_en': 'Learn to anticipate runtime failures defensively using try/except/finally and master accessible traceback reading with F4.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Anticipated Errors and try/except Blocks',
                'instruccion_en': "In production software, systems encounter volatile conditions: users type letters when numbers are requested, target files vanish, or networks drop. Without defensive guards, Python raises an uncaught 'Exception' and the process crashes abruptly. To engineer fault-tolerant software, we employ `try / except` blocks: 1. `try:` block: Houses the operations that may encounter runtime faults. 2. `except SpecificError:` block: Catches the expected exception class, allowing recovery without crashing. 3. `finally:` block (optional): Runs unconditionally whether a fault occurred or not (ideal for resource cleanup). Diagnostic Jump with F4: In this IDE, when an unhandled exception occurs, pressing F4 teleports your cursor straight to the failing line for instant inspection. Press Enter or Alt + Right Arrow to observe exception handling in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Catching ZeroDivisionError',
                'instruccion_en': 'Notice how dividing by zero does not crash execution thanks to the except block. Press Control + Enter to hear the handled message.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Catching Invalid Conversions (ValueError)',
                'instruccion_en': 'Attempt casting non-numeric text inside try, catching `ValueError` gracefully. Press Control + Enter.',
                'pistas_en': ['ValueError triggers when int() receives alphabetical characters.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Safe Conversion Function',
                'instruccion_en': "Define `convertir_a_entero(texto):` attempting `return int(texto)` inside try. Catch `ValueError` returning `None`. Call with 'abc' and print result. Run with Control + Enter.",
                'pistas_en': ['def convertir_a_entero(texto): try: return int(texto) except ValueError: return None'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The finally Block',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['It is the unconditional final guarantee.'],
                'pregunta_en': 'Under what conditions do statements inside a finally block execute?',
                'opciones_en': ['They execute ALWAYS and unconditionally, whether an exception occurred or not.', 'Exclusively if an exception occurred inside the try block.', 'Only if zero exceptions occurred inside the try block.'],
                'explicacion_en': 'The finally clause guarantees cleanup and resource disposal regardless of execution outcome.',
            },
        ]
    },
    33: {
        'titulo_en': 'Chapter 33: File Input and Output: open() and the with Context Manager',
        'resumen_en': 'Learn to read and write persistent files to disk safely, guaranteeing resource disposal using with open().',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Disk Persistence and Context Managers',
                'instruccion_en': "Until now, our data resided in RAM and vanished when execution halted. To persist data across computer reboots, we must write state to secondary storage files. In Python, we interface with file streams via `open()`. Core open modes: - `'w'` (write): Creates a new file or OVERWRITES existing contents completely. - `'r'` (read): Opens an existing file for reading; raises `FileNotFoundError` if absent. - `'a'` (append): Appends data to the end of the file without deleting existing lines. The `with` Context Manager: Instead of manual `f.close()` calls, we use: `with open('archivo.txt', 'w', encoding='utf-8') as f:`. The `with` statement guarantees that the file stream is cleanly flushed and closed upon leaving the block, even if an exception occurs. Press Enter or Alt + Right Arrow to observe file operations in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Safe Writing and Reading',
                'instruccion_en': "Inspect the full cycle: writing text to 'notas.txt' followed by reading and printing to stdout. Press Control + Enter.",
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': "Step 3: Experimentation: Appending Lines with Mode 'a'",
                'instruccion_en': "Open with mode 'a' to append a second line with `\\n` and read the full file. Press Control + Enter.",
                'pistas_en': ["Mode 'a' appends to the end without truncating."],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Persisting Student Message',
                'instruccion_en': "Write 'Estudiante activo en NVDA' to 'mensaje.txt'. Open in mode 'r', read into `texto_leido`, and print `print(texto_leido)`. Run with Control + Enter.",
                'pistas_en': ["with open('mensaje.txt', 'w', encoding='utf-8') as f: f.write('Estudiante activo en NVDA') then read in mode 'r'."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Advantage of with open()',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of guaranteed automatic closing.'],
                'pregunta_en': 'Why is using with open() standard software engineering practice over f = open() and f.close()?',
                'opciones_en': ['Guarantees that file streams are closed and deallocated automatically even on exceptions.', 'Renders the file hidden from other users.', 'Converts plain text automatically into an MP3 audio track.'],
                'explicacion_en': 'The with context manager executes the __exit__ hook, guaranteeing resource deallocation in the OS.',
            },
        ]
    },
    34: {
        'titulo_en': 'Chapter 34: Structured Data Persistence with JSON (json.dump and json.load)',
        'resumen_en': "Master the universal structured data interchange format (JSON) using Python's native standard library.",
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The JSON Standard and Serialization',
                'instruccion_en': "Writing raw unstructured text suffices for basic notes, but fails for structured state such as user records or configuration profiles. **JSON** (*JavaScript Object Notation*) is the universal standard for structured data persistence and cross-platform communication. JSON maps directly to native Python mappings: braces `{}` for dictionaries and brackets `[]` for lists. Python's native `json` standard library module provides: - `json.dump(data, file, indent=2)`: Serializes Python dictionaries/lists directly to disk in formatted JSON. - `json.load(file)`: Deserializes JSON files directly into live Python dictionaries in RAM. Because it is built-in, zero third-party packages are needed. Press Enter or Alt + Right Arrow to observe JSON persistence.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Saving and Loading with json',
                'instruccion_en': "Notice how a dictionary serializes to 'config.json' with dump() and deserializes back via load(). Press Control + Enter.",
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Mutating and Re-serializing',
                'instruccion_en': 'Mutate a field in the loaded dictionary and save it back to disk. Press Control + Enter.',
                'pistas_en': ['Verify the version updates to 3.0.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Persistent Task List in JSON',
                'instruccion_en': "Create list `mis_tareas = ['Aprender JSON', 'Dominar NVDA']`. Save to 'tareas.json' with `json.dump()`. Load into `tareas_recuperadas` and print the first task. Press Control + Enter.",
                'pistas_en': ["json.dump(mis_tareas, f) in mode 'w', then tareas_recuperadas = json.load(f) in 'r' and print(tareas_recuperadas[0])."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The json.load() Function',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of loading from disk into memory.'],
                'pregunta_en': 'What operation does json.load(file) perform in Python?',
                'opciones_en': ['Reads a JSON-formatted file and transforms it into native Python dictionaries/lists in RAM.', 'Downloads a remote JSON file from the web automatically.', 'Deletes the JSON file from the hard drive.'],
                'explicacion_en': 'json.load deserializes JSON streams into native Python dictionary and list structures.',
            },
        ]
    },
    35: {
        'titulo_en': 'Chapter 35: Object-Oriented Paradigm: Classes, Instances, and Attributes',
        'resumen_en': 'Master Object-Oriented Programming: model real-world domains using classes as blueprints and instances as concrete objects.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The Mental Model of Classes and Objects',
                'instruccion_en': 'Up to this point, our programs were procedural (discrete variables manipulated by loose functions). **Object-Oriented Programming** (OOP) groups state (attributes) and behavior (methods) into a unified entity called an **Object**. The core architectural analogy: 1. The **Class** (`class`): The architectural blueprint or cookie cutter. It specifies properties, but the class itself is not a physical cookie. 2. The **Object** or **Instance**: The baked cookie or constructed building instantiated from the blueprint. You can build 100 distinct buildings from one blueprint; each retains independent memory state. In Python, we declare a class using the `class` keyword followed by a capitalized `PascalCase` identifier (e.g. `class Usuario:`). Press Enter or Alt + Right Arrow to observe classes and instances in action.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Class Definition and Instantiation',
                'instruccion_en': 'Observe how class `Estudiante` is defined and two independent objects instantiated: `alumno1` and `alumno2`. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Assigning Distinct Instance Attributes',
                'instruccion_en': "Assign distinct attributes to each student using dot notation: `alumno1.nombre = 'Elena'` and `alumno2.nombre = 'Kevin'`. Print both and press Control + Enter.",
                'pistas_en': ['Dot notation binds the attribute to that specific object.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Modeling a Software Task',
                'instruccion_en': "Create `class Tarea: pass`. Instantiate `t = Tarea()`. Assign `t.titulo = 'Aprender POO'` and `t.completada = True`. Print: 'Tarea: Aprender POO, Estado: True'. Run with Control + Enter.",
                'pistas_en': ["class Tarea: pass, t = Tarea(), t.titulo = 'Aprender POO', t.completada = True, print(f'Tarea: {t.titulo}, Estado: {t.completada}')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Class versus Object Relationship',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Remember the architectural blueprint and constructed building analogy.'],
                'pregunta_en': 'What is the conceptual relationship between a Class and an Object in OOP?',
                'opciones_en': ['The class is the blueprint/template; the object is the concrete instance allocated in memory.', 'They are identical and signify the exact same thing.', 'A class stores only numbers while an object stores only strings.'],
                'explicacion_en': 'A class is the abstract template of structure and behavior; an object is the concrete manifestation instantiated from it.',
            },
        ]
    },
    36: {
        'titulo_en': 'Chapter 36: The __init__ Constructor, self Parameter, and Instance Methods',
        'resumen_en': 'Learn to initialize objects automatically using __init__, demystify self, and define object behaviors via instance methods.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: The __init__ Constructor and self',
                'instruccion_en': "Manually attaching attributes one-by-one (`objeto.x = 1`) is error-prone. In professional OOP, every object must be initialized into a valid state from its first moment in RAM. We achieve this using the special constructor method `__init__()` (with double leading and trailing underscores, known as *dunder init*). Demystifying the `self` Parameter: The first parameter of any instance method is convention-named `self`. `self` represents the specific instance being operated on in RAM. When writing `self.nombre = nombre`, you instruct Python: 'Bind this datum onto MY individual instance attributes'. Methods are functions scoped inside classes that receive `self` to query or mutate internal instance state. Press Enter or Alt + Right Arrow to observe constructors in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Class with __init__ and Instance Method',
                'instruccion_en': 'Inspect class `CanalAccesible`. Notice how `__init__` sets the name and `describir()` formats output. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Mutating Internal State via Method',
                'instruccion_en': 'Create class `Contador` with method `incrementar()` adding `self.valor += 1`. Run with Control + Enter.',
                'pistas_en': ['Calling c.incrementar() twice increments value to 2.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Secure Savings Account',
                'instruccion_en': "Define `class CuentaBancaria:`. In `__init__(self, titular):` set `self.titular = titular`, `self.saldo = 0`. Add method `depositar(self, monto):` doing `self.saldo += monto`. Create `cuenta = CuentaBancaria('Elena')`, deposit 150 and print: `print(f'Titular: {cuenta.titular}, Saldo: {cuenta.saldo}')`. Run with Control + Enter.",
                'pistas_en': ["Define __init__ and depositar with self. Instantiate cuenta = CuentaBancaria('Elena'), call cuenta.depositar(150), and print."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The Meaning of self',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['self refers to the individual object itself.'],
                'pregunta_en': 'What does the conventional first parameter self represent inside instance methods?',
                'opciones_en': ['It represents the specific concrete instance upon which the method is invoked.', 'It is a secret keyword to initiate network connections.', 'It represents the source code line number.'],
                'explicacion_en': "self binds the method to the specific instance's memory, granting access to its unique attributes.",
            },
        ]
    },
    37: {
        'titulo_en': 'Chapter 37: The Python Standard Library (math, random, datetime, pathlib)',
        'resumen_en': "Explore Python's 'batteries included': industrial modules preinstalled natively without external package managers.",
        'pasos': [
            {
                'titulo_en': "Step 1: Foundational Concept: Python's Batteries Included",
                'instruccion_en': "A primary reason Python dominates the global software industry is its 'Batteries Included' philosophy. Unlike ecosystems requiring fragile third-party downloads for routine utilities, Python ships out-of-the-box with hundreds of production modules available via simple `import` statements. Core Standard Library modules: - `math`: High-precision mathematical functions: square roots (`math.sqrt`), trigonometry, constants like `math.pi`. - `random`: Pseudorandom number generators, simulations, and random sampling (`random.randint`, `random.choice`). - `datetime`: Datetime parsing, date calculations, clocks, and intervals. - `pathlib`: Robust, object-oriented cross-platform filesystem path management. All of this runs natively inside NVDA with zero package compilation issues. Press Enter or Alt + Right Arrow to observe standard modules in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: math and random Modules',
                'instruccion_en': 'Inspect how math and random import natively without external tooling. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Timestamps with datetime',
                'instruccion_en': "Use `datetime.date.today()` to retrieve today's date and print it. Press Control + Enter.",
                'pistas_en': ["datetime is built into Python's native standard library."],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Random Token Generator',
                'instruccion_en': 'Use `import random`. Given `caracteres = [\'A\', \'B\', \'C\', \'1\', \'2\', \'3\']`, pick 4 random characters: `token = [random.choice(caracteres) for _ in range(4)]`. Print: `print(f\'Token generado: {"".join(token)}\')`. Press Control + Enter.',
                'pistas_en': ["Use random.choice inside a list or loop and join with ''.join."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: The Standard Library',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ["Remember the 'batteries included' philosophy."],
                'pregunta_en': 'Why do Python Standard Library modules (like math, random, json, sqlite3) require zero pip installation?',
                'opciones_en': ["Because they are built-in and shipped natively with the Python runtime ('batteries included').", 'Because they secretly download across every print call.', 'Because they only run on NASA mainframe clusters.'],
                'explicacion_en': 'The Standard Library is an inseparable core component of the official Python runtime across all platforms.',
            },
        ]
    },
    38: {
        'titulo_en': 'Chapter 38: Relational Databases with SQLite (sqlite3): Tables and Queries',
        'resumen_en': 'Learn to manage industrial SQL relational databases using the built-in sqlite3 engine without external servers.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Relational Databases and the sqlite3 Engine',
                'instruccion_en': "When software manages thousands of interdependent entities (users, invoices, catalogs), simple JSON files become unscalable. The industry solves this using **Relational Databases** queried via **SQL** (*Structured Query Language*). Python natively bundles **SQLite**, the most widely deployed SQL database engine in existence (powering browsers, phones, and NVDA itself). Advantages of SQLite: - Zero Configuration: Requires no standalone database daemon or server process. The entire relational store lives in a single disk file (or inside RAM via `':memory:'`). - Parameterized SQL Queries: To prevent catastrophic vulnerabilities (*SQL Injection*), we NEVER concatenate raw strings; we utilize the `?` placeholder parameter tuple. Press Enter or Alt + Right Arrow to observe SQLite in action.",
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Creating Tables and Inserting Records',
                'instruccion_en': 'Inspect how we connect to sqlite3 in-memory, create a users table, and query via SELECT. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Filtering Records with WHERE Clause',
                'instruccion_en': 'Filter the SQL query using `WHERE nota >= 9.0` to retrieve honors students only. Press Control + Enter.',
                'pistas_en': ['WHERE filters records inside the database engine.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Accessible SQLite Inventory',
                'instruccion_en': "Connect to `:memory:`, create table `articulos (nombre TEXT, cantidad INTEGER)`. Insert `('Teclado', 15)` parameterized. Query and print: 'Teclado: 15 unidades'. Close connection and run with Control + Enter.",
                'pistas_en': ["cursor.execute('INSERT INTO articulos VALUES (?, ?)', ('Teclado', 15)), then fetchall() and print."],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Parameterized Queries with ?',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Think of defensive cybersecurity protection.'],
                'pregunta_en': 'Why is it mandatory in production systems to use ? placeholders instead of string concatenation in SQL?',
                'opciones_en': ['To prevent catastrophic SQL Injection vulnerabilities and guarantee data security.', 'Because computers cannot parse quotes inside SQL.', 'To reduce database disk space footprint by half.'],
                'explicacion_en': 'Parameterized queries decouple code instructions from user inputs, completely neutralizing SQL Injection attacks.',
            },
        ]
    },
    39: {
        'titulo_en': 'Chapter 39: Assistive Technology and Accessible Software: NVDA Speech and Audio Signals',
        'resumen_en': 'Learn how software interfaces with screen readers, speech synthesizers, and acoustic cues to engineer inclusive systems.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Assistive Tech and Accessibility in Software Architecture',
                'instruccion_en': 'Assistive Technology (Tiflotechnology) is the engineering discipline devoted to crafting tools and adaptations for blind or low-vision users. In accessible software architecture, it is insufficient for routines to merely compute; UX must convey state transparently across two primary sensory modalities: 1. Speech Channel: Concise, non-redundant messages informing which action completed or which element holds focus. 2. Acoustic Channel (Auditory Cues / Earcons): Short, subtle tones of varying frequencies that deliver instant status confirmation without disrupting speech (e.g. higher-pitch for success, lower-pitch for fault). Under Windows and inside NVDA, Python emits native acoustic tones via standard `winsound.Beep(frequency, duration)`. Designing accessible systems from day zero is the signature hallmark of world-class software engineers. Press Enter or Alt + Right Arrow to hear accessible auditory cues.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Emitting Accessible Audio Cues',
                'instruccion_en': 'Notice how winsound produces frequency tones to confirm system states. Press Control + Enter to listen.',
                'pistas_en': ['Press Control + Enter to run and hear the pitch.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Auditory Alert Signal',
                'instruccion_en': 'Emit an alert signal using a lower pitch (440 Hz) with longer duration (250 ms). Press Control + Enter.',
                'pistas_en': ['winsound.Beep(440, 250) emits a lower pitch tone.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Accessible Notifier Routine',
                'instruccion_en': "Define `notificar(tipo_evento, mensaje):` printing `f'[{tipo_evento.upper()}]: {mensaje}'`. If `tipo_evento == 'exito'` beep 880Hz, else 440Hz. Test with `notificar('exito', 'Datos guardados correctamente')`. Run with Control + Enter.",
                'pistas_en': ["def notificar(tipo_evento, mensaje): print(f'[{tipo_evento.upper()}]: {mensaje}') if tipo_evento == 'exito': winsound.Beep(880, 100) else: winsound.Beep(440, 100) notificar('exito', 'Datos guardados correctamente')"],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Benefit of Multimodal Auditory Feedback',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Consider speed and avoiding auditory fatigue.'],
                'pregunta_en': 'What is the primary advantage of combining speech synthesis with acoustic earcons in accessible software?',
                'opciones_en': ['Provides instant status verification without saturating cognitive auditory load with redundant speech.', 'Reduces CPU electrical power consumption.', 'Forces the user to memorize mathematical coordinates.'],
                'explicacion_en': 'Acoustic earcons deliver instantaneous feedback without voice latency or cognitive speech saturation.',
            },
        ]
    },
    40: {
        'titulo_en': 'Chapter 40: Capstone Project: Accessible Information and Task Management Engine',
        'resumen_en': 'Integrate the complete curriculum: layered architecture, OOP, structured persistence, error handling, and accessible UI.',
        'pasos': [
            {
                'titulo_en': 'Step 1: Foundational Concept: Clean Layered Architecture',
                'instruccion_en': 'Congratulations on reaching the capstone module of your engineering journey! To build industrial-grade software, you must assemble all concepts mastered into a **Clean Layered Architecture**. Professional software strictly decouples concerns across four layers: 1. Domain / Entity Layer: Classes modeling domain concepts (e.g. `Tarea`, encapsulating title, date, status). 2. Persistence Layer: Robust logic reading/writing state to disk (via JSON or SQLite) using `with open()`. 3. Application / Service Layer: Business logic orchestrating validations, insertions, queries, and filters. 4. Accessibility / Presentation Layer: Responsive human-computer interaction through clear NVDA speech and auditory earcons. Press Enter or Alt + Right Arrow to inspect the full Capstone Engine.',
                'pistas_en': ['Advance with Enter or Alt + Right Arrow.'],
            },
            {
                'titulo_en': 'Step 2: Observation & Analysis: Inspecting the Accessible Manager',
                'instruccion_en': 'Inspect the complete Manager architecture. Note the Tarea class, JSON persistence, and formatted summary. Press Control + Enter.',
                'pistas_en': ['Press Control + Enter to execute.'],
            },
            {
                'titulo_en': 'Step 3: Experimentation: Toggling Task Completion',
                'instruccion_en': 'Add method `completar()` on class Tarea and verify state updates to True. Run with Control + Enter.',
                'pistas_en': ['t.completada must be True.'],
            },
            {
                'titulo_en': 'Step 4: Practical Challenge: Deploying the Complete System',
                'instruccion_en': "Create `class Proyecto` with `__init__(self, nombre)` initializing `self.nombre = nombre`, `self.modulos = []`. Add `agregar_modulo(self, mod)`. Create `p = Proyecto('Sistema Accesible')`, add 'Núcleo Python' and 'Lector NVDA'. Print: `print(f'Proyecto {p.nombre} con {len(p.modulos)} módulos activos')`. Press Control + Enter.",
                'pistas_en': ['class Proyecto with __init__ and agregar_modulo. Instantiate p, add both modules, and print with f-string.'],
            },
            {
                'titulo_en': 'Step 5: Conceptual Check: Separation of Concerns',
                'instruccion_en': 'Select the correct option with arrow keys and press Enter to verify.',
                'pistas_en': ['Consider modularity and long-term maintainability.'],
                'pregunta_en': 'Why is separating business logic from user interface presentation fundamental in software engineering?',
                'opciones_en': ['Enables modifying, testing, and adapting accessibility without risking core business calculation rules.', 'Forces source code files to weigh exactly 1 kilobyte.', 'It is a legal mandate exclusive to financial banking systems.'],
                'explicacion_en': 'Separation of Concerns guarantees modularity, testability, maintainability, and lifelong accessibility.',
            },
        ]
    },
}

GLOSARIO_EN = {
    'algoritmo': 'Ordered, unambiguous, finite sequence of logical instructions designed to solve a problem.',
    'ambito': 'Region of source code where an identifier is visible and resolved (local, global, built-in).',
    'and': 'Logical operator returning True strictly when all evaluated conditions are true.',
    'append': 'Method appending a new element to the tail of a list in constant amortized time.',
    'argumento': 'Actual value supplied between parentheses to a function invocation.',
    'aritmetica': 'Fundamental arithmetic operations (+, -, *, /, //, %, **) evaluated under precedence rules.',
    'array': 'Contiguous memory structure storing sequential homogeneous items.',
    'ascii': 'Numerical character encoding mapping 128 characters to 7-bit binary numbers.',
    'asignacion': 'Operation using = that computes the right-hand expression and stores it into the left-hand variable.',
    'asincronia': 'Non-blocking concurrency paradigm allowing systems to handle multiple asynchronous events.',
    'atributo': 'Named variable bound to the internal state of a class or concrete instance.',
    'autocompletado': 'IDE accessibility tool suggesting symbols and keywords to minimize typing effort.',
    'binario': 'Base-2 numeral system used internally by the CPU, consisting exclusively of zeros and ones.',
    'bit': 'Binary digit representing the fundamental unit of information (0 or 1) in an electronic circuit.',
    'booleano': 'Primitive data type that can only evaluate to True or False.',
    'braille': 'Tactile reading and writing system interfaced through refreshable braille displays.',
    'break': 'Jump statement immediately terminating the innermost loop construct.',
    'bucle': 'Control flow structure executing a statement block repeatedly.',
    'byte': 'Standard unit of digital information consisting of a contiguous sequence of 8 bits.',
    'call_stack': 'LIFO call stack in memory tracking active execution frames.',
    'capstone': 'Comprehensive integration project demonstrating all competencies acquired throughout a curriculum.',
    'casting': 'Explicit conversion of a value across types using constructors like int(), float(), str().',
    'clase': 'Blueprint or architectural template defining object attributes and behavior.',
    'codigo_fuente': 'Human-readable instructions written in a formal programming language.',
    'coleccion': 'Data structure capable of grouping multiple items under a single variable.',
    'comentario': 'Source line prefixed with #, completely skipped by the interpreter for human guidance.',
    'compilador': 'Program translating complete source code into executable binary machine code prior to execution.',
    'concatenacion': 'Operation joining two or more character sequences into a unified string.',
    'condicion': 'Logical proposition evaluating to a boolean value (True or False).',
    'consola': 'Text-based standard input/output stream where programs receive commands and emit output.',
    'constructor': 'Special initializer method (__init__) executed automatically upon object instantiation.',
    'context_manager': 'Resource management protocol governed by with that guarantees deterministic cleanup.',
    'continue': 'Jump statement skipping the remainder of the current iteration to advance to the next.',
    'cpu': 'Central Processing Unit responsible for fetching, decoding, and executing machine instructions at high speed.',
    'debugging': 'Methodical engineering process of isolating, diagnosing, and resolving software faults.',
    'def': 'Reserved keyword used to declare functions and methods in Python.',
    'delimitador': 'Paired grouping characters (quotes, parentheses, brackets, braces) structuring code.',
    'desempaquetado': 'Idiomatic syntax extracting tuple or list elements directly into discrete variables.',
    'diccionario': 'Associative hash map storing unique key-value pairs with O(1) average lookup.',
    'dry': 'Don’t Repeat Yourself: fundamental software engineering principle prohibiting logic duplication.',
    'earcon': 'Short acoustic auditory cue communicating software state without cognitive voice latency.',
    'elif': 'Short for else if: chained conditional clause evaluating secondary alternative predicates.',
    'else': 'Default fallback branch executing when all preceding conditions evaluate to false.',
    'encapsulamiento': 'OOP principle concealing internal state mechanics to protect object integrity.',
    'enumerate': 'Built-in routine yielding sequential (index, item) pairs across iterations.',
    'es_par': 'Algorithm using modulo % 2 == 0 to determine exact divisibility by two.',
    'escape': 'Backslash (\\) mechanism conferring special control meaning to characters in strings.',
    'estado': 'Current snapshot of values residing in memory at a specific execution timestamp.',
    'excepcion': 'Anomalous runtime event interrupting normal execution, caught via try/except.',
    'f_string': 'String literal prefixed with f that interpolates variables enclosed in braces {}.',
    'finally': 'Defensive block in try/except executing unconditionally regardless of fault status.',
    'float': 'Numeric data type representing real numbers with fractional floating-point parts.',
    'for': 'Definite iteration loop traversing sequences and collection items.',
    'funcion': 'Encapsulated modular routine invoked by name that accepts arguments and yields returns.',
    'hardware': 'Physical electronic machinery and components forming a computing platform.',
    'identificador': 'Symbolic token naming variables, routines, and classes under snake_case conventions.',
    'if': 'Conditional branching statement executing indented blocks when predicates evaluate to true.',
    'inmutabilidad': 'Property of data types (like tuples and strings) prohibiting in-place mutation after creation.',
    'input': 'Built-in routine halting execution to capture user keystrokes from standard input.',
    'instancia': 'Concrete manifested object allocated in RAM instantiated from a class blueprint.',
    'int': 'Numeric data type representing positive, negative, or zero integers without fractions.',
    'interprete': 'Engine reading, analyzing, and executing source code instruction by instruction in real time.',
    'iteracion': 'Single execution pass through a loop construct traversing collection elements.',
    'json': 'JavaScript Object Notation, lightweight, human-readable data interchange format widely used across APIs.',
    'lector_pantalla': 'Assistive screen reading software like NVDA translating screen information into synthetic speech and braille.',
    'len': 'Built-in function measuring and returning the cardinal element count of sequences.',
    'lista': 'Ordered, mutable sequence of items delimited by square brackets [].',
    'metodo': 'Function scoped inside a class that acts on instance memory receiving self.',
    'modulo': 'Python source file with reusable routines imported via the import statement.',
    'mutabilidad': 'Characteristic of collections (like lists and dictionaries) permitting in-place mutation.',
    'name_error': 'Exception raised when attempting to evaluate an identifier absent from memory scopes.',
    'none': 'Python singleton object formally denoting the absence of a value.',
    'not': 'Logical negation operator inverting truth values.',
    'nvda': 'NonVisual Desktop Access, free and open-source screen reader for Windows operating systems.',
    'objeto': 'Unified entity in RAM binding state via attributes and behaviors via methods.',
    'open': 'Built-in function interfacing with the filesystem for buffered reading or writing.',
    'operador': 'Special symbol (+, ==, and) executing mathematical, logical, or relational actions.',
    'or': 'Logical operator returning True whenever at least one operand evaluates to true.',
    'parametrizada': 'SQL statement using ? placeholders to separate query logic from data, eliminating SQL injection.',
    'parametro': 'Formal variable declared in a function signature receiving incoming caller data.',
    'pass': 'No-op statement acting as a structural placeholder when syntax requires an indented line.',
    'pep8': 'Official style guide and software engineering best practices for Python source code.',
    'persistencia': 'Capability of retaining data across process lifecycles onto secondary non-volatile storage or disk.',
    'pop': 'List method extracting and deleting an element at an index (defaulting to tail).',
    'precedencia': 'Hierarchical evaluation precedence ordering arithmetic and logical operators.',
    'print': 'Foundational routine routing strings to standard output for screen reader speech.',
    'ram': 'Random Access Memory: high-speed volatile storage holding active process states.',
    'range': 'Immutable arithmetic progression generator of integers utilized in for loops.',
    'reasignacion': 'Action of replacing an identifier’s memory reference with a newly computed payload.',
    'refactorizacion': 'Process of restructuring existing code to improve internal design without changing external behavior.',
    'relacional': 'Operators comparing values and producing boolean outcomes (==, !=, <, >, <=, >=).',
    'return': 'Statement concluding routine execution and handing a computed value to the caller.',
    'salida_estandar': 'The standard output stream (stdout) where processes write diagnostics and text.',
    'sangria': 'Leading whitespace indentation (PEP 8 4 spaces) defining code block nesting.',
    'self': 'Conventional explicit reference to the active concrete instance inside methods.',
    'sentencia': 'Complete executable instruction processed by the Python interpreter.',
    'serializacion': 'Translating complex objects in RAM into persistent byte streams or text (JSON).',
    'short_circuit': 'Logical optimization stopping compound evaluation once truth value is determined.',
    'sintaxis': 'Grammatical rules governing how instructions must be authored.',
    'sistema_operativo': 'System software managing hardware resources and providing common services for applications.',
    'snake_case': 'Naming convention formatting identifiers in lowercase separated by underscores.',
    'software': 'Collection of code routines instructing hardware machinery how to compute.',
    'sqlite': 'Lightweight, self-contained relational SQL database engine embedded in Python’s standard library.',
    'sqlite3': 'Embedded relational SQL database engine bundled natively in Python Standard Library.',
    'ssl': 'Secure Sockets Layer providing encrypted cryptographic network communication.',
    'str': 'Primitive data type representing immutable character string literals.',
    'syntax_error': 'Parsing error indicating invalid code grammar preventing compilation.',
    'tabla_verdad': 'Algebraic matrix cataloging all truth outcomes across logical operations.',
    'tiflotecnologia': 'Assistive engineering discipline designing accessible systems for blind individuals.',
    'timeout': 'Maximum time threshold allocated to a computation before aborting execution.',
    'traceback': 'Call stack diagnostic dump pinpointing the exact line where an exception occurred.',
    'true_false': 'The two boolean literals representing binary truth.',
    'try_except': 'Defensive error-handling construct engineered for fault-tolerant applications.',
    'tupla': 'Ordered, immutable sequence delimited by parentheses ().',
    'type_error': 'Exception raised when applying operations onto incompatible data types.',
    'unicode': 'Universal character standard mapping unique integer codes to characters worldwide.',
    'unittest': 'Standard library unit testing framework certifying software correctness.',
    'variable': 'Symbolic identifier referencing a memory location containing a mutable payload.',
    'while': 'Conditional iteration loop repeating statements while its predicate remains true.',
    'winsound': 'Windows-specific built-in module emitting acoustic frequency tones.',
    'with': 'Statement wrapping context managers ensuring deterministic resource disposal.',
    'zen_python': 'Collection of 19 guiding engineering principles defining Python’s philosophy.',
}

CODIGO_EN_MAP = {6: {1: "print('Hello, accessible world')\n", 2: "print('Hello, programming student')\n", 3: '# Write your two print statements here:\n\n'}, 7: {1: "tool = 'NVDA'\nprint(tool)\n", 2: "tool = 'Accessible screen reader'\nprint(tool)\n", 3: '# Create the variable student and print it:\n\n'}, 8: {1: "# This is an explanatory comment\n# The following line emits the official message:\nprint('Code documented successfully')\n", 2: "# Author: Kevin\nprint('Active comments')\n", 3: "print('Old message that must be disabled')\nprint('Current active message')\n"}, 9: {1: "status = 'Loading data...'\nprint(status)\nstatus = 'Process completed'\nprint(status)\n", 2: "status = 'Starting'\nprint(status)\nstatus = 'Successful operation in NVDA'\nprint(status)\n", 3: '# Declare score = 0, print, reassign to 100, and print:\n\n'}, 10: {1: 'base = 10\nheight = 5\narea = base * height\nprint(area)\n', 2: 'average = (8 + 9 + 10) // 3\nprint(average)\n', 3: '# Declare width, height, calculate perimeter, and print:\n\n'}, 11: {1: "print('Real division:', 15 / 4)\nprint('Integer division:', 15 // 4)\nprint('Remainder or modulo:', 15 % 4)\n", 2: 'price = 49.99\ndiscount = 10.50\ntotal = price - discount\nprint(total)\n', 3: '# Calculate per_child and leftovers, and print them:\n\n'}, 12: {1: "print('Upper accessible line\\nLower processed line')\n", 2: 'print("The language \'Python\' is accessible")\n', 3: '# Create menu with newlines and print it:\n\n'}, 13: {1: "user = 'Elena'\nchapter = 13\nprint(f'Student {user} attending Chapter {chapter}')\n", 2: "value = 25\nprint(f'Double of {value} is {value * 2}')\n", 3: '# Declare product, price, quantity, and print with f-string:\n\n'}, 14: {1: "age_str = '20'\nage = int(age_str)\nmonths = age * 12\nprint(f'Age: {age} years, equivalent to {months} months')\n", 2: "num1_str = '50'\nnum2_str = '25'\ntotal = int(num1_str) + int(num2_str)\nprint(f'Total sum: {total}')\n", 3: "entry = '80'\n# Convert to int, calculate double and half, and print with f-string:\n\n"}, 15: {1: "print('Is 10 greater than 5?:', 10 > 5)\nprint('Is 4 equal to 9?:', 4 == 9)\nprint('Is 7 different from 7?:', 7 != 7)\n", 2: "age = 20\nis_adult = age >= 18\nprint(f'Is adult?: {is_adult}')\n", 3: "saved_key = 'python2026'\nentered_key = 'python2026'\n# Compare with == and print access_granted:\n\n"}, 16: {1: "has_key = True\nknows_code = False\nprint('Enter with and (key AND code)?:', has_key and knows_code)\nprint('Enter with or (key OR code)?:', has_key or knows_code)\nprint('Negation of knows_code with not:', not knows_code)\n", 2: "locked = False\navailable = not locked\nprint(f'System available?: {available}')\n", 3: '# Declare gpa, attendance, evaluate gets_scholarship, and print:\n\n'}, 17: {1: "age = 20\nif age >= 18:\n    print('Access granted due to legal age')\n", 2: "age = 15\nif age >= 18:\n    print('Access granted due to legal age')\n", 3: 'temperature = 35\n# Write the if statement with 4-space indentation:\n\n'}, 18: {1: "age = 16\nif age >= 18:\n    print('Access granted')\nelse:\n    print('Access denied: must be at least 18')\n", 2: "age = 25\nif age >= 18:\n    print('Access granted')\nelse:\n    print('Access denied: must be at least 18')\n", 3: 'number = 14\n# Check if number % 2 == 0 using if/else:\n\n'}, 19: {1: "score = 75\nif score >= 90:\n    print('Grade: Outstanding')\nelif score >= 70:\n    print('Grade: Passed')\nelse:\n    print('Grade: Needs reinforcement')\n", 2: "score = 95\nif score >= 90:\n    print('Grade: Outstanding')\nelif score >= 70:\n    print('Grade: Passed')\nelse:\n    print('Grade: Needs reinforcement')\n", 3: 'temp = 22\n# Write the if / elif / else structure with 4-space indentation:\n\n'}, 20: {1: "for i in range(1, 6):\n    print(f'Step number: {i}')\n", 2: "for n in range(2, 11, 2):\n    print(f'Even: {n}')\n", 3: 'total = 0\n# Iterate with for adding to total and print total at the end:\n\n'}, 21: {1: "counter = 1\nwhile counter <= 3:\n    print(f'Loop iteration: {counter}')\n    counter += 1\nprint('Process finished')\n", 2: "countdown = 5\nwhile countdown > 0:\n    print(f'T-minus: {countdown}')\n    countdown -= 1\nprint('Liftoff!')\n", 3: 'energy = 1\n# Write while loop doubling or tripling energy:\n\n'}, 22: {1: "step = 1\nwhile step < 5:\n    print(f'Safe progress step #{step}')\n    step += 1\nprint('Safe execution completed')\n", 2: "level = 1\nwhile level <= 4:\n    print(f'Level {level} cleared')\n    level += 1\nprint('All levels completed')\n", 3: 'battery = 70\n# Increase battery by 10 until reaching 100%:\n\n'}, 23: {1: "for n in range(1, 10):\n    if n == 3:\n        print(f'Target {n} detected, skipping review')\n        continue\n    if n == 6:\n        print('Target 6 reached, stopping search')\n        break\n    print(f'Checking item {n}')\n", 2: "for n in range(1, 7):\n    if n % 2 != 0:\n        continue\n    print(f'Processed even: {n}')\n", 3: 'readings = [15, 22, -1, 30]\n# Iterate through readings and stop on negative:\n\n'}, 24: {1: "languages = ['Python', 'C', 'JavaScript', 'Rust']\nprint('First language:', languages[0])\nprint('Last language:', languages[-1])\n", 2: "languages = ['Python', 'C', 'JavaScript', 'Rust']\nlanguages[1] = 'C++'\nprint(languages)\n", 3: '# Create tools and print the first and last element:\n\n'}, 25: {1: "tasks = ['Review Python', 'Configure NVDA']\ntasks.append('Practice loops')\nprint(f'Total tasks: {len(tasks)}')\nprint('Updated tasks:', tasks)\n", 2: "tasks = ['Lesson 1', 'Lesson 2', 'Lesson 3']\nremoved = tasks.pop()\nprint('Removed:', removed)\nprint('Remaining:', tasks)\n", 3: "queue = ['Ana', 'Bernardo']\n# Add Carlos, remove Ana, and print queue:\n\n"}, 26: {1: "fruits = ['Apple', 'Pear', 'Banana']\nfor index, fruit in enumerate(fruits, start=1):\n    print(f'{index}. {fruit}')\n", 2: "channels = ['Synthesized Speech', 'Braille Display', 'Acoustic Cue']\nfor index, channel in enumerate(channels, start=1):\n    print(f'{index}. Channel: {channel}')\n", 3: 'prices = [12.50, 8.00, 24.50]\ntotal = 0\n# Iterate through prices accumulating in total and print:\n\n'}, 27: {1: "resolution = (1920, 1080)\nwidth, height = resolution\nprint(f'Width: {width}px, Height: {height}px')\n", 2: "coordinates = (10, 25)\nprint(f'Immutable X-axis: {coordinates[0]}')\n", 3: "user = ('Elena', 'Developer', 2026)\n# Unpack into name, role, year, and print with f-string:\n\n"}, 28: {1: "config = {'language': 'en', 'volume': 85, 'speech': True}\nprint('Configured language:', config['language'])\nprint('Volume level:', config['volume'])\n", 2: "config = {'language': 'en', 'volume': 85}\nconfig['volume'] = 50\nconfig['braille'] = True\nrate = config.get('rate', 45)\nprint('Updated settings:', config)\nprint('Default rate:', rate)\n", 3: '# Create profile dictionary and print with f-string:\n\n'}, 29: {1: "def greet_user(name):\n    print(f'Hello, {name}. Welcome to the accessible environment.')\n\ngreet_user('Elena')\ngreet_user('Kevin')\n", 2: "def show_progress(chapter, total):\n    print(f'Advancing: Chapter {chapter} of {total}')\n\nshow_progress(29, 40)\n", 3: '# Define calculate_area and call it with 7 and 6:\n\n'}, 30: {1: "def square(x):\n    return x * x\n\nres = square(8)\nprint(f'Result saved in memory: {res}')\n", 2: "def square(n):\n    return n * n\n\nresult = square(5) + 10\nprint(f'Chained calculation: {result}')\n", 3: '# Define is_adult with return, assign to authorized, and print:\n\n'}, 31: {1: "def generate_report():\n    local_message = 'Secure internal report'\n    return local_message\n\nreport = generate_report()\nprint(report)\n", 2: "version = 1\n\ndef get_version():\n    return f'Active global version: {version}'\n\nprint(get_version())\n", 3: '# Define calculate_tax with subtotal as parameter and return 19%:\n\n'}, 32: {1: "try:\n    divisor = 0\n    result = 100 / divisor\n    print(result)\nexcept ZeroDivisionError:\n    print('Safe notice: Cannot divide by zero.')\n", 2: "user_input = 'twenty'\ntry:\n    number = int(user_input)\n    print(number)\nexcept ValueError:\n    print('Format error: Input contains no valid numeric digits.')\n", 3: '# Define convert_to_integer with try/except ValueError, assign to res, and print:\n\n'}, 33: {1: "with open('notes.txt', 'w', encoding='utf-8') as f:\n    f.write('Python is accessible with NVDA')\n\nwith open('notes.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n\nprint(f'Content retrieved from disk: {content}')\n", 2: "with open('log.txt', 'w', encoding='utf-8') as f:\n    f.write('Entry 1\\n')\n\nwith open('log.txt', 'a', encoding='utf-8') as f:\n    f.write('Appended Entry 2\\n')\n\nwith open('log.txt', 'r', encoding='utf-8') as f:\n    print(f.read().strip())\n", 3: '# Write to message.txt, then read and print:\n\n'}, 34: {1: "import json\n\nuser = {'name': 'Elena', 'level': 3, 'accessible': True}\n\nwith open('config.json', 'w', encoding='utf-8') as f:\n    json.dump(user, f, indent=2)\n\nwith open('config.json', 'r', encoding='utf-8') as f:\n    loaded_data = json.load(f)\n\nprint('Data retrieved from JSON:', loaded_data['name'], loaded_data['level'])\n", 2: "import json\n\ndata = {'app': 'Python Tutor', 'version': 1.0}\ndata['version'] = 1.0\n\nwith open('app_meta.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f)\n\nwith open('app_meta.json', 'r', encoding='utf-8') as f:\n    print(json.load(f))\n", 3: "import json\n\nmy_tasks = ['Learn JSON', 'Master NVDA']\n# Save to tasks.json, read into retrieved_tasks, and print the first element:\n\n"}, 35: {1: "class Student:\n    institution = 'NVDA Accessible Academy'\n\nstudent1 = Student()\nstudent2 = Student()\n\nprint('Student 1 belongs to:', student1.institution)\nprint('Student 2 belongs to:', student2.institution)\n", 2: "class Student:\n    pass\n\nstudent1 = Student()\nstudent1.name = 'Elena'\n\nstudent2 = Student()\nstudent2.name = 'Kevin'\n\nprint(f'Registered students: {student1.name} and {student2.name}')\n", 3: '# Define class Task, create t, assign attributes, and print:\n\n'}, 36: {1: "class AccessibleChannel:\n    def __init__(self, name, channel_type):\n        self.name = name\n        self.channel_type = channel_type\n\n    def describe(self):\n        return f'Channel: {self.name} ({self.channel_type})'\n\nchannel1 = AccessibleChannel('NVDA Voice', 'Synthesized Speech')\nprint(channel1.describe())\n", 2: "class Counter:\n    def __init__(self):\n        self.value = 0\n\n    def increment(self):\n        self.value += 1\n\nc = Counter()\nc.increment()\nc.increment()\nprint(f'Current counter value: {c.value}')\n", 3: '# Define BankAccount, deposit 150, and print:\n\n'}, 37: {1: "import math\nimport random\n\nroot = math.sqrt(64)\ndice = random.randint(1, 6)\n\nprint(f'Square root of 64: {root}')\nprint(f'Random dice roll: {dice}')\n", 2: "import datetime\n\ntoday = datetime.date.today()\nprint(f'Date recorded by system: {today}')\n", 3: "import random\ncharacters = ['A', 'B', 'C', '1', '2', '3']\n# Generate a random 4-character token and print it:\n\n"}, 38: {1: "import sqlite3\n\nconnection = sqlite3.connect(':memory:')\ncursor = connection.cursor()\n\ncursor.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)')\ncursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', ('Elena', 9.5))\ncursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', ('Kevin', 9.0))\nconnection.commit()\n\ncursor.execute('SELECT name, grade FROM students')\nfor row in cursor.fetchall():\n    print(f'Student: {row[0]}, Grade: {row[1]}')\n\nconnection.close()\n", 2: "import sqlite3\n\ncon = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE courses (title TEXT, hours INTEGER)')\ncur.execute('INSERT INTO courses VALUES (?, ?)', ('Accessible Python', 40))\ncur.execute('INSERT INTO courses VALUES (?, ?)', ('Quick HTML', 10))\ncon.commit()\n\ncur.execute('SELECT title FROM courses WHERE hours >= 20')\nfor row in cur.fetchall():\n    print(f'Intensive course: {row[0]}')\ncon.close()\n", 3: 'import sqlite3\n# Create database in memory, insert article, and print:\n\n'}, 39: {1: "import winsound\n\nprint('Emitting success acoustic signal (880 Hz frequency)...')\nwinsound.Beep(880, 150)\nprint('Acoustic notification completed.')\n", 2: "import winsound\n\nprint('Acoustic warning signal (440 Hz):')\nwinsound.Beep(440, 250)\nprint('Notice emitted.')\n", 3: 'import winsound\n# Define notify with distinct tone and test it:\n\n'}, 40: {1: "import json\n\nclass Task:\n    def __init__(self, task_id, title):\n        self.task_id = task_id\n        self.title = title\n        self.completed = False\n\n    def to_dict(self):\n        return {'id': self.task_id, 'title': self.title, 'completed': self.completed}\n\nclass TaskManager:\n    def __init__(self):\n        self.tasks = []\n\n    def add(self, title):\n        new_task = Task(len(self.tasks) + 1, title)\n        self.tasks.append(new_task)\n        return new_task\n\n    def save_json(self, path):\n        data = [t.to_dict() for t in self.tasks]\n        with open(path, 'w', encoding='utf-8') as f:\n            json.dump(data, f, indent=2)\n\nmanager = TaskManager()\nmanager.add('Complete Python with NVDA course')\nmanager.save_json('final_tasks.json')\nprint(f'Integrated system active: {len(manager.tasks)} tasks managed successfully.')\n", 2: "class Task:\n    def __init__(self, title):\n        self.title = title\n        self.completed = False\n\n    def complete(self):\n        self.completed = True\n\nt = Task('Python Graduation')\nt.complete()\nprint(f'Final task status: {t.title} -> Completed: {t.completed}')\n", 3: '# Develop Project class and integrate modules:\n\n'}}

def APLICAR_TRADUCCIONES(curriculum):
    """Aplica las traducciones al objeto CURRICULUM en memoria."""
    for cap in curriculum:
        cid = cap.get('id')
        tr = CHAPTER_TRANSLATIONS.get(cid)
        if not tr:
            continue
        cap['titulo_en'] = tr.get('titulo_en', cap.get('titulo', ''))
        cap['resumen_en'] = tr.get('resumen_en', cap.get('resumen', ''))
        pasos_tr = tr.get('pasos', [])
        for i, paso in enumerate(cap.get('pasos', [])):
            if i < len(pasos_tr):
                ptr = pasos_tr[i]
                for k, v in ptr.items():
                    paso[k] = v
            # Aplicar codigo_en si existe en CODIGO_EN_MAP
            if cid in CODIGO_EN_MAP and i in CODIGO_EN_MAP[cid]:
                paso['codigo_en'] = CODIGO_EN_MAP[cid][i]


def obtener_glosario(lang=None):
    """Devuelve el glosario en el idioma correspondiente (español o inglés)."""
    if lang is None:
        try:
            from .i18n import obtener_idioma_actual
            lang = obtener_idioma_actual()
        except Exception:
            lang = 'es'
    if lang == 'en':
        return GLOSARIO_EN
    try:
        from .curriculum import GLOSARIO
        return GLOSARIO
    except Exception:
        return GLOSARIO_EN
