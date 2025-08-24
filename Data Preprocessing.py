# Categorical columns
cat_cols = dataset.select_dtypes(include='object').columns
print("Categorical variables:", len(cat_cols))

# Integer columns
int_cols = dataset.select_dtypes(include='int').columns
print("Integer variables:", len(int_cols))

# Float columns
float_cols = dataset.select_dtypes(include='float').columns
print("Float variables:", len(float_cols))
