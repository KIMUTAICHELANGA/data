import pandas as pd

# Load the CSV file
df = pd.read_csv("orcid.csv")

# Drop rows where 'Firstname' and 'Lastname' are both empty
df_cleaned = df.dropna(subset=['Firstname', 'Lastname'], how='all')

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv("orcid_cleaned.csv", index=False)

print("Data cleaned and saved as 'orcid_cleaned.csv'.")
