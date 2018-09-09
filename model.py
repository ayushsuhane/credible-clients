import numpy as np
from sklearn.ensemble import RandomForestRegressor


class CreditModel:
    def __init__(self):
        """
        Instantiates the model object, creating class variables if needed.
        """

        # TODO: Initialize your model object.
        self.predictor = RandomForestRegressor(n_estimators = 10, random_state = 42)

    def fit(self, X_train, y_train):
        """
        Fits the model based on the given `X_train` and `y_train`.

        You should somehow manipulate and store this data to your model class
        so that you can make predictions on new testing data later on.
        """

        # TODO: Fit your model based on the given X and y.

        self.predictor.fit(X=X_train, y=y_train)

    def predict(self, X_test):
        """
        Returns `y_hat`, a prediction for a given `X_test` after fitting.

        You should make use of the data that you stored/computed in the
        fitting phase to make your prediction on this new testing data.
        """

        # TODO: Predict on `X_test` based on what you learned in the fit phase.
        outcome = self.predictor.predict(X=X_test)
        return outcome
