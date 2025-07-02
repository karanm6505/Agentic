**
# Course Syllabus
## Course Title: Mixed-Signal Circuit Design
**Course Code:** EE 335
**Credits:** 3
**Semester:** Fall 2024
**Instructor:** [Instructor Name Placeholder]
**Contact:** instructor.email@university.edu
**Office Hours:** Tuesdays & Thursdays 2:00 PM - 3:00 PM or By Appointment

### Course Description:
This course provides a comprehensive introduction to the design and analysis of mixed-signal integrated circuits. Students will learn the fundamental principles of both analog and digital circuit design, emphasizing their integration and interaction. Key topics include data converters (ADCs and DACs), switched-capacitor circuits, sample-and-hold circuits, phase-locked loops (PLLs), and oscillator design. Students will gain practical experience using industry-standard simulation tools (e.g., Cadence) to design, simulate, and analyze mixed-signal circuits. The course emphasizes understanding performance trade-offs, power consumption, area considerations, and layout issues.

### Prerequisites:
EE 201 (Circuit Analysis I), EE 211 (Digital Logic Design)

### Learning Objectives:
1.  Analyze the performance characteristics of analog-to-digital converters (ADCs) and digital-to-analog converters (DACs), including key specifications such as ENOB, INL, and DNL.
2.  Design and simulate switched-capacitor circuits for signal processing applications, including filters and amplifiers, considering noise and gain.
3.  Implement sample-and-hold circuits and understand their impact on system performance, including aperture error, jitter, and droop, and design considerations.
4.  Evaluate the design considerations for phase-locked loops (PLLs) and oscillators, including stability, phase noise, and frequency synthesis techniques.
5.  Apply simulation tools (e.g., Cadence) to design, simulate, and analyze mixed-signal integrated circuits, including transient, AC, and noise analysis.
6.  Develop a comprehensive design report detailing the design, simulation, and analysis of a mixed-signal circuit, including layout considerations and parasitic effects, and compare and contrast different design approaches.
7.  Compare and contrast various mixed-signal circuit architectures, considering trade-offs in performance, power consumption, area, cost, and process variations.

### Required Textbooks:
- Behzad Razavi, *Design of Analog CMOS Integrated Circuits*, McGraw-Hill Education, 2016 (ISBN: 978-0071257608)

### Recommended Readings:
- None

### Weekly Schedule:
**Week 1: Introduction to Mixed-Signal Design**
- Topics: Course overview, design flow, analog and digital interface, challenges in mixed-signal design, introduction to Cadence simulation tools (e.g., Virtuoso), review of basic circuit concepts (MOSFET operation, biasing, small-signal analysis).
- Readings: Razavi, Chapter 1
- Activities: Lab: Introduction to Cadence, schematic capture, simulation setup, and basic circuit simulation (e.g., DC operating point, transient analysis of a simple inverter, amplifier).
- Due: N/A

**Week 2: Analog-to-Digital Converters (ADCs) - Part 1**
- Topics: ADC specifications (ENOB, SNR, SFDR, THD, etc.), sampling, quantization, Nyquist rate, aliasing, and signal reconstruction; introduction to different ADC types.
- Readings: Razavi, Chapter 17
- Activities: Simulation of ideal samplers and quantizers, introduction to sampling theorem, and aliasing effects; Matlab simulation of quantization noise.
- Due: Homework 1: ADC Specification Analysis

**Week 3: Analog-to-Digital Converters (ADCs) - Part 2**
- Topics: ADC architectures: Flash, Successive Approximation, integrating ADCs, and performance analysis; comparison of different ADC architectures.
- Readings: Razavi, Chapter 17
- Activities: Simulation of Flash ADC, performance evaluation, and comparison of architectures; design of a simple successive approximation ADC using Verilog-A.
- Due: Quiz 1: ADC Principles

**Week 4: Digital-to-Analog Converters (DACs) - Part 1**
- Topics: DAC specifications (INL, DNL, settling time), current steering DACs, and design considerations; layout considerations for matching.
- Readings: Razavi, Chapter 18
- Activities: Design and simulation of current steering DACs, including layout considerations for matching (e.g., common centroid); Monte Carlo simulation for mismatch analysis.
- Due: Homework 2: DAC Design

**Week 5: Digital-to-Analog Converters (DACs) - Part 2**
- Topics: Resistor string DACs, charge redistribution DACs, noise considerations, and dynamic performance; comparison of different DAC architectures.
- Readings: Razavi, Chapter 18
- Activities: Simulation of resistor string DAC, comparison of architectures, and noise analysis; design of a charge redistribution DAC.
- Due: Quiz 2: DAC Architectures

