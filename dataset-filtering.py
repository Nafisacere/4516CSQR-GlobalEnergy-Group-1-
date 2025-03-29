import pandas as pd

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)  
pd.set_option('display.max_colwidth', None)  

file_path = r"C:\Users\menac\OneDrive\Desktop\csws\4516CSQR-GlobalEnergy-Group-1-\Renewable_Energy_Usage_Sampled.csv"
data = pd.read_csv(file_path)

print("Step 2: Check the data types of each column")
print(data.dtypes)

print("\nStep 3: Remove the 'Country' column")
data = data.drop(columns=["Country"])
print("'Country' column removed!")

print("\nStep 4: Fill missing values with zero")
data = data.fillna(0)
print("Missing values filled with zero!")

print("\nStep 5: Check for duplicate rows")
duplicate_rows = data[data.duplicated()]
if duplicate_rows.empty:
    print("No duplicate rows found!")
else:
    print("Duplicate rows found:")
    print(duplicate_rows)

data.reset_index(drop=True, inplace=True)  
data.index = data.index + 1  

print("\nStep 7: Display the cleaned dataset (row numbers start from 1)")
print(data.to_string(index=False)) 

output_file_path = r"C:\Users\menac\OneDrive\Desktop\csws\4516CSQR-GlobalEnergy-Group-1-\Cleaned_Renewable_Energy_Usage_Sampled.csv"
data.to_csv(output_file_path, index=False)
print(f"\nCleaned dataset saved to '{output_file_path}'")