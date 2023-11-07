import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import json

# Load data from the CSV file (adjust the filename as needed)
csv_filename = 'sp800-53r5-control-catalog.csv'
df = pd.read_csv(csv_filename)



# Create a list of unique control identifiers
unique_controls = list(set(df['Control Identifier']))

# Create a list of unique related controls by filtering out NaN values
unique_related_controls = list(set(df['Related Controls'].str.split(', ').explode().dropna()))

# Combine unique controls and related controls
all_nodes = unique_controls + unique_related_controls

# Create a dictionary to assign numeric IDs to nodes
node_ids = {node: i for i, node in enumerate(all_nodes)}

# Create source and target indices for edges, handling NaN values
source_indices = []
target_indices = []

for _, row in df.iterrows():
    control_identifier = row['Control Identifier']
    related_controls = row['Related Controls']

    if not pd.isna(related_controls):
        related_controls = related_controls.split(', ')
        for related in related_controls:
            source_indices.append(node_ids[control_identifier])
            target_indices.append(node_ids[related])

# Create a Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=[1] * len(source_indices)  # You can customize the values as needed
    )
))

# Customize the Sankey diagram layout
fig.update_layout(title_text="Control Relationships - Sankey Diagram", font_size=10)

# Show the Sankey diagram
fig.show()
