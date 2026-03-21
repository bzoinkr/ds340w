import pandas as pd
from sklearn.model_selection import train_test_split

# Load CDC PLACES dataset (County level 2024/2025 release example via Socrata API)
# Replace URL with Place, Tract, or ZCTA endpoints as needed.
url = "https://data.cdc.gov/resource/swc5-untb.csv?$limit=5000" 
df = pd.read_csv(url)

# Define features (X) and target variable (y) based on your specific objective
# X = df.drop(columns=['your_target_column'])
# y = df['your_target_column']

# First split: 70% Train, 30% Temporary (to be split into Val/Test)
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42)

# Second split: Divide the temporary 30% equally into 15% Validation and 15% Test
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42)

print(f"Total rows: {len(df)}")
print(f"Train rows: {len(train_df)}")
print(f"Validation rows: {len(val_df)}")
print(f"Test rows: {len(test_df)}")

# Save splits to CSV
train_df.to_csv("train.csv", index=False)
val_df.to_csv("validate.csv", index=False)
test_df.to_csv("test.csv", index=False)

print("\nSaved train.csv, validate.csv, test.csv")
