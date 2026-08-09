import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/GOPIKA/Desktop/student_scores.csv")

print("Student dataset loaded successfully")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumns in Dataset:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())
