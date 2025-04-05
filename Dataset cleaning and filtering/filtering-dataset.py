import pandas as pd

# use Pandas to display all rows and columns of the dataset
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)  
pd.set_option('display.max_colwidth', None)  

#1. read the CVS file using file path
file_path = r"C:\Users\bhjaa\OneDrive\Documents\GitHub\4516CSQR-GlobalEnergy-Group-1-\Dataset cleaning and filtering\Renewable_Energy_Usage_Sampled.csv"
data =pd.read_csv(file_path)

#2. Check the data types of each column and make sure they are the same throughot the dataset
print("2: Check the data types of each column")
print(data.dtypes)

#3. Remove the "Country" column as it wont be used in the visualization
print("\n3: Remove the 'Country' column")
data = data.drop(columns=["Country"])
print("'Country' column removed!")

#4. Fill missing values with zero so the code does not break
print("\n4: Fill missing values with zero")
data = data.fillna(0)
print("Completed!!! All missing values filled with zero!")

#5. Check for duplicate rows
print("\n5: Check for duplicate rows")
duplicate_rows = data[data.duplicated()]
if duplicate_rows.empty:
    print("No duplicate rows found!")
else:
    print("Duplicate rows found:")
    print(duplicate_rows)

#6. Reset the index to start from 1
data.reset_index(drop=True, inplace=True)  # Reset starting from 1 index and droping the old index
data.index = data.index + 1  # Start row numbers from 1 and keep adding one with every new line of data

#7. Display the cleaned dataset with row numbers starting from 1 
print("\n7: Display the cleaned dataset (row numbers start from 1)")
print(data.to_string(index=False))  

#8. Display the dataset info to check for missing values and data types
print("\n8: Dataset Info")
print(data.info())

#9. Display the dataset summary statistics
print("\n9: Dataset Summary Statistics")
print(data.describe(include='all'))


#Finally Save the cleaned dataset to a new CSV file
# Use the same directory path as the input file and append the new file name
output_file_path = r"C:\Users\bhjaa\OneDrive\Documents\GitHub\4516CSQR-GlobalEnergy-Group-1-\Dataset cleaning and filtering\Cleaned_Renewable_Energy_Usage_Sampled.csv"
data.to_csv(output_file_path, index=False)
print(f"\nCleaned dataset saved to '{output_file_path}'")