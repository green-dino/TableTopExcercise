import pandas as pd
import networkx as nx
from networkx.algorithms import community
from pyvis.network import Network

df = pd.read_csv('sp800-53r5-control-catalog.csv')

# Create an empty graph
G = nx.Graph()

# Process the "Control Identifier" and "Related Controls" columns to add edges to the graph
for index, row in df.iterrows():
    control_identifier = row['Control Identifier']
    related_controls = row['Related Controls']
    
    if not pd.isna(related_controls):
        related_controls = related_controls.split(', ')

        # Add nodes for the control and related controls
        G.add_node(control_identifier)
        for related_control in related_controls:
            G.add_node(related_control)
            G.add_edge(control_identifier, related_control)

# Perform community detection
communities = list(community.greedy_modularity_communities(G))

# Create a pyvis Network instance
net = Network(height="100%", width="100%", directed=True, notebook=True, select_menu=True, filter_menu=True)

# Add nodes and edges to the pyvis Network with positions
for node, (x, y) in nx.spring_layout(G, seed=42).items():
    net.add_node(node, x=x, y=y)

for edge in G.edges():
    net.add_edge(edge[0], edge[1])

# Save the plot as an HTML file
net.show_buttons(filter_=['physics'])
net.write_html('control_communities_pyvis.html')
