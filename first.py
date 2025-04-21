import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Initial Shape:", df.shape)
print(df.info())

df.drop_duplicates(inplace=True)

print("Missing Values:\n", df.isnull().sum())
df.dropna(inplace=True)

df.columns = df.columns.str.lower().str.replace(" ", "_")

df["dt_customer"] = pd.to_datetime(df["dt_customer"], format='%d-%m-%Y')

df["education"] = df["education"].str.strip().str.lower()
df["marital_status"] = df["marital_status"].str.strip().str.lower()

df["income"] = pd.to_numeric(df["income"], errors='coerce')
df["year_birth"] = pd.to_numeric(df["year_birth"], errors='coerce')

print(df.dtypes)

df.to_csv("cleaned_customer_data.csv", index=False)
print("Cleaning complete. Cleaned data saved to 'cleaned_customer_data.csv'")
