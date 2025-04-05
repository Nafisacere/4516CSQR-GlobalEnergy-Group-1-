import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

# use file path to read the CLEANED dataset from my file
file_path = "Cleaned_Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path)

# This is used to make the boxplot more visually appealing and also using the colors that I like
energy_sources = data['Energy_Source'].unique()
pie_colors = plt.cm.Pastel1.colors
color_map = dict(zip(energy_sources, pie_colors))

#----------------------------------------------------------------------------------------------------------------------------------------------
# FIRST QUESTION: ENERGY TYPE VS COST SAVINGS(BOXPLOT)
def show_box_plot():
    fig, ax = plt.subplots(figsize=(9, 6))
    box_data = [data[data['Energy_Source'] == source]['Cost_Savings_USD'] for source in energy_sources]
    boxplot = ax.boxplot(box_data, patch_artist=True,
                         boxprops=dict(color='black'),
                         medianprops=dict(color='darkred', linewidth=1.5),
                         whiskerprops=dict(color='black'),
                         capprops=dict(color='black'),
                         flierprops=dict(marker='o', markerfacecolor='gray', markersize=6, linestyle='none'))
    for patch, source in zip(boxplot['boxes'], energy_sources):
        patch.set_facecolor(color_map[source])
    ax.set_title("Cost Savings Distribution by Energy Source")
    ax.set_xlabel("Energy Source")
    ax.set_ylabel("Cost Savings (USD)")
    ax.set_xticks(range(1, len(energy_sources) + 1))
    ax.set_xticklabels(energy_sources, rotation=30, ha='right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


#--------------------------------------------------------------------------------------------------------------------------------------------------
# SECOND QUESTION: ENERGY SOURCE DISTRIBUTION (PIE CHART)
def show_pie_chart():
    energy_counts = data['Energy_Source'].value_counts()
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(energy_counts, labels=energy_counts.index, autopct='%1.1f%%', startangle=140,
           colors=[color_map[source] for source in energy_counts.index], wedgeprops={'edgecolor': 'black'})
    ax.set_title("Distribution of Energy Sources Used by Households")
    plt.tight_layout()
    plt.show()


#-----------------------------------------------------------------------------------------------------------------------------------------------------
# THIRD QUESTION: AVERAGE MONTHLY ENERGY USAGE BY HOUSEHOLD SIZE (BAR CHART)
def show_bar_chart():
    avg_usage = data.groupby('Household_Size')['Monthly_Usage_kWh'].mean()
    bar_colors = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF', '#A0C4FF', '#BDB2FF', '#FFC6FF']
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(avg_usage.index, avg_usage.values, color=bar_colors[:len(avg_usage)], edgecolor='black')
    ax.set_title('Average Monthly Energy Usage by Household Size')
    ax.set_xlabel('Household Size')
    ax.set_ylabel('Average Monthly Energy Usage (kWh)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Create Tkinter window
window = tk.Tk()
window.title("DATASET VISUALIZATION: Cost Savings, Usage, and Household Analysis")
window.geometry("400x300")

# Add buttons to display individual graphs
btn1 = ttk.Button(window, text="1.ENERGY TYPE VS COST SAVINGS(BOXPLOT)", command=show_box_plot)
btn1.pack(pady=10)

btn2 = ttk.Button(window, text="2.ENERGY SOURCE DISTRIBUTION (PIE CHART)", command=show_pie_chart)
btn2.pack(pady=10)

btn3 = ttk.Button(window, text="3.AVERAGE MONTHLY ENERGY USAGE BY HOUSEHOLD SIZE (BAR CHART)", command=show_bar_chart)
btn3.pack(pady=10)

# Run the Tkinter loop
window.mainloop()
