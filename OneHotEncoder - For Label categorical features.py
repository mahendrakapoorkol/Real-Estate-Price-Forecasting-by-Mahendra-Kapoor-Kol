from sklearn.preprocessing import OneHotEncoder

# Identify categorical columns
cat_cols = new_dataset.select_dtypes(include='object').columns
print("Categorical variables:", list(cat_cols))
print("No. of categorical features:", len(cat_cols))

# Apply OneHotEncoding
encoder = OneHotEncoder(drop=None, sparse_output=False, handle_unknown='ignore')
encoded = pd.DataFrame(encoder.fit_transform(new_dataset[cat_cols]),
                       index=new_dataset.index,
                       columns=encoder.get_feature_names_out(cat_cols))

# Merge encoded columns with numerical ones
final_df = pd.concat([new_dataset.drop(columns=cat_cols), encoded], axis=1)
