# Import the necessary libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Patch  # For creating custom legend 

# Load the data from a CSV file
file_path = "C:/Users/EmanS/Documents/GitHub/4516CSQR-GlobalEnergy-Group-1-/Cleaned_Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path) # Read the CSV file into a DataFrame

# Calculate the total energy used by each region and sort it from highest to lowest
total_region_energy = data.groupby("Region")["Monthly_Usage_kWh"].sum().sort_values(ascending=False)

# Set the figure size for the bar chart
plt.figure(figsize=(12, 8))  

# Creating a custom color palette for the bar chart using a colormap
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(total_region_energy)))

# Create the bar chart
bars = plt.bar(total_region_energy.index, total_region_energy, color=colors, edgecolor='black', linewidth=1)

# Add a title and labels to the chart
plt.title("Total Renewable Energy Usage by Region", fontsize=20, pad=20, fontweight='bold')
plt.xlabel("Region", fontsize=14, labelpad=10)
plt.ylabel("Total Monthly Usage (kWh)", fontsize=14, labelpad=10)

# Improve the formatting of the x axis and y axis
plt.xticks(rotation=45, ha='right', fontsize=12)  
plt.yticks(fontsize=12)  
plt.grid(axis='y', linestyle='--', alpha=0.4)  

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()  # the height of the bar
    
    # Add a label directly above the bar formatted and postioned accurately 
    plt.text(
        bar.get_x() + bar.get_width() / 2,  
        height,  
        f"{int(height):,}",  
        ha='center',  
        va='bottom',  
        fontsize=12  
    )

# Create a legend to explain the color coding
legend_elements = [
    Patch(facecolor=plt.cm.viridis(0.5), edgecolor='black', label='Energy Usage (kWh)')  # Creating a custom legend 
]
plt.legend(handles=legend_elements, loc='upper right', fontsize=12)  # Add the legend to the chart

# Adjust the layout to ensure everything fits well
plt.tight_layout()

# Customize the background color of the plot
plt.gca().set_facecolor('#f5f5f5')  

# Display the chart
plt.show()