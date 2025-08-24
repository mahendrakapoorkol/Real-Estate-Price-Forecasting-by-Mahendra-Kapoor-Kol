# Remove Id column
cleaned_data = dataset.drop(columns=['Id'])

# Fill missing SalePrice with average value
cleaned_data['SalePrice'] = cleaned_data['SalePrice'].fillna(cleaned_data['SalePrice'].mean())

# Drop rows with other missing values
final_data = cleaned_data.dropna()

# Check missing values
print(final_data.isna().sum())
