# The chart displays average monthly energy usage (in kWh) for each income group.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and read the csv file
df= pd.read_csv (r"C:\Users\menac\OneDrive\Desktop\csws\4516CSQR-GlobalEnergy-Group-1-\data filtering-cleaning files\Cleaned_Renewable_Energy_Usage_Sampled.csv")

# Group the data by income level and calculate the average energy usage (in specific order)
avg_usage= df.groupby('Income_Level') ['Monthly_Usage_kWh' ].mean( ).reindex(['High', 'Middle', 'Low'])

# Create a bar chart to visualize average energy usage by income level
plt.figure (figsize=(10, 6) )

# Set soft aesthetic bar colors based on income level order
bars = plt.bar(avg_usage.index, avg_usage.values, color=['#E57373', '#BA68C8', '#64B5F6'], edgecolor='black')

# title and axis labels
plt.title ('Average Monthly Energy Usage by Household Income Level', fontsize=16)
plt.xlabel ('Income Level', fontsize=12)
plt.ylabel('Monthly Energy Usage (kWh)',fontsize=12)

# Add the usage values on top of each bar
for bar in bars :
    height = bar.get_height( )
    plt.text(bar.get_x() + bar.get_width()/2, height + 5,  f'{height:.1f} kWh' , 
             ha= 'center', va= 'bottom', fontsize=10)

# Add a horizontal grid for better readability
plt.grid(axis='y',linestyle='--', alpha=0.3)

# Add source information below the chart
plt.figtext(0.01, -0.03, 'Source: Cleaned_Renewable_Energy_Usage_Sampled.csv', fontsize=8)

# Adjust layout to prevent label overlap and show the plot
plt.tight_layout( )
plt.show()

# Print the average usage values in the terminal for reference
print("Average Monthly Energy Usage by Income Level:")
print(avg_usage.round(1) )
