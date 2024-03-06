import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges between nodes
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k')

# Show the plot
plt.show()