**Week 6: Switched-Capacitor Circuits - Part 1**
- Topics: Switched-capacitor fundamentals, charge transfer, parasitic-insensitive circuits, switched-capacitor amplifiers, and basic building blocks (integrators, amplifiers).
- Readings: Razavi, Chapter 9
- Activities: Lab: Implementing a switched-capacitor integrator, simulation, and analysis, including gain, bandwidth, and noise; design of a SC amplifier.
- Due: Project Proposal

**Week 7: Switched-Capacitor Circuits - Part 2**
- Topics: Switched-capacitor filters, design examples, noise analysis in switched-capacitor circuits, and design trade-offs; filter design methodology.
- Readings: Razavi, Chapter 9
- Activities: Simulation of switched-capacitor filters, filter performance evaluation, and sensitivity analysis; design and simulation of a SC filter.
- Due: Homework 3: Switched-Capacitor Filter Design

**Week 8: Sample-and-Hold Circuits**
- Topics: Sample-and-hold architectures, aperture error, jitter, droop, noise in sample-and-hold circuits, and design trade-offs, and performance limitations; design considerations for high-speed applications.
- Readings: Razavi, Chapter 10
- Activities: Lab: Design and simulation of a sample-and-hold circuit, transient and AC analysis, and performance evaluation; jitter analysis and design.
- Due: Midterm Exam

**Week 9: Phase-Locked Loops (PLLs) - Part 1**
- Topics: PLL fundamentals, basic building blocks (phase detector, charge pump, loop filter, VCO), PLL transfer function, and stability analysis; introduction to PLL applications.
- Readings: Razavi, Chapter 13
- Activities: Introduction to PLL simulation, basic PLL design, and loop filter design; PLL design using a behavioral model.
- Due: N/A

**Week 10: Phase-Locked Loops (PLLs) - Part 2**
- Topics: Charge-pump PLLs, loop filters, jitter analysis, stability considerations, and design examples, and advanced PLL architectures (e.g., fractional-N).
- Readings: Razavi, Chapter 13
- Activities: PLL simulation and analysis, stability analysis (Bode plots), jitter calculations, and performance evaluation; design of a charge-pump PLL.
- Due: Homework 4: PLL Design

**Week 11: Oscillators**
- Topics: Ring oscillators, LC oscillators, phase noise, oscillator design considerations, and design examples, and frequency stability; oscillator phase noise analysis.
- Readings: Razavi, Chapter 14
- Activities: Oscillator design and simulation, phase noise analysis (using Cadence PNOISE simulation), and performance evaluation; design of a ring oscillator and an LC oscillator.
- Due: Quiz 3: PLL and Oscillator Principles

**Week 12: Layout Considerations and Parasitic Effects**
- Topics: Layout techniques, matching, shielding, substrate noise, impact of parasitics on performance, and design rules, and introduction to layout tools (e.g., Cadence layout editor); layout best practices.
- Readings: Razavi, Chapter 11
- Activities: Layout of basic analog blocks (e.g., current source, amplifier), introduction to layout tools, parasitic extraction, and layout verification (DRC, LVS).
- Due: N/A

**Week 13: Mixed-Signal System Design**
- Topics: System-level considerations, interfacing analog and digital blocks, power supply design, clock distribution, ESD protection, and case studies, and system-level noise analysis; design challenges in mixed-signal systems.
- Readings: Selected papers (provided by instructor) on mixed-signal system design.
- Activities: Discussion of mixed-signal system design, case studies (e.g., a specific data converter application), and design challenges; system-level simulations.
- Due: Progress Report 1: Preliminary Design

**Week 14: Design Project Work - Part 1**
- Topics: Students work on their final design projects, including schematic capture, simulation, and initial layout, with instructor guidance, and project planning and initial design reviews; project specific challenges.
- Readings: N/A
- Activities: Lab sessions for project work, instructor consultation, debugging, and design reviews; project milestone review and feedback.
- Due: N/A

**Week 15: Design Project Work - Part 2**
- Topics: Students continue working on their final design projects, completing simulations, layout, and performance analysis, with instructor guidance, and final design verification and optimization; project specific challenges and solutions.
- Readings: N/A
- Activities: Lab sessions for project work, instructor consultation, final debugging, and design reviews; project milestone review and feedback.
- Due: Progress Report 2: Simulation Results

**Week 16: Final Project Presentations and Report Submission**
- Topics: Student presentations, final report submission, peer review, and grading, and course review; final project presentation guidelines and feedback.
- Readings: N/A
- Activities: Final project presentations, Q&A, peer review of final reports, and course wrap-up; final project report submission and grading.
- Due: Final Design Report

### Assessment Breakdown:
- Exams: 30% (Midterm: 15%, Final: 15%)
- Circuit Simulation Projects: 40% (including homework assignments, lab exercises, and project components)
- Design Report: 20%
- Quizzes: 10% (3 quizzes)

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%