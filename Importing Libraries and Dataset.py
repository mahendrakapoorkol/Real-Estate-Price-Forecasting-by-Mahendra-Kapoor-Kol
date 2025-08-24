import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_excel("HousePricePrediction.xlsx")

# Show first 5 rows
print(data.iloc[:5])
