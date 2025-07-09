# Course Syllabus
## Course Title: Distributed Systems
**Course Code:** CS457
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides a comprehensive introduction to the fundamental concepts, architectures, and algorithms underlying distributed systems. Students will explore topics such as distributed communication, concurrency control, fault tolerance, and consistency models. Through lectures, readings, and hands-on programming projects, students will gain practical experience in designing, implementing, and evaluating distributed systems. The course emphasizes both theoretical foundations and practical applications, preparing students for advanced study or careers in distributed computing.

### Prerequisites:
Data Structures and Algorithms, Operating Systems, Computer Networks

### Learning Objectives:
1.  Explain the core concepts and challenges of distributed systems.
2.  Design and implement distributed algorithms for communication, coordination, and consensus.
3.  Evaluate the performance and reliability of distributed systems.
4.  Compare and contrast different consistency models and their trade-offs.
5.  Apply fault-tolerance techniques to enhance the robustness of distributed systems.
6.  Analyze the security considerations in distributed system design.

### Required Textbooks:
- George Coulouris, Tim Kindberg, Jean Dollimore, Gordon Blair, *Distributed Systems: Concepts and Design*, 5th Edition, Addison-Wesley, 2011 (ISBN: 978-0132143011)

### Recommended Readings:
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System", *Communications of the ACM*, 21(7):558-565, 1978.
- Michael J. Fischer, Nancy Lynch, Michael S. Paterson, "Impossibility of Distributed Consensus with One Faulty Process", *Journal of the ACM*, 32(2):374-382, 1985.

### Weekly Schedule:
**Week 1: Introduction to Distributed Systems**
- Topics: What is a distributed system? Goals, challenges, and examples of distributed systems.
- Readings: Coulouris et al., Chapter 1
- Activities: Introduction to the course, discussion of distributed system examples
- Due: N/A

**Week 2: Architectures for Distributed Systems**
- Topics: Architectural styles, system architectures, middleware, and common platforms.
- Readings: Coulouris et al., Chapter 2
- Activities: Discussion on different architectural styles (e.g., client-server, peer-to-peer)
- Due: N/A

**Week 3: Interprocess Communication**
- Topics: Remote Procedure Call (RPC), Message Passing Interface (MPI), and Distributed Shared Memory (DSM).
- Readings: Coulouris et al., Chapter 4
- Activities: Implement a simple RPC mechanism.
- Due: N/A

**Week 4: Naming**
- Topics: Naming entities, name resolution, and distributed directory services.
- Readings: Coulouris et al., Chapter 5
- Activities: Discussion on DNS and LDAP.
- Due: N/A

**Week 5: Synchronization**
- Topics: Clock synchronization, logical clocks, and global state.
- Readings: Coulouris et al., Chapter 6, Lamport (1978)
- Activities: Implementation of Lamport timestamps.
- Due: N/A

**Week 6: Distributed Mutual Exclusion**
- Topics: Algorithms for mutual exclusion, token-based and non-token-based algorithms.
- Readings: Coulouris et al., Chapter 6
- Activities: Implement a distributed mutual exclusion algorithm.
- Due: Project Proposal Due

**Week 7: Election Algorithms**
- Topics: Bully algorithm, Ring algorithm, and other election algorithms.
- Readings: Coulouris et al., Chapter 6
- Activities: Implementation of the Bully algorithm.
- Due: N/A

**Week 8: Consistency and Replication**
- Topics: Data replication, consistency models, and replica management.
- Readings: Coulouris et al., Chapter 7
- Activities: Discussion on different consistency models (e.g., strict consistency, eventual consistency).
- Due: N/A

**Week 9: Fault Tolerance**
- Topics: Failure models, process resilience, and reliable client-server communication.
- Readings: Coulouris et al., Chapter 8
- Activities: Discussion on different fault tolerance techniques (e.g., checkpointing, replication).
- Due: N/A

**Week 10: Distributed Commit Protocols**
- Topics: Two-phase commit (2PC) and Three-phase commit (3PC).
- Readings: Coulouris et al., Chapter 8
- Activities: Discussion of 2PC and its limitations
- Due: Project Milestone 1 Due

**Week 11: Distributed File Systems**
- Topics: File system design, naming, caching, and consistency.
- Readings: Coulouris et al., Chapter 9
- Activities: Discussion on NFS and HDFS.
- Due: N/A

**Week 12: Distributed Transactions**
- Topics: Transactions, nested transactions, and concurrency control.
- Readings: Coulouris et al., Chapter 10
- Activities: Implementing a simple distributed transaction.
- Due: N/A

**Week 13: Security in Distributed Systems**
- Topics: Security threats, access control, and cryptography.
- Readings: Coulouris et al., Chapter 11
- Activities: Discussion on security protocols (e.g., Kerberos, SSL/TLS).
- Due: N/A

**Week 14: Distributed Object-Based Systems**
- Topics: Distributed objects, remote method invocation (RMI), and object request brokers (ORBs).
- Readings: Coulouris et al., Chapter 12
- Activities: Discussion on CORBA and Java RMI.
- Due: N/A

**Week 15: Case Studies**
- Topics: Google File System (GFS), Apache Hadoop, and Apache Kafka.
- Readings: Research papers on GFS, Hadoop, and Kafka.
- Activities: Presentation and discussion on case studies.
- Due: Project Milestone 2 Due

**Week 16: Review and Project Presentations**
- Topics: Review of key concepts and project presentations.
- Readings: N/A
- Activities: Student project presentations.
- Due: Final Project Report Due

### Assessment Breakdown:
*   **Project Proposal (5%):** A detailed proposal outlining the objectives, design, and implementation plan for the semester-long project.
*   **Project Milestone 1 (15%):** A progress report demonstrating the initial implementation and testing of core project components.
*   **Project Milestone 2 (20%):** A demonstration of the completed project with intermediate results.
*   **Final Project Report (30%):** A comprehensive report detailing the project's design, implementation, evaluation, and results.
*   **Quizzes (30%):** Several quizzes throughout the semester to assess understanding of key concepts and algorithms.

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%