from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score 
from sklearn.metrics import explained_variance_score

# Prints standard regression error metrics given 
def print_regression_error_metrics(preds, y_test):
    print('MSE, MAE, R^2, EVS for feature set '+ str([mean_squared_error(y_test, preds),
                 median_absolute_error(y_test, preds),
                 r2_score(y_test, preds),
                 explained_variance_score(y_test, preds)]))