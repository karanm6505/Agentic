**
# Course Syllabus
## Course Title: Graph Neural Networks
**Course Code:** CS490
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
This course provides an introduction to graph neural networks (GNNs), a class of neural networks designed to operate on graph-structured data. Students will learn the fundamental concepts behind GNNs, including graph representation learning, message passing, and different GNN architectures. The course will cover both theoretical foundations and practical applications of GNNs in various domains such as social network analysis, recommendation systems, and bioinformatics. Students will gain hands-on experience implementing and applying GNNs using popular deep learning frameworks.

### Prerequisites:
Data Structures and Algorithms, Linear Algebra, Probability and Statistics, Machine Learning, Python Programming

### Learning Objectives:
1.  Understand the fundamental concepts of graph theory and graph representation learning.
2.  Implement various graph neural network architectures, including GCNs, GATs, and GraphSAGE.
3.  Apply GNNs to solve real-world problems in domains such as social network analysis and recommendation systems.
4.  Evaluate the performance of GNN models and compare different architectures.
5.  Analyze the limitations of GNNs and explore potential solutions.
6.  Design and implement a GNN-based project to address a specific problem.

### Required Textbooks:
- Kipf, T. N., & Welling, M. *Semi-Supervised Classification with Graph Convolutional Networks*. ICLR, 2017. (Available online)
- Hamilton, W. L. *Graph Representation Learning*. Morgan & Claypool Publishers, 2020. (ISBN: 978-1681737109)

### Recommended Readings:
- Battaglia, P. W., Hamrick, J. B., Bapst, V., Sanchez-Gonzalez, A., Zambaldi, V., Malinowski, M., ... & Pascanu, R. *Relational inductive biases, deep learning, and graph networks*. *arXiv preprint arXiv:1806.01261*, 2018.
- Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. *Graph Attention Networks*. ICLR, 2018.

### Weekly Schedule:
**Week 1: Introduction to Graph Neural Networks**
- Topics: Introduction to graphs, graph representations, applications of graph neural networks.
- Readings: Hamilton, Chapter 1; Kipf & Welling, Section 1-2.
- Activities: Introduction to graph data structures and libraries.
- Due: N/A

**Week 2: Graph Theory Fundamentals**
- Topics: Basic graph properties, graph traversal algorithms, network analysis.
- Readings: Hamilton, Chapter 2.
- Activities: Lab session: Graph traversal and network analysis in Python.
- Due: N/A

**Week 3: Spectral Graph Theory**
- Topics: Laplacian matrix, graph Fourier transform, spectral clustering.
- Readings: Chung, F. R. K. *Spectral Graph Theory*. American Mathematical Society, 1997, Chapter 1-2.
- Activities: Discussion on spectral properties of graphs.
- Due: N/A

**Week 4: Introduction to Neural Networks**
- Topics: Feedforward networks, backpropagation, activation functions.
- Readings: Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016, Chapter 6.
- Activities: Review of basic neural network concepts.
- Due: N/A

**Week 5: Graph Convolutional Networks (GCNs)**
- Topics: Convolutional operations on graphs, GCN architecture, layer-wise propagation.
- Readings: Kipf & Welling, Section 3.
- Activities: Lab session: Implementing GCNs in PyTorch.
- Due: Programming Assignment 1: Implement a basic GCN (Due Week 6)

**Week 6: GCN Variants and Applications**
- Topics: Different GCN architectures, applications in node classification and link prediction.
- Readings: Hamilton, Chapter 4.
- Activities: Discussion on GCN applications.
- Due: Programming Assignment 1: Implement a basic GCN

**Week 7: Graph Attention Networks (GATs)**
- Topics: Attention mechanism, GAT architecture, multi-head attention.
- Readings: Veličković et al., Section 3.
- Activities: Lab session: Implementing GATs in TensorFlow.
- Due: N/A

**Week 8: GAT Applications and Comparison with GCNs**
- Topics: Applications of GATs, comparison with GCNs, advantages and disadvantages.
- Readings: Veličković et al., Section 4.
- Activities: Comparison of GCN and GAT performance on different datasets.
- Due: N/A

**Week 9: GraphSAGE**
- Topics: Inductive learning on graphs, GraphSAGE architecture, sampling strategies.
- Readings: Hamilton, Ying, & Leskovec. *Inductive Representation Learning on Large Graphs*. NeurIPS, 2017.
- Activities: Lab session: Implementing GraphSAGE in PyTorch Geometric.
- Due: Programming Assignment 2: Implement GraphSAGE (Due Week 10)

**Week 10: GraphSAGE Applications**
- Topics: Applications of GraphSAGE in large-scale graph data.
- Readings: Hamilton, Ying, & Leskovec. *Inductive Representation Learning on Large Graphs*. NeurIPS, 2017.
- Activities: Discussion on GraphSAGE applications.
- Due: Programming Assignment 2: Implement GraphSAGE

**Week 11: Graph Autoencoders**
- Topics: Autoencoders, graph autoencoders, variational graph autoencoders.
- Readings: Kipf & Welling. *Variational Graph Auto-Encoders*. NIPS Workshop, 2016.
- Activities: Lab session: Implementing graph autoencoders.
- Due: N/A

**Week 12: Advanced GNN Architectures**
- Topics: Message passing neural networks, graph isomorphism networks.
- Readings: Gilmer et al. *Message Passing Neural Networks*. ICML, 2017.
- Activities: Discussion on advanced GNN architectures.
- Due: Project Proposal Due

**Week 13: Applications in Social Network Analysis**
- Topics: Community detection, social influence analysis, fake news detection.
- Readings: Research papers on GNNs for social network analysis.
- Activities: Guest speaker: Social network analysis with GNNs.
- Due: N/A

**Week 14: Applications in Recommendation Systems**
- Topics: Collaborative filtering, knowledge graph-based recommendation.
- Readings: Research papers on GNNs for recommendation systems.
- Activities: Discussion on GNNs for recommendation systems.
- Due: N/A

**Week 15: Project Presentations**
- Topics: Student project presentations.
- Readings: N/A
- Activities: Project presentations.
- Due: N/A

**Week 16: Project Presentations and Wrap-up**
- Topics: Final project presentations, course review.
- Readings: N/A
- Activities: Project presentations and course wrap-up.
- Due: Final Project Report (Due at the end of the week)

### Assessment Breakdown:
- Programming Assignments (40%): Two programming assignments focusing on implementing GCN and GraphSAGE models.
- Final Project (60%): A project involving the design, implementation, and evaluation of a GNN model for a specific problem. Includes a project proposal (5%), presentation (15%), and final report (40%).

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%