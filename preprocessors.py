import numpy as np
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin

class ImputeConstDatetime(BaseEstimator, TransformerMixin):
    def __init__(self, value, variables):

        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")

        self.value = value
        self.variables = variables

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.variables] = X[self.variables].fillna(pd.to_datetime(self.value, format = "%d-%b-%Y"))
        return X

class TimeDifference(BaseEstimator, TransformerMixin):

    def __init__(self, variables, reference_date):
        
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")

        self.variables = variables
        self.reference_date = reference_date

    def fit(self, X, y = None):
        return self 

    def transform(self, X):
        X = X.copy()
        date = pd.to_datetime(self.reference_date, format = "%d-%b-%Y")

        for feature in self.variables:
            X[feature] = (date - X[feature]).dt.days

        return X 