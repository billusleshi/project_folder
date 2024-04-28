import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sqlite3

# Connect to the SQL database
conn = sqlite3.connect('telecom_database.db')

# Load the telecom dataset from the SQL database
telecom_data = pd.read_sql_query('SELECT * FROM telecom_data_table', conn)

# Close the database connection
conn.close()

# Bivariate Analysis
bivariate_data = telecom_data[['Social Media DL', 'Social Media UL']]
plt.figure(figsize=(8, 6))
sns.scatterplot(data=bivariate_data, x='Social Media DL', y='Social Media UL')
plt.title('Relationship between Social Media Download and Upload Data')
plt.xlabel('Social Media Download Data (Bytes)')
plt.ylabel('Social Media Upload Data (Bytes)')
plt.show()

# Compute correlation coefficient
correlation_coefficient = bivariate_data.corr().iloc[0, 1]
print("Correlation Coefficient between Social Media Download and Upload Data:", correlation_coefficient)

# Variable Transformations
telecom_data['Session_Duration_Decile'] = pd.qcut(telecom_data['Dur. (ms)'], q=10, labels=False)
data_usage_per_decile = telecom_data.groupby('Session_Duration_Decile').agg({
    'Total DL (Bytes)': 'sum',
    'Total UL (Bytes)': 'sum'
})
print("\nTotal Data Usage per Decile Class:")
print(data_usage_per_decile)

# Correlation Analysis
correlation_variables = telecom_data[['Social Media DL', 'Google DL', 'Email DL', 'Youtube DL', 'Netflix DL', 'Gaming DL', 'Other DL']]
correlation_matrix = correlation_variables.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Dimensionality Reduction (Principal Component Analysis - PCA)
pca_variables = telecom_data[['Social Media DL', 'Google DL', 'Email DL', 'Youtube DL', 'Netflix DL', 'Gaming DL', 'Other DL']]
pca = PCA(n_components=2)
principal_components = pca.fit_transform(pca_variables)
explained_variance_ratio = pca.explained_variance_ratio_
print("\nExplained Variance Ratio (PC1, PC2):", explained_variance_ratio)
