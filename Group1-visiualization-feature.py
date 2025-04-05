
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = "C:/Users/EmanS/Documents/GitHub/4516CSQR-GlobalEnergy-Group-1-/Cleaned_Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path) 


aggregated_data = data.groupby("Energy_Source")["Cost_Savings_USD"].sum()


colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']


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


plt.title("Proportion of Total Cost Savings by Energy Source", fontsize=16, fontweight='bold')


plt.legend(wedges, aggregated_data.index, title="Energy Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)


plt.tight_layout()

plt.show()

