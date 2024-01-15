# Alkın Şahin 200218020 Algorithm Analysis Project
Algorithm Analysis Project: Network Topology Optimization

We would like to extend our appreciation to Dr. Evrim Güler [ (https://github.com/evrimguler) ], our esteemed teacher, for his invaluable guidance and challenging assignments that have prepared us for this project. We are three dedicated students - Alper Akkaya ( 210212027 ), Alkın Şahin ( 200218020 ) and Kutay Yeşilyurt ( 200218022 ) - collaborating on a Python-based project for our Algorithm Analysis class.

Project Overview: Our project revolves around optimizing a US backbone topology comprising 24 nodes and 43 edges. The input file includes adjacency, bandwidth, delay, and reliability matrices. The matrices are separated by colons, with each matrix separated by an empty row. Noteworthy points include:

In the neighborhood matrix, link distances range uniformly from 1 to 5. Bandwidth matrix values are uniformly distributed between 3 and 10. The delay matrix follows a uniform distribution between 1 and 5. Reliability matrix values fall between 0.95 and 0.99. Request and Solution: Requests contain source and destination node IDs along with bandwidth requirements. The Solution function, designed in Python, takes the input text file and the request as parameters. The objective is to find the shortest path between the source and destination, adhering to specific constraints:

Bandwidth demand must be 5. The delay threshold should be less than 40. Reliability threshold must exceed 0.70. Implemented Algorithms: To solve the problem, we have implemented three algorithms:

Dijkstra's Algorithm Bellman-Ford Algorithm A Algorithm* Flody-Warshall Algorithm Equation Overview: In the given equation, Graph (G) comprises vertices and edges (G=(V,E)). For two vertices i and j in the graph, ij denotes an edge in the edge set. Key notations include:

bw: Bandwidth demand. 𝛿𝑖𝑗: Binary indicator, 1 if edge (i, j) is used, 0 otherwise. 𝑑𝑖𝑠𝑡𝑖𝑗: Edge distances between i and j.

Input File: [text.txt]

Feel free to explore our GitHub profiles for more details:

Alper Akkaya's GitHub [ (https://github.com/AlperBekir) ] Alkın Şahin's GitHub [ (https://github.com/SaaazDack77) ] Kutay Yeşilyurt's GitHub [ (https://github.com/KutisTR) ]

We look forward to presenting the results of our project and appreciate the opportunity to apply our algorithmic skills to real-world scenarios.
