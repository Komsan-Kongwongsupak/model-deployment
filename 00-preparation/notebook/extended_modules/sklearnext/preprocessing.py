from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder

# Custom Transformer to use LabelEncoder within ColumnTransformer
class LabelEncoderTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoder = LabelEncoder()

    def fit(self, X, y=None):
        self.encoder.fit(X)  # Fit the LabelEncoder with the input data
        return self

    def transform(self, X):
        # Transform the data and reshape it to a 2D array to maintain consistency with sklearn transformers
        return self.encoder.transform(X).reshape(-1, 1)
