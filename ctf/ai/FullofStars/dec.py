import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.npy.gz")
core_data = np.loadtxt("known_samples.npy.gz")
all_data = np.vstack((core_data, data))
del data

class_count = len(core_data)

out_labels = np.full((all_data.shape[0],), -1)

#Added code here

# Normalising the data for X, Y, Z
x_min, x_max = np.min(all_data[:, 0]), np.max(all_data[:, 0])
y_min, y_max = np.min(all_data[:, 1]), np.max(all_data[:, 1])
z_min, z_max = np.min(all_data[:, 2]), np.max(all_data[:, 2])

# Apply normalisation to each axis across the entire dataset
all_data[:, 0] = (all_data[:, 0] - x_min) / (x_max - x_min)
all_data[:, 1] = (all_data[:, 1] - y_min) / (y_max - y_min)
all_data[:, 2] = (all_data[:, 2] - z_min) / (z_max - z_min)
core_data[:, 0] = (core_data[:, 0] - x_min) / (x_max - x_min)
core_data[:, 1] = (core_data[:, 1] - y_min) / (y_max - y_min)
core_data[:, 2] = (core_data[:, 2] - z_min) / (z_max - z_min)

import plotly.graph_objs as go
import plotly.io as pio
import plotly.colors as pc

valid_indices = np.where(np.where(out_labels != -1)[0])[0] # filter out the unabelled points
valid_labels = out_labels[valid_indices]
valid_stars = all_data[valid_indices]

# Separate core_data points from the valid stars
core_data_indices = np.arange(class_count)
core_data_stars = core_data  # The original labelled stars

# Choose a qualitative colorscale for distinct colors
color_scale = pc.qualitative.Plotly  # You can also try 'D3', 'Set1', etc.

# Create the 3D scatter plot for all stars
trace = go.Scatter3d(
    x=valid_stars[:, 0],
    y=valid_stars[:, 1],
    z=valid_stars[:, 2],
    mode='markers',
    marker=dict(
        size=1,
        color=valid_labels,  # Assign labels to colors
        colorscale=color_scale,  # Use the discrete colorscale
        opacity=0.8,
        colorbar=dict(title='Cluster Label')
    ),
    text=[f"Index: {i}<br>Label: {label}<br>X: {x}<br>Y: {y}<br>Z: {z}"
          for i, (x, y, z), label in zip(valid_indices, valid_stars, valid_labels)],
    hoverinfo='text'  # Display the custom text on hover
)

# Create another scatter plot for the core_data stars with text annotations
core_trace = go.Scatter3d(
    x=core_data_stars[:, 0],
    y=core_data_stars[:, 1],
    z=core_data_stars[:, 2],
    mode='markers+text',
    marker=dict(
        size=2,
        color='red',  # Different color for core_data points
        opacity=0.9,
    ),
    text=[str(i) for i in core_data_indices],  # Display index as text
    textposition='top center'
)

# Set up the layout with increased height
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='X Coordinate'),
        yaxis=dict(title='Y Coordinate'),
        zaxis=dict(title='Z Coordinate')
    ),
    width=1200,  # You can adjust the width here
    height=1200  # Increase the height here
)

# Create the figure with both traces
fig = go.Figure(data=[trace, core_trace], layout=layout)

# Render the plot in the notebook (or in a browser if not using a notebook environment)
pio.show(fig)

###

assert(np.all(np.logical_and(0 <= out_labels, out_labels < 256)))

file_data = bytearray(out_labels[256:].shape[0])
for ix, val in enumerate(out_labels[256:]):
    file_data[ix] = val
file_data = bytes(file_data)
with open("flag.jpg", "wb") as outfile:
    outfile.write(file_data)
del file_data

