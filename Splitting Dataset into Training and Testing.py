from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

features = df_final.drop(columns=['SalePrice'])
target = df_final['SalePrice']

X_train, X_valid, y_train, y_valid = train_test_split(
    features, target, test_size=0.2, train_size=0.8, random_state=42
)
