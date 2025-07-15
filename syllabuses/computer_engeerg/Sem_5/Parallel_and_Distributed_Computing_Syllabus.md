**
# Course Syllabus
## Course Title: Parallel and Distributed Computing
**Course Code:** CS450
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides an introduction to the fundamental concepts of parallel and distributed computing. Students will learn about parallel programming models, distributed system architectures, and concurrency control mechanisms. The course covers both theoretical foundations and practical programming skills, enabling students to design, implement, and analyze parallel and distributed applications. Topics include shared-memory and message-passing programming, distributed consensus, fault tolerance, and performance evaluation.

### Prerequisites:
Data Structures and Algorithms, Computer Architecture

### Learning Objectives:
1.  Explain the fundamental concepts and challenges of parallel and distributed computing.
2.  Implement parallel algorithms using shared-memory and message-passing programming models.
3.  Analyze the performance of parallel and distributed applications.
4.  Design and implement distributed systems with fault tolerance and consistency.
5.  Apply concurrency control mechanisms to ensure data integrity in parallel and distributed environments.
6.  Evaluate different parallel and distributed computing paradigms for specific applications.

### Required Textbooks:
-   Andrew S. Tanenbaum and Maarten Van Steen, *Distributed Systems: Principles and Paradigms*, 3rd Edition, CreateSpace Independent Publishing Platform, 2017. (ISBN: 978-1543057738)
-   Peter Pacheco, *An Introduction to Parallel Programming*, Morgan Kaufmann, 2011. (ISBN: 978-0123742605)

### Recommended Readings:
-   Leslie Lamport, *The Part-Time Parliament*, ACM Transactions on Computer Systems, 16(2):133-169, 1998.
-   Michael J. Fischer, Nancy Lynch, Michael S. Paterson, *Impossibility of Distributed Consensus with One Faulty Process*, Journal of the ACM, 32(2):374-382, 1985.

### Weekly Schedule:
**Week 1: Introduction to Parallel and Distributed Computing**
- Topics: Overview of parallel and distributed systems, motivations and challenges, Flynn's taxonomy.
- Readings: Tanenbaum & Van Steen, Chapter 1; Pacheco, Chapter 1
- Activities: Introduction to the course, discussion of parallel and distributed computing applications.
- Due: N/A

**Week 2: Parallel Programming Models: Shared Memory**
- Topics: Threads, locks, OpenMP, race conditions, data races.
- Readings: Pacheco, Chapter 2, Chapter 3
- Activities: Lab session: Introduction to OpenMP.
- Due: N/A

**Week 3: Parallel Programming Models: Message Passing**
- Topics: MPI, point-to-point communication, collective communication.
- Readings: Pacheco, Chapter 4, Chapter 5
- Activities: Lab session: Introduction to MPI.
- Due: N/A

**Week 4: Performance Analysis of Parallel Programs**
- Topics: Speedup, efficiency, Amdahl's Law, scalability.
- Readings: Pacheco, Chapter 6
- Activities: Analyzing the performance of different parallel algorithms.
- Due: Programming Assignment 1 (OpenMP)

**Week 5: Distributed System Architectures**
- Topics: Client-server, peer-to-peer, cloud computing.
- Readings: Tanenbaum & Van Steen, Chapter 2
- Activities: Discussion of different distributed system architectures.
- Due: N/A

**Week 6: Communication in Distributed Systems**
- Topics: Remote procedure call (RPC), message queuing, distributed object frameworks.
- Readings: Tanenbaum & Van Steen, Chapter 4
- Activities: Case study of a distributed communication system.
- Due: N/A

**Week 7: Time and Global States**
- Topics: Clock synchronization, logical clocks, vector clocks, global state recording.
- Readings: Tanenbaum & Van Steen, Chapter 6
- Activities: Discussion of clock synchronization algorithms.
- Due: N/A

**Week 8: Midterm Exam**
- Topics: All topics covered in weeks 1-7.
- Readings: Review all assigned readings.
- Activities: Midterm exam.
- Due: Midterm Exam

**Week 9: Coordination and Agreement**
- Topics: Distributed mutual exclusion, election algorithms.
- Readings: Tanenbaum & Van Steen, Chapter 5
- Activities: Analysis of different distributed mutual exclusion algorithms.
- Due: N/A

**Week 10: Distributed Consensus**
- Topics: Paxos, Raft, Byzantine fault tolerance.
- Readings: Lamport, *The Part-Time Parliament*; Fischer, Lynch, Paterson, *Impossibility of Distributed Consensus with One Faulty Process*
- Activities: Discussion of consensus algorithms.
- Due: Programming Assignment 2 (MPI)

**Week 11: Fault Tolerance**
- Topics: Failure models, redundancy, replication, checkpointing.
- Readings: Tanenbaum & Van Steen, Chapter 7
- Activities: Case study of a fault-tolerant distributed system.
- Due: N/A

**Week 12: Consistency and Replication**
- Topics: Data-centric consistency models, client-centric consistency models, replica management.
- Readings: Tanenbaum & Van Steen, Chapter 8
- Activities: Discussion of different consistency models.
- Due: N/A

**Week 13: Distributed File Systems**
- Topics: Design principles, examples (e.g., HDFS, NFS).
- Readings: Tanenbaum & Van Steen, Chapter 9
- Activities: Analysis of a distributed file system architecture.
- Due: Project Proposal

**Week 14: Distributed Databases**
- Topics: CAP theorem, distributed transaction management, two-phase commit.
- Readings: Tanenbaum & Van Steen, Chapter 10
- Activities: Discussion of distributed database concepts.
- Due: N/A

**Week 15: Advanced Topics in Parallel and Distributed Computing**
- Topics: Guest lecture or student presentations on advanced topics.
- Readings: Selected research papers.
- Activities: Student presentations.
- Due: Project Report

**Week 16: Final Project Presentations**
- Topics: Student presentations of their parallel computing projects.
- Readings: N/A
- Activities: Final project presentations.
- Due: Final Project Presentation and Code

### Assessment Breakdown:
*   Programming Assignments (20%): Two programming assignments focusing on parallel programming using OpenMP and MPI.
*   Midterm Exam (25%): A comprehensive exam covering the theoretical concepts and algorithms discussed in the first half of the course.
*   Final Project (35%): A significant parallel computing project involving design, implementation, and performance evaluation. Includes a project proposal (5%), a project report (15%), and a final presentation (15%).
*   Final Exam (20%): A comprehensive exam covering all topics discussed throughout the semester.

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%