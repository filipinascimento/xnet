# XNET File format (xnetwork)

`xnetwork` is a small python package that allows you to read `.xnet` files (compleX NETwork format), a format designed to easily handle graph data with multiple attributes.

This file format is used across several of my other projects, including [Helios-Web](http://heliosweb.io).

### Installation

You can easily install `xnetwork` by using `pip`:

```bash
pip install xnetwork
```

### Usage

#### Loading a Graph

To read a Graph from a `.xnet` formatted file, simply use the `load` function:

```python
from xnetwork import load

graph = load("path_to_file.xnet")
```

#### Saving a Graph

To save a graph object to `.xnet` format:

```python
from xnetwork import save
from igraph import Graph

# Your igraph graph object
g = Graph()

save(g, "output_file.xnet")
```

### .xnet Format

A brief overview of the `.xnet` format:

```
#vertices <number_of_vertices>
<Vertex 0 name>
<Vertex 1 name>
...

#edges weighted|nonweighted undirected|directed
<source_vertex> <target_vertex> [weight]
...

#v "<vertex_attribute_name>" s|n|v2|v3
<attribute_value>
...

#e "<edge_attribute_name>" s|n|v2|v3
<attribute_value>
...
```


 - The `#vertices` tag specifies the number of vertices in the graph, followed by their labels.
  
 - The `#edges` tag specifies if edges are weighted or non-weighted and whether they are directed or undirected. Each subsequent line lists an edge by its source and target vertices, optionally followed by a weight in square brackets.

 - The `#v` and `#e` tags specify vertex and edge attributes respectively. These tags are followed by the attribute name and its type. The type can be a string (`s`), number (`n`), 2D vector (`v2`), or 3D vector (`v3`).

 - 

### Example

Consider the following `.xnet` file:

```
#vertices 4 
"Label 0"
"Label 1"
...
#edges weighted undirected
0 1 [0.1]
0 2 [0.2]
...
#v "A string property" s
"A string value"
"Another string value"
...
```

This represents a graph with 4 vertices and 2 weighted, undirected edges.

### API Reference
### load(fileName='test.xnet', compressed=False)

Read a Graph from a xnet formatted file.

#### Parameters
- `fileName` : string
    Input file path.
- `compressed` : bool
    If True, input file is compressed using gzip.

#### Returns
- `igraph.Graph` : The graph object loaded from the file.

### save(g, fileName='test.xnet', ignoredNodeAtts=[], ignoredEdgeAtts=[], compressed=False)

Write igraph object to .xnet format.

Vertex attributes 'name' and 'weight' are treated in a special manner. They correspond to attributes assigned inside the #vertices tag. Edge attribute 'weight' is assigned to edges inside the #edges tag.

#### Parameters
- `g` : igraph.Graph
    Input graph.
- `fileName` : string
    Output file.
- `ignoredNodeAtts` : list
    List of node attributes to ignore when writing graph.
- `ignoredEdgeAtts` : list
    List of edge attributes to ignore when writing graph.
- `compressed` : bool
    If True, output file will be compressed using gzip.

#### Returns
- `None` : The function saves the graph object to the specified file.

 

### Special network attribute names
Some attribute names are interpreted by certain software in different ways.
 - Node attribute named `Label` is interpreted as vertex label.
 - Node attribute named `Position` is interpreted as vertex position (can be v2 or v3).
 - Node attribute named `weight` is interpreted as edge weight.

### Authors

- Filipi N. Silva (filipi@iu.edu)
- Cesar H. Comin

### License

This project is licensed under the MIT License.

### Links

- [GitHub Repository](https://github.com/filipinascimento/xnet)

---

Feel free to contribute and raise issues on the GitHub repository.
