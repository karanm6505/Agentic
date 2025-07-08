**
# Course Syllabus
## Course Title: Compiler Design
**Course Code:** CS450
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides a comprehensive introduction to the theory and practice of compiler design. Students will learn the fundamental principles and techniques involved in translating high-level programming languages into executable machine code. Topics covered include lexical analysis, parsing, semantic analysis, intermediate code generation, code optimization, and target code generation. The course emphasizes hands-on experience through programming projects that involve building a working compiler for a simplified programming language.

### Prerequisites:
Data Structures and Algorithms, Computer Architecture, Theory of Computation

### Learning Objectives:
1.  Describe the phases of a compiler and their interactions.
2.  Implement lexical analyzers using regular expressions and finite automata.
3.  Construct parsers using context-free grammars and parsing techniques such as LL and LR parsing.
4.  Perform semantic analysis, including type checking and symbol table management.
5.  Generate intermediate code representations for high-level language constructs.
6.  Apply code optimization techniques to improve the performance of generated code.
7.  Generate target machine code for a specific architecture.

### Required Textbooks:
- Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, *Compilers: Principles, Techniques, and Tools*, 2nd Edition, Pearson Education, 2007 (ISBN: 978-0321486813)

### Recommended Readings:
- Andrew W. Appel, *Modern Compiler Implementation in C*, Cambridge University Press, 1998.
- Keith D. Cooper and Linda Torczon, *Engineering a Compiler*, Morgan Kaufmann, 2011.

### Weekly Schedule:
**Week 1: Introduction to Compilers**
- Topics: Overview of compilation process, compiler structure, phases of a compiler, bootstrapping.
- Readings: Chapter 1 of the textbook.
- Activities: Introduction to the course project.
- Due: N/A

**Week 2: Lexical Analysis**
- Topics: Regular expressions, finite automata, scanner generators (e.g., Flex).
- Readings: Chapter 3 of the textbook.
- Activities: Lab session on regular expressions.
- Due: N/A

**Week 3: Lexical Analysis Implementation**
- Topics: Implementing a lexical analyzer, error handling in lexical analysis.
- Readings: Chapter 3 of the textbook.
- Activities: Lab session: Implementing a scanner using Flex.
- Due: N/A

**Week 4: Syntax Analysis: Context-Free Grammars**
- Topics: Context-free grammars, derivation, parse trees, ambiguity.
- Readings: Chapter 4 of the textbook.
- Activities: Discussion on grammar design.
- Due: N/A

**Week 5: Parsing: Top-Down Parsing**
- Topics: LL(1) parsing, recursive descent parsing, predictive parsing.
- Readings: Chapter 4 of the textbook.
- Activities: Lab session: Implementing a recursive descent parser.
- Due: Quiz 1 (Lexical Analysis)

**Week 6: Parsing: Bottom-Up Parsing**
- Topics: LR parsing, SLR parsing, CLR parsing, LALR parsing.
- Readings: Chapter 4 of the textbook.
- Activities: Discussion on LR parsing techniques.
- Due: N/A

**Week 7: Parser Generators**
- Topics: Using parser generators (e.g., Yacc, Bison).
- Readings: Chapter 4 of the textbook.
- Activities: Lab session: Implementing a parser using Bison.
- Due: Project Part 1 (Lexical Analyzer and Parser)

**Week 8: Semantic Analysis: Symbol Tables**
- Topics: Symbol table organization, scope management, attribute storage.
- Readings: Chapter 6 of the textbook.
- Activities: Discussion on symbol table design.
- Due: N/A

**Week 9: Semantic Analysis: Type Checking**
- Topics: Type systems, type checking rules, type conversion.
- Readings: Chapter 6 of the textbook.
- Activities: Lab session: Implementing type checking.
- Due: N/A

**Week 10: Intermediate Code Generation**
- Topics: Intermediate representations (e.g., three-address code, abstract syntax trees).
- Readings: Chapter 8 of the textbook.
- Activities: Discussion on intermediate code formats.
- Due: Quiz 2 (Parsing and Semantic Analysis)

**Week 11: Intermediate Code Generation Implementation**
- Topics: Translating high-level code to intermediate code.
- Readings: Chapter 8 of the textbook.
- Activities: Lab session: Generating three-address code.
- Due: N/A

**Week 12: Code Optimization: Basic Blocks and Control Flow Graphs**
- Topics: Basic blocks, control flow graphs, data flow analysis.
- Readings: Chapter 9 of the textbook.
- Activities: Discussion on control flow analysis.
- Due: N/A

**Week 13: Code Optimization: Optimization Techniques**
- Topics: Common subexpression elimination, dead code elimination, loop optimization.
- Readings: Chapter 9 of the textbook.
- Activities: Lab session: Implementing code optimization techniques.
- Due: Project Part 2 (Semantic Analyzer and Intermediate Code Generator)

**Week 14: Code Generation**
- Topics: Target machine architecture, instruction selection, register allocation.
- Readings: Chapter 10 of the textbook.
- Activities: Discussion on code generation strategies.
- Due: N/A

**Week 15: Code Generation Implementation**
- Topics: Generating machine code for a specific architecture.
- Readings: Chapter 10 of the textbook.
- Activities: Lab session: Generating target code.
- Due: N/A

**Week 16: Final Project Presentations and Review**
- Topics: Review of course material, final project presentations.
- Readings: Review all chapters.
- Activities: Final project presentations.
- Due: Final Project (Complete Compiler)

### Assessment Breakdown:
*   Programming Projects: 40% (Two projects, 20% each, involving building components of a compiler)
*   Quizzes: 20% (Two quizzes, 10% each, covering theoretical concepts)
*   Final Exam: 40% (Comprehensive exam covering all topics)

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%