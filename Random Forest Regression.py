from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error

def train_rf(X_train, y_train, X_test, y_test, trees=10):
    model = RandomForestRegressor(n_estimators=trees, random_state=1)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return mean_absolute_percentage_error(y_test, preds)

mape_score = train_rf(X_train, Y_train, X_valid, Y_valid)
print("MAPE:", mape_score)
