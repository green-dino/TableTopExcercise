import pandas as pd
import networkx as nx
import json

# Load data from the CSV file (adjust the filename as needed)
csv_filename = 'sp800-53r5-control-catalog.csv'
df = pd.read_csv(csv_filename)

# Create an empty graph
G = nx.Graph()

# Process the CSV data to add nodes and edges
for index, row in df.iterrows():
    control_identifier = row['Control Identifier']
    related_controls = row['Related Controls']
    
    if not pd.isna(related_controls):
        related_controls = related_controls.split(', ')

        # Add nodes for the control and related controls
        G.add_node(control_identifier, label=control_identifier)  # Include the 'label' attribute
        for related_control in related_controls:
            G.add_node(related_control, label=related_control)  # Include the 'label' attribute
            G.add_edge(control_identifier, related_control)

# Export the graph to GraphML format (compatible with Gephi)
graphml_filename = 'your_graph.graphml'
nx.write_graphml(G, graphml_filename)


print(f"Graph data exported to '{graphml_filename}' in GraphML format.")