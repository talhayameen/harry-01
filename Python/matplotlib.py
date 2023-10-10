import yaml
import networkx as nx
import matplotlib.pyplot as plt

# Load YAML data (you can replace this with your YAML data)
yaml_data = """
graph:
  - A
  - B
  - C
edges:
  - [A, B]
  - [B, C]
"""

data = yaml.safe_load(yaml_data)

# Create a directed graph
G = nx.DiGraph()

# Add nodes
if 'graph' in data:
    G.add_nodes_from(data['graph'])

# Add edges
if 'edges' in data:
    G.add_edges_from(data['edges'])

# Visualize the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=20, arrows=True, connectionstyle='arc3,rad=0.1')
plt.show()
