# Count unique values for categorical columns
unique_counts = {col: dataset[col].nunique() for col in object_cols}

plt.figure(figsize=(10, 6))
pd.Series(unique_counts).plot(kind="bar")
plt.title("Unique Values in Categorical Features")
plt.xticks(rotation=75)
plt.ylabel("Count")
plt.show()
