# Course Syllabus
## Course Title: Parallel Computing
**Course Code:** CS421
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides an introduction to the fundamental concepts and techniques of parallel computing. Students will learn about various parallel programming models, including shared memory, message passing, and data parallelism, and how to implement them using industry-standard libraries and frameworks. The course will also cover parallel architectures and performance analysis, equipping students with the knowledge and skills to design, implement, and evaluate parallel programs for a variety of applications.

### Prerequisites:
Data Structures and Algorithms, Computer Architecture

### Learning Objectives:
1.  Understand the fundamental concepts of parallel computing, including speedup, efficiency, and Amdahl's Law.
2.  Implement parallel algorithms using shared memory programming models (e.g., OpenMP).
3.  Develop parallel applications using message passing interface (MPI).
4.  Utilize GPU programming frameworks (e.g., CUDA) for data-parallel computations.
5.  Analyze the performance of parallel programs and identify optimization opportunities.
6.  Evaluate different parallel architectures and their suitability for specific applications.

### Required Textbooks:
- Peter S. Pacheco, *An Introduction to Parallel Programming*, Morgan Kaufmann, 2011 (ISBN: 978-0123742605)

### Recommended Readings:
- Article: "CUDA Zone: A History of GPUs", *IEEE Computer Graphics and Applications*, 30(6):14-19, 2010.

### Weekly Schedule:
**Week 1: Introduction to Parallel Computing**
- Topics: Motivation for parallel computing, Flynn's Taxonomy, Amdahl's Law, Speedup and Efficiency.
- Readings: Pacheco, Chapter 1
- Activities: Introduction to the course and parallel computing concepts.
- Due: N/A

**Week 2: Parallel Architectures**
- Topics: Shared memory architectures, Distributed memory architectures, Interconnection networks.
- Readings: Pacheco, Chapter 2
- Activities: Discussion on different parallel architectures.
- Due: N/A

**Week 3: Shared Memory Programming with OpenMP**
- Topics: OpenMP programming model, Parallel regions, Work sharing constructs.
- Readings: Pacheco, Chapter 3
- Activities: Lab session: Introduction to OpenMP.
- Due: N/A

**Week 4: OpenMP: Synchronization and Data Sharing**
- Topics: Synchronization constructs (locks, barriers), Data sharing attributes.
- Readings: Pacheco, Chapter 4
- Activities: Lab session: OpenMP synchronization and data sharing.
- Due: N/A

**Week 5: Message Passing Interface (MPI)**
- Topics: MPI programming model, Point-to-point communication.
- Readings: Pacheco, Chapter 5
- Activities: Lab session: Introduction to MPI.
- Due: N/A

**Week 6: MPI: Collective Communication**
- Topics: Collective communication operations (broadcast, gather, scatter, reduce).
- Readings: Pacheco, Chapter 6
- Activities: Lab session: MPI collective communication.
- Due: Project Proposal

**Week 7: Parallel Algorithm Design: Decomposition Techniques**
- Topics: Domain decomposition, Functional decomposition.
- Readings: Pacheco, Chapter 7
- Activities: Discussion on parallel algorithm design.
- Due: N/A

**Week 8: Parallel Algorithm Design: Task Scheduling**
- Topics: Static scheduling, Dynamic scheduling.
- Readings: Pacheco, Chapter 8
- Activities: Lab session: Implementing different task scheduling algorithms.
- Due: N/A

**Week 9: Introduction to GPU Computing**
- Topics: GPU architecture, CUDA programming model.
- Readings: CUDA Programming Guide
- Activities: Introduction to CUDA.
- Due: N/A

**Week 10: CUDA: Memory Management**
- Topics: Global memory, Shared memory, Constant memory.
- Readings: CUDA Programming Guide
- Activities: Lab session: CUDA memory management.
- Due: N/A

**Week 11: CUDA: Kernel Optimization**
- Topics: Thread divergence, Memory access patterns.
- Readings: CUDA Programming Guide
- Activities: Lab session: CUDA kernel optimization.
- Due: Project Progress Report

**Week 12: Hybrid Programming: MPI and OpenMP**
- Topics: Combining MPI and OpenMP for hybrid parallelism.
- Readings: Research papers on hybrid programming
- Activities: Discussion on hybrid programming.
- Due: N/A

**Week 13: Performance Analysis and Tuning**
- Topics: Performance metrics, Profiling tools.
- Readings: Pacheco, Chapter 9
- Activities: Lab session: Performance analysis and tuning.
- Due: N/A

**Week 14: Case Studies in Parallel Computing**
- Topics: Parallel algorithms for scientific computing, data analysis, and machine learning.
- Readings: Research papers on parallel applications
- Activities: Presentation of case studies.
- Due: N/A

**Week 15: Project Presentations**
- Topics: Student presentations of their parallel computing projects.
- Readings: N/A
- Activities: Project presentations.
- Due: N/A

**Week 16: Final Project Report Due**
- Topics: N/A
- Readings: N/A
- Activities: N/A
- Due: Final Project Report

### Assessment Breakdown:
*   **Programming Projects (60%):** Three programming projects designed to provide hands-on experience with shared memory programming (OpenMP), message passing (MPI), and GPU programming (CUDA). Each project requires a detailed report explaining the design, implementation, and performance analysis of the parallel solution.
*   **Project Proposal (5%):** A detailed proposal outlining the objectives, methodology, and expected outcomes of the final project.
*   **Project Progress Report (5%):** A mid-term report detailing the progress made on the final project, including preliminary results and any challenges encountered.
*   **Final Project Report (30%):** A comprehensive report documenting the design, implementation, and evaluation of the final parallel computing project.

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%