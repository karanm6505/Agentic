**
# Course Syllabus
## Course Title: Compiler Design
**Course Code:** CS452
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides a comprehensive introduction to the theory and practice of compiler design. Students will learn the fundamental principles behind compiler construction, including lexical analysis, parsing, semantic analysis, and code generation. The course emphasizes hands-on experience through programming assignments and a significant compiler implementation project. By the end of the course, students will have a strong understanding of how high-level programming languages are translated into executable code.

### Prerequisites:
Data Structures, Computer Architecture, Theory of Computation

### Learning Objectives:
1.  Analyze the different phases of a compiler and their interactions.
2.  Implement lexical analyzers and parsers using various techniques and tools.
3.  Develop semantic analysis modules for type checking and intermediate code generation.
4.  Design and implement code generation strategies for different target architectures.
5.  Apply optimization techniques to improve the performance of generated code.
6.  Evaluate the efficiency and correctness of a compiler.

### Required Textbooks:
- Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, *Compilers: Principles, Techniques, and Tools (2nd Edition)*, Pearson Education, 2007 (ISBN: 978-0321486813)

### Recommended Readings:
- Andrew W. Appel, *Modern Compiler Implementation in C*, Cambridge University Press, 1998.
- Article Title: "Efficient Compilation Techniques", Journal of Computer Science, 25(3):120-145, 2020.

### Weekly Schedule:
**Week 1: Introduction to Compilers**
- Topics: Overview of compilation, phases of a compiler, compiler vs. interpreter, bootstrapping.
- Readings: Chapter 1 of the textbook.
- Activities: Introduction to the course project.
- Due: N/A

**Week 2: Lexical Analysis**
- Topics: Regular expressions, finite automata, lexical analyzer generators (e.g., Flex).
- Readings: Chapter 3 of the textbook.
- Activities: Lab session: Using Flex to build a lexical analyzer.
- Due: N/A

**Week 3: Lexical Analysis Implementation**
- Topics: Implementation of lexical analyzer, symbol table management.
- Readings: Chapter 3 of the textbook.
- Activities: Lab session: Implementing symbol table.
- Due: N/A

**Week 4: Syntax Analysis: Context-Free Grammars**
- Topics: Context-free grammars, derivations, parse trees, ambiguity.
- Readings: Chapter 4 of the textbook.
- Activities: N/A
- Due: N/A

**Week 5: Syntax Analysis: Top-Down Parsing**
- Topics: Top-down parsing, LL(1) grammars, recursive descent parsing.
- Readings: Chapter 4 of the textbook.
- Activities: Lab session: Implementing a recursive descent parser.
- Due: Programming Assignment 1: Lexical Analyzer (Due end of Week 5)

**Week 6: Syntax Analysis: Bottom-Up Parsing**
- Topics: Bottom-up parsing, LR parsing, SLR parsing.
- Readings: Chapter 4 of the textbook.
- Activities: N/A
- Due: N/A

**Week 7: Syntax Analysis: LR Parsing Implementation**
- Topics: LR(1) and LALR parsing, parser generators (e.g., Yacc/Bison).
- Readings: Chapter 4 of the textbook.
- Activities: Lab session: Using Bison to build a parser.
- Due: N/A

**Week 8: Semantic Analysis: Type Checking**
- Topics: Syntax-directed translation, type systems, type checking.
- Readings: Chapter 6 of the textbook.
- Activities: N/A
- Due: Midterm Exam (Covers Weeks 1-7)

**Week 9: Semantic Analysis: Intermediate Code Generation**
- Topics: Intermediate representations (e.g., three-address code), syntax-directed translation schemes.
- Readings: Chapter 6 of the textbook.
- Activities: Lab session: Generating three-address code.
- Due: N/A

**Week 10: Intermediate Code Generation Implementation**
- Topics: Implementation of intermediate code generation.
- Readings: Chapter 6 of the textbook.
- Activities: N/A
- Due: N/A

**Week 11: Code Generation: Target Code Generation**
- Topics: Target machine architecture, instruction selection, register allocation.
- Readings: Chapter 8 of the textbook.
- Activities: N/A
- Due: N/A

**Week 12: Code Generation: Optimization**
- Topics: Basic blocks, control flow graphs, data flow analysis.
- Readings: Chapter 9 of the textbook.
- Activities: Lab session: Implementing basic code optimization techniques.
- Due: Programming Assignment 2: Parser and Semantic Analyzer (Due end of Week 12)

**Week 13: Code Optimization Techniques**
- Topics: Common subexpression elimination, dead code elimination, loop optimization.
- Readings: Chapter 9 of the textbook.
- Activities: N/A
- Due: N/A

**Week 14: Compiler Project Work**
- Topics: Working on the compiler project.
- Readings: Relevant chapters from the textbook.
- Activities: Project consultation with the instructor.
- Due: N/A

**Week 15: Compiler Project Work**
- Topics: Working on the compiler project.
- Readings: Relevant chapters from the textbook.
- Activities: Project consultation with the instructor.
- Due: N/A

**Week 16: Project Presentations and Final Review**
- Topics: Project presentations, final review of the course material.
- Readings: Review all chapters.
- Activities: Project presentations.
- Due: Compiler Project (Due end of Week 16)

### Assessment Breakdown:
*   Programming Assignments (20%): Two programming assignments focusing on lexical analysis and parsing/semantic analysis.
*   Midterm Exam (30%): Covers the first half of the course, including lexical analysis, parsing, and syntax-directed translation.
*   Compiler Project (30%): A significant project involving the implementation of a complete compiler for a simplified programming language.
*   Final Exam (20%): Comprehensive exam covering all topics in the course.

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%