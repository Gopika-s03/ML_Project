import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Rahul", "Priya", None],
    "Age": [21, 22, None, 22, 20],
    "Marks": [85, 90, 78, 90, None],
    "City": ["Chennai", "Madurai", "Coimbatore", "Madurai", "Salem"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())

df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.drop_duplicates()

print("\nDataset Statistics:")
print(df.describe())

print("\nCleaned Dataset:\n")
print(df)

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_dataset.csv'")
