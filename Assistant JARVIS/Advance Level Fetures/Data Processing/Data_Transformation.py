import pandas as pd
import numpy as np
import logging
import argparse
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression

# Set up logging
logging.basicConfig(filename='data_transformation.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataTransformer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.df = None

    def load_data(self):
        """Load data from a CSV file."""
        try:
            self.df = pd.read_csv(self.input_file)
            logging.info("Successfully loaded data from %s", self.input_file)
        except Exception as e:
            logging.error("Error loading data from %s: %s", self.input_file, e)
            raise

    def impute_missing_values(self, strategy='mean'):
        """Impute missing values using specified strategy."""
        imputer = SimpleImputer(strategy=strategy)
        self.df[:] = imputer.fit_transform(self.df)
        logging.info("Imputed missing values using %s strategy", strategy)

    def scale_data(self, features, method='standard'):
        """Scale numerical features using the specified method."""
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        else:
            raise ValueError("Unsupported scaling method. Use 'standard' or 'minmax'.")

        self.df[features] = scaler.fit_transform(self.df[features])
        logging.info("Scaled features: %s using %s method", features, method)

    def encode_categorical(self, categorical_features):
        """Encode categorical features using one-hot encoding."""
        encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_features = encoder.fit_transform(self.df[categorical_features])
        
        # Create a DataFrame with the encoded features
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))
        
        # Drop original categorical columns and concatenate the new encoded columns
        self.df = pd.concat([self.df.drop(categorical_features, axis=1), encoded_df], axis=1)
        logging.info("Encoded categorical features: %s", categorical_features)

    def feature_engineering(self):
        """Example of feature engineering (create new features)."""
        if 'date' in self.df.columns:
            self.df['year'] = pd.to_datetime(self.df['date']).dt.year
            self.df['month'] = pd.to_datetime(self.df['date']).dt.month
            logging.info("Created year and month features from 'date' column.")

    def feature_selection(self, target_variable, num_features):
        """Select top k features based on correlation with the target variable."""
        X = self.df.drop(columns=[target_variable])
        y = self.df[target_variable]
        selector = SelectKBest(score_func=f_regression, k=num_features)
        selector.fit(X, y)
        selected_features = X.columns[selector.get_support()]
        self.df = self.df[selected_features.tolist() + [target_variable]]
        logging.info("Selected top %d features based on correlation with %s", num_features, target_variable)

    def export_data(self):
        """Export the transformed data to a CSV file."""
        try:
            self.df.to_csv(self.output_file, index=False)
            logging.info("Successfully exported transformed data to %s", self.output_file)
        except Exception as e:
            logging.error("Error exporting data to %s: %s", self.output_file, e)
            raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform data transformations on a CSV file.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    parser.add_argument('--scale', type=str, choices=['standard', 'minmax'], default='standard', 
                        help='Scaling method for numerical features')
    parser.add_argument('--categorical_features', type=str, nargs='+', help='List of categorical features to encode')
    parser.add_argument('--numerical_features', type=str, nargs='+', help='List of numerical features to scale')
    parser.add_argument('--impute', type=str, choices=['mean', 'median', 'most_frequent'], default='mean',
                        help='Imputation strategy for missing values')
    parser.add_argument('--target_variable', type=str, help='Target variable for feature selection')
    parser.add_argument('--num_features', type=int, default=5, help='Number of top features to select based on correlation')

    args = parser.parse_args()

    transformer = DataTransformer(args.input_file, args.output_file)
    
    # Load data
    transformer.load_data()
    
    # Impute missing values
    transformer.impute_missing_values(strategy=args.impute)
    
    # Scale numerical features
    if args.numerical_features:
        transformer.scale_data(args.numerical_features, method=args.scale)
    
    # Encode categorical features
    if args.categorical_features:
        transformer.encode_categorical(args.categorical_features)
    
    # Feature engineering
    transformer.feature_engineering()
    
    # Feature selection
    if args.target_variable:
        transformer.feature_selection(target_variable=args.target_variable, num_features=args.num_features)
    
    # Export the transformed data
    transformer.export_data()

    print(f"Data transformed and exported to {args.output_file} successfully.")
