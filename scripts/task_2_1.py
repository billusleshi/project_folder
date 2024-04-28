import pandas as pd

# Load dataset
telecom_data = pd.read_csv('telecom_dataset.csv')
# Group by user ID
user_groups = telecom_data.groupby('MSISDN')

# Aggregate data
user_aggregated_data = user_groups.agg({
    'Bearer Id': 'count',  # Number of xDR sessions
    'Dur. (ms)': 'sum',   # Session duration
    'Total DL (Bytes)': 'sum',  # Total download data
    'Total UL (Bytes)': 'sum',  # Total upload data
    'Social Media DL (Bytes)': 'sum',  # Social Media data
    'Social Media UL (Bytes)': 'sum',
    'Google DL (Bytes)': 'sum',  # Google data
    'Google UL (Bytes)': 'sum',
    'Email DL (Bytes)': 'sum',   # Email data
    'Email UL (Bytes)': 'sum',
    'Youtube DL (Bytes)': 'sum',  # Youtube data
    'Youtube UL (Bytes)': 'sum',
    'Netflix DL (Bytes)': 'sum',  # Netflix data
    'Netflix UL (Bytes)': 'sum',
    'Gaming DL (Bytes)': 'sum',  # Gaming data
    'Gaming UL (Bytes)': 'sum',
    'Other DL (Bytes)': 'sum',   # Other data
    'Other UL (Bytes)': 'sum'
})
# Check for missing values
print(user_aggregated_data.isnull().sum())

# Handle missing values (if any)
user_aggregated_data.fillna(0, inplace=True)  # Replace missing values with 0

# Convert data types if necessary
# (e.g., convert duration from milliseconds to minutes)
user_aggregated_data['Dur. (ms)'] /= 60000  # Convert milliseconds to minutes
