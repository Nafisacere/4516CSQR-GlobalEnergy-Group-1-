# Import the necessary libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

# Load the data from a CSV file
file_path = "C:/Users/EmanS/Documents/GitHub/4516CSQR-GlobalEnergy-Group-1-/Cleaned_Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

# Calculate the yearly energy trend by grouping the data by year
# Finding the average monthly usage for each year
yearly_energy_trend = data.groupby('Year')['Monthly_Usage_kWh'].mean().reset_index()

# Set the figure size for the line graph
plt.figure(figsize=(10, 6))  

# Plot the average monthly energy usage over the years and format the line and markers
plt.plot(
    yearly_energy_trend['Year'],  # X-axis: Year
    yearly_energy_trend['Monthly_Usage_kWh'],  # Y-axis: Average Monthly Usage
    marker='o',  
    markersize=9,  
    markerfacecolor='r',  
    markeredgecolor='k',  
    linestyle='-',  
    color='k',  
    linewidth=2,  
    label='Average Monthly Usage'  # Label for the legend
)

# Add a title and labels to the plot
plt.title('Trend in Average Monthly Energy Usage (2020-2024)', fontsize=14)  # Title of the plot
plt.xlabel('Year', fontsize=12) # Label for the X-axis
plt.ylabel('Average Monthly Usage (kWh)', fontsize=12)  # Label for the Y-axis

# Add a grid to the plot for better readability
plt.grid(True, linestyle='--', alpha=0.7)  

# Set the x axis to show each year
plt.xticks(yearly_energy_trend['Year'])  

# Add a legend to explain what the line represents
plt.legend(loc='upper left', fontsize=12)  

# Adjust the layout to ensure everything fits well
plt.tight_layout()

# Display the graph
plt.show()  

