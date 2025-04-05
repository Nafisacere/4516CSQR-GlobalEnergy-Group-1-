# Importing libraries needed for data handling, plotting, and the GUI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk #for GUI creation 
from tkinter import ttk

# Load the cleaned energy usage data from a CSV file
file_path = "Cleaned_Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path)

# Group the data by energy source and sum up the cost savings for each
aggregated_data = data.groupby("Energy_Source")["Cost_Savings_USD"].sum()

# Define custom colors for the pie chart sections.
# The colors were changed for a more appropriate representation of the data. 
colors = ['#e80000', '#66b3ff', '#34cd4b', '#d4dd22', '#c2c2f0', '#a82fce']

#To create and display the pie chart when button is clicked
def show_pie_chart():
    plt.figure(figsize=(10, 8)) 
    
    wedges, texts, autotexts = plt.pie(
        aggregated_data,  
        labels=aggregated_data.index,  
        autopct='%1.1f%%',  
        startangle=140,  
        colors=colors,  
        textprops={'fontsize': 12}, 
        wedgeprops={'edgecolor': 'black'}  
    )
    
  # Add a title to the chart
    plt.title("Proportion of Total Cost Savings by Energy Source (Pie-Chart)", fontsize=16, fontweight='bold')
    
  # Add a legend to the side with energy source labels
    plt.legend(wedges, aggregated_data.index, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)

# Adjust layout to make sure everything fits
    plt.tight_layout()
    
# # Display the pie chart
    plt.show()

# Create the main window for the GUI.
window = tk.Tk() 
#Setting the title and size of the window.
window.title("Group Visualization: Cost Savings")
# Setting the size of the window.
window.geometry("400x200") 

# Creating a label to introduce the pie chart
btn = ttk.Button(window, text="Click here to Show Pie Chart", command=show_pie_chart)
# Adding some padding around the button
btn.pack(pady=60) 

# Rendering the GUI window and waiting for user interaction.
window.mainloop()
# The code ends here, and the GUI will remian open until the user closes it. 
# The pie chart will be displayed when the button is clicked. 
# The pie chart will show the proportion of total cost savings by energy sources.
# The chart will be displayed using matplotlib, and the GUI is created using tinker.
