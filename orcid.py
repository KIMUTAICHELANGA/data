import pandas as pd
import requests

# Load the CSV file
df = pd.read_csv("aphrc.csv")

# Add new columns for ORCID and OpenAlex Author ID
df['ORCID'] = ''
df['OpenAlex_ID'] = ''

# Function to fetch ORCID and OpenAlex ID
def get_openalex_data(firstname, lastname):
    base_url = "https://api.openalex.org/authors"
    params = {
        "search": f"{firstname} {lastname}"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            # Assume the first result is the correct author
            author = results[0]
            orcid = author.get('orcid', '')
            openalex_id = author.get('id', '').split('/')[-1]  # Extract only the ID part
            return orcid, openalex_id
    return '', ''

# Loop through each row to fetch data
for index, row in df.iterrows():
    firstname = row['Firstname']
    lastname = row['Lastname']
    orcid, openalex_id = get_openalex_data(firstname, lastname)
    df.at[index, 'ORCID'] = orcid
    df.at[index, 'OpenAlex_ID'] = openalex_id

# Save the updated DataFrame as 'orcid.csv'
df.to_csv("orcid.csv", index=False)

print("Data updated and saved as 'orcid.csv'.")
