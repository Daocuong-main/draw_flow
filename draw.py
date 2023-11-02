# Import the necessary modules
import torch
import matplotlib.pyplot as plt
import random

# Load the data from data_3.pt file
data = torch.load('data_3.pt')

# Define the labels for each class
labels = ['E-commerce', 'Video on-demand', 'Interactive data']
n=3
# Loop through the n tensors in the data
for i in range(n):
    # Get the tensor and the label from the data
    tensor, label = data[random.randint(0, len(data) - 1)]
    
    # Create a figure and an axis for plotting
    fig, ax = plt.subplots(figsize=(32, 32))

    tensor = tensor[0]

    print(type(tensor))
    # Plot the tensor as an image
    ax.imshow(tensor, cmap='gray', aspect='auto')

    # # Set the title of the plot as the label
    # ax.set_title(labels[label], fontdict={'fontsize': 32}, loc='left')
    
    # Remove the axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Adjust the figure margins to fit the image to the frame
    fig.tight_layout()

    # Save the figure as svg format
    fig.savefig(f'tensor_{i}.svg', transparent=True)

