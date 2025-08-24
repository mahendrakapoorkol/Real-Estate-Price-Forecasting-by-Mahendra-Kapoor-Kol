from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

def evaluate_lr(X_tr, y_tr, X_val, y_val):
    model = LinearRegression().fit(X_tr, y_tr)
    preds = model.predict(X_val)
    return mean_absolute_percentage_error(y_val, preds)

mape_score = evaluate_lr(X_train, Y_train, X_valid, Y_valid)
print("Mean Absolute Percentage Error:", mape_score)
