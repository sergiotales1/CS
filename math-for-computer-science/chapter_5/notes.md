# Graph

Graphs are structures built with objects (vertices or nodes) that have a relationship with each other. They're connected by edges.

## Incidence and adjacency

### Adjacent

Two vertices are adjacent if an edge is in between them:

Example: the edge E = {u, v} makes the u and v vertices be adjacent.

### Incident

An edge that connects two vertices is called incident

Example: the edge E = {u, v} is an incident to vertex u and is also an incident to vertex v.

### Degree

The degree of a vertex is the count of how many edges are incident to it. It's essentially the number of connections a vertex has to other vertices. The degree of a vertex v is denoted as deg(v). An equivalent way to think about it is that the degree of a vertex is the number of vertices adjacent to it.

Example, if a vertex v is connected to three other distinct vertices, its degree, deg(v), is 3.

## Subgraph

A subgraph is a smaller graph that is "part of" a larger graph. Think of it like taking a few nodes and their connecting edges from a bigger network.

It's basically a little part of a graph that has some of the vertices and edges from the bigger graph.

## Weighted Graphs

a weighted graph is a graph where each edge has a numerical value assigned to it. This value is called the weight or cost of the edge.

### Sigma

∑ ​deg(x) - this is saying that for all x belonging to M, we sum its degree.
x∈M

### Bipartite graph

A bipartite graph is a graph whose vertices can be divided into two separate and independent sets, let's call them U and V. The key rule is that every edge in the graph connects a vertex in U to a vertex in V. No edges are allowed to connect two vertices within the same set (e.g., no edges between two vertices in U, or between two vertices in V).

## Handshake lemma

The sum of the degrees of the vertices in a graph equals twice the number of edges.

This occurs because each edge adds 2 to the sum of total degrees. One for each endpoint.
