# Option 1: Using shape directly
print(dataset.shape)

# Option 2: Unpack rows and columns
rows, cols = dataset.shape
print("Rows:", rows, "Columns:", cols)

# Option 3: Use len() with columns
print("Rows:", len(dataset), "Columns:", len(dataset.columns))
