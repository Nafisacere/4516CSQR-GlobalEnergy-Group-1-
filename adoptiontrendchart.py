import pandas as pd 
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\xyzst\Documents\GitHub\4516CSQR-GlobalEnergy-Group-1-\Cleaned_Renewable_Energy_Usage_Sampled.csv")

# Prepare the data
yearly_adoption = df.groupby(['Adoption_Year', 'Energy_Source']).size().unstack()

# Create the visualization
plt.figure(figsize=(12, 6))

# Plot each energy source as a separate line
for source in yearly_adoption.columns:
    plt.plot(yearly_adoption.index,
             yearly_adoption[source],
             marker='o',
             label=source,
             linewidth=2)

# Customize the chart
plt.title('Renewable Energy Adoption Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Households Adopting', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

# Add legend and adjust layout
plt.legend(title=

'Energy Source', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

# Save and display
plt.savefig('renewable_adoption_trends.png', dpi=300, bbox_inches='tight')
plt.show()

# Print the raw data for reference
print("\nYearly Adoption Counts:")
print(yearly_adoption)