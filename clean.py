import pandas as pd

# Load Excel file
df = pd.read_csv('sample.csv')

# Function to handle mixed date formats
def parse_mixed_date(date_str):
    for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    return pd.NaT  # Not a Time if nothing matches

# Apply the function to the column
df['Ship_Date'] = df['Ship_Date'].apply(parse_mixed_date)

# Convert to desired format: dd-mm-yyyy
df['Ship_Date'] = df['Ship_Date'].dt.strftime('%d-%m-%Y')

# Save to new Excel file
df.to_csv('sample.csv', index=False)

print("Mixed format dates converted to dd-mm-yyyy successfully!")
