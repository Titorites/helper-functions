import matplotlib.pyplot as plt
import mglearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def plot_linreg_package(X, y, lr):
    plt.plot(X, y, "o")
    xline = np.linspace(min(X), max(X), 100)
    slope = lr.coef_[0]
    intercept = lr.intercept_
    y_fit = intercept + slope * xline
    plt.plot(xline, y_fit, "--")
    plt.show()


def train_linreg_package():
    """Load data, split into train and test sets, and train a Linear Regression model."""
    X, y = mglearn.datasets.make_wave(n_samples=60)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    lr = LinearRegression().fit(X_train, y_train)
    return X, y, lr
