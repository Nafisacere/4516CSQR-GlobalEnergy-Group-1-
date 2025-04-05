import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = r"C:\Users\Nadir\Documents\GitHub\4516CSQR-GlobalEnergy-Group-1-\Cleaned_Renewable_Energy_Usage_Sampled.csv"
print(f"Attempting to load file from: {file_path}")
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Debug: Print column names
print("Columns in dataset:", data.columns)

# Check if dataset is empty
if data.empty:
    print("The dataset is empty.")
    exit()

#First visualization: Effect of Government Subsidies on Cost Savings
# Check if required columns exist
if 'Subsidy_Received' in data.columns and 'Cost_Savings_USD' in data.columns:
    # Ensure correct data types
    data['Subsidy_Received'] = data['Subsidy_Received'].astype(str)
    
    # Debug: Print first few rows
    print(data.head())
    
    # Calculate average cost savings for each subsidy group
    avg_cost_savings = data.groupby('Subsidy_Received')['Cost_Savings_USD'].mean()
    print("Average cost savings by subsidy group:", avg_cost_savings)
    
    # Create a bar chart with lilac and pink colors
    plt.figure(figsize=(8, 6))
    bars = avg_cost_savings.plot(kind='bar', color=['#ddd1ff', '#ffd1f3'], edgecolor='black')  # Lilac and Pink
    
    # Add labels on top of each bar
    for i, value in enumerate(avg_cost_savings):
        plt.text(i, value + 5, f'{value:.2f}', ha='center', va='bottom', fontsize=10, color='black')
    
    # Customize the chart
    plt.title('Effect of Government Subsidies on Cost Savings')
    plt.xlabel('Subsidy Received (Yes/No)')
    plt.ylabel('Average Cost Savings (USD)')
    plt.xticks(rotation=0)
    plt.tight_layout()  # Ensure proper layout
    plt.show()
else:
    print("Required columns 'Subsidy_Received' and 'Cost_Savings_USD' are missing in the dataset.")
    
# Second visualization: Trend of Average Cost Savings Over the Years
# Check if required columns exist for the second visualization
if 'Year' in data.columns and 'Cost_Savings_USD' in data.columns:
    # Calculate average cost savings for each year
    avg_cost_savings_by_year = data.groupby('Year')['Cost_Savings_USD'].mean()
    print("Average cost savings by year:", avg_cost_savings_by_year)
    
    # Create a line plot
    plt.figure(figsize=(10, 6))
    avg_cost_savings_by_year.plot(kind='line', marker='o', color='#b5a2c8', linewidth=2)
    
    # Customize the chart
    plt.title('Trend of Average Cost Savings Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Average Cost Savings (USD)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()  # Ensure proper layout
    plt.show()
else:
    print("Required columns 'Year' and 'Cost_Savings_USD' are missing in the dataset.")