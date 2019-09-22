# Labyrinth

## Purpose

A labyrinth is a representation of a simple graph with named nodes and undirected eges. Each node may have a color token as well. Labyrinth is a singular module with the following functions on it. The module is written in Python 3.

## Methods

The constructor will ensure that the undirected unweighted graph is a simple graph with no self edges, or multiple edges with the same pair of nodes. The nodes will default to have no colored token. The names of the nodes must be unique. The nodes and edges may be empty to start.

`init(nodes: list[string], edges: dict[node: string-> nodes: list[string]]) : Labyrinth`

Adds a node to the graph with no specified color token or any edges connected to it
`node`: the unique name of the given node

`addNode(node: string) : void`

Adds an undirected edge between the two nodes
`node1`: the first vertex of the edge to add
`node2`: the second vertex of the edge to add

`addEdge(node1: string, node2: string): void`

Removes a node from the graph, removing its color, and removing all undirected edges. If the node does not exist the method does nothing.
`node`: the name of the node to remove

`removeNode(node: string): void`

Removes an edge from the graph, if the edge does not exist the method does nothing
`node1`: the vertex of the edge to remove
`node2`: the other vetex of the edge to remove

`removeEdge(node1: string, node2: string): void`

Changes the color token of the node with the given color. Different nodes can have the same color
`node`: the name of the node that will have a token added
`color`: the color of the token

`changeColor(node: string, color: string): void`

retrieves the color token of the node
`node`: the name of the node

`getColor(node: string) : string`

checks if any node with the given color an reach the named node
`color`: the color of the token to be queried from
`node`: the name of the node to find a path to

`query(color: string, node: string) : boolean`
