import pandas as pd
import os
import numpy as np
import logging
import argparse
from pandas_profiling import ProfileReport
from scipy import stats
import time

# Set up logging
logging.basicConfig(filename='batch_processing.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class BatchDataProcessing:
    def __init__(self, input_dir, output_dir, missing_value_method='mean', outlier_method='zscore'):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.missing_value_method = missing_value_method
        self.outlier_method = outlier_method
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info("Output directory created at %s", output_dir)

    def profile_data(self, df, file_path):
        """Generate a profiling report and save it."""
        profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
        profile_file_path = os.path.join(self.output_dir, f"profile_{os.path.basename(file_path)}.html")
        profile.to_file(profile_file_path)
        logging.info("Profiling report saved for %s as %s", file_path, profile_file_path)

    def handle_missing_values(self, df):
        """Handle missing values in the DataFrame."""
        for column in df.columns:
            if df[column].isnull().any():
                if self.missing_value_method == 'drop':
                    df.dropna(subset=[column], inplace=True)
                    logging.info("Dropped rows with missing values in %s", column)
                elif self.missing_value_method == 'mean':
                    if df[column].dtype in ['int64', 'float64']:
                        df[column].fillna(df[column].mean(), inplace=True)
                        logging.info("Filled missing values in %s with mean", column)
                elif self.missing_value_method == 'median':
                    if df[column].dtype in ['int64', 'float64']:
                        df[column].fillna(df[column].median(), inplace=True)
                        logging.info("Filled missing values in %s with median", column)
                elif self.missing_value_method == 'mode':
                    df[column].fillna(df[column].mode()[0], inplace=True)
                    logging.info("Filled missing values in %s with mode", column)

    def remove_outliers(self, df):
        """Remove outliers using the specified method."""
        numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
        for column in numerical_columns:
            if self.outlier_method == 'zscore':
                z_scores = np.abs(stats.zscore(df[column].dropna()))
                df = df[(z_scores < 3)]
                logging.info("Removed outliers from %s using Z-score method", column)
            elif self.outlier_method == 'iqr':
                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)
                IQR = Q3 - Q1
                df = df[(df[column] >= (Q1 - 1.5 * IQR)) & (df[column] <= (Q3 + 1.5 * IQR))]
                logging.info("Removed outliers from %s using IQR method", column)
        return df

    def process_file(self, file_path):
        """Clean a single file and save the cleaned version."""
        try:
            df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
            logging.info("Loaded data from %s", file_path)
            self.profile_data(df, file_path)

            # Remove duplicates
            initial_shape = df.shape
            df.drop_duplicates(inplace=True)
            logging.info("Removed duplicates from %s: %d -> %d rows", file_path, initial_shape[0], df.shape[0])

            # Handle missing values
            self.handle_missing_values(df)

            # Remove outliers
            df = self.remove_outliers(df)

            # Save the cleaned DataFrame
            output_file_path = os.path.join(self.output_dir, os.path.basename(file_path))
            df.to_csv(output_file_path, index=False)
            logging.info("Cleaned data saved to %s", output_file_path)

        except Exception as e:
            logging.error("Error processing %s: %s", file_path, e)

    def process_all_files(self):
        """Process all CSV files in the input directory."""
        files = [f for f in os.listdir(self.input_dir) if f.endswith('.csv') or f.endswith('.xlsx')]
        total_files = len(files)
        
        if total_files == 0:
            logging.warning("No CSV or Excel files found in %s", self.input_dir)
            return

        for i, file in enumerate(files):
            file_path = os.path.join(self.input_dir, file)
            logging.info("Processing file %d of %d: %s", i + 1, total_files, file)
            self.process_file(file_path)
            print(f"Processed {i + 1} of {total_files} files.")
            time.sleep(1)  # Simulate processing time for each file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Batch process CSV and Excel files for data cleaning.')
    parser.add_argument('input_dir', type=str, help='Directory containing the files to clean')
    parser.add_argument('output_dir', type=str, help='Directory to save the cleaned files')
    parser.add_argument('--missing_value_method', type=str, default='mean', 
                        choices=['drop', 'mean', 'median', 'mode'], help='Method to handle missing values')
    parser.add_argument('--outlier_method', type=str, default='zscore', 
                        choices=['zscore', 'iqr'], help='Method to handle outliers')
    
    args = parser.parse_args()

    batch_processor = BatchDataProcessing(args.input_dir, args.output_dir, 
                                          missing_value_method=args.missing_value_method, 
                                          outlier_method=args.outlier_method)
    batch_processor.process_all_files()
