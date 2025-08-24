from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_percentage_error

def train_and_evaluate(X_tr, y_tr, X_val, y_val):
    model = SVR()
    model.fit(X_tr, y_tr)
    y_hat = model.predict(X_val)
    return mean_absolute_percentage_error(y_val, y_hat)

mape_score = train_and_evaluate(X_train, Y_train, X_valid, Y_valid)
print("Mean Absolute Percentage Error:", mape_score)
