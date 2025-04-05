# question:How does the average monthly energy usage differ between Urban and Rural areas from 2010 to 2024?

import pandas as pd
import matplotlib.pyplot as plt

# load the data from csv
df = pd.read_csv (r"C:\Users\menac\OneDrive\Desktop\csws\4516CSQR-GlobalEnergy-Group-1-\Cleaned_Renewable_Energy_Usage_Sampled.csv")

#calculate average monthly usage grouped by year and area type
usage_by_year = df.groupby (['Year', 'Urban_Rural'] ) ['Monthly_Usage_kWh'].mean( ).unstack()

#make the graph
plt.figure (figsize= (12 , 6 ))

# plot line for urban
plt.plot(usage_by_year.index , usage_by_year ['Urban'], label= 'Urban',color='#3498db', marker='o')

# plot line for rural
plt.plot(usage_by_year.index, usage_by_year ['Rural'], label='Rural', color='#e74c3c', marker='s' )

# add chart labels and legend
plt.title ( 'Urban vs Rural Average Monthly Energy Usage (kWh) per Year', fontsize=14 )
plt.xlabel ('Year ', fontsize=12)
plt.ylabel ( 'Avg Monthly Usage (kWh)', fontsize=12 )
plt.legend( )
plt.grid (True, linestyle='--', alpha=0.3)
plt.xticks(usage_by_year.index)  # make sure all years are shown

#show the graph
plt.tight_layout()
plt.show()

