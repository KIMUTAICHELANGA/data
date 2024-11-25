import pandas as pd

# Load the CSV file
df = pd.read_csv("aphrc.csv")

# Select only the desired columns
df_filtered = df[['Firstname', 'Lastname', 'Contact Details']]

# Save the updated DataFrame back to the same CSV file
df_filtered.to_csv("aphrc.csv", index=False)

print("Columns successfully removed. Updated file saved as 'aphrc.csv'.")
