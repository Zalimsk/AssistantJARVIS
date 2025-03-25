import pandas as pd
import os
import logging
import json
import argparse
import numpy as np

# Set up logging
logging.basicConfig(filename='data_import_export.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataImporterExporter:
    def __init__(self, input_file, output_file, overwrite=False):
        self.input_file = input_file
        self.output_file = output_file
        self.overwrite = overwrite

    def import_data(self):
        """Import data from various formats (CSV, Excel, JSON)."""
        try:
            if self.input_file.endswith('.csv'):
                df = pd.read_csv(self.input_file)
            elif self.input_file.endswith('.xlsx'):
                df = pd.read_excel(self.input_file)
            elif self.input_file.endswith('.json'):
                df = pd.read_json(self.input_file)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV, Excel, or JSON file.")

            logging.info("Successfully imported data from %s", self.input_file)
            return df

        except Exception as e:
            logging.error("Error importing data from %s: %s", self.input_file, e)
            raise

    def export_data(self, df):
        """Export data to various formats (CSV, Excel, JSON)."""
        try:
            if not self.overwrite and os.path.exists(self.output_file):
                raise FileExistsError(f"{self.output_file} already exists. Use --overwrite to allow overwriting.")

            if self.output_file.endswith('.csv'):
                df.to_csv(self.output_file, index=False)
            elif self.output_file.endswith('.xlsx'):
                df.to_excel(self.output_file, index=False)
            elif self.output_file.endswith('.json'):
                df.to_json(self.output_file, orient='records', lines=True)
            else:
                raise ValueError("Unsupported file format. Please provide a CSV, Excel, or JSON file.")
            
            logging.info("Successfully exported data to %s", self.output_file)

        except Exception as e:
            logging.error("Error exporting data to %s: %s", self.output_file, e)
            raise

    def validate_data(self, df):
        """Perform basic data validation checks."""
        if df.isnull().values.any():
            logging.warning("Data contains missing values.")
            print("Warning: Data contains missing values.")
        
        # Check for incorrect data types
        for column in df.select_dtypes(include=[np.object]):
            if df[column].apply(lambda x: isinstance(x, str)).any() == False:
                logging.warning(f"Column {column} contains non-string values.")
        
        logging.info("Data validation complete.")

    def transform_data(self, df):
        """Custom data transformation (example: normalize numeric columns)."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = (df[col] - df[col].mean()) / df[col].std()  # Standardization
            logging.info(f"Normalized column: {col}")
        return df

    def profile_data(self, df):
        """Generate a summary of the data."""
        summary = df.describe(include='all')
        logging.info("Data profile summary:\n%s", summary)
        print("Data profile summary:\n", summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import and export data in various formats with enhancements.')
    parser.add_argument('input_file', type=str, help='Path to the input file (CSV, Excel, or JSON)')
    parser.add_argument('output_file', type=str, help='Path to the output file (CSV, Excel, or JSON)')
    parser.add_argument('--overwrite', action='store_true', help='Allow overwriting of existing output files')
    
    args = parser.parse_args()

    data_processor = DataImporterExporter(args.input_file, args.output_file, overwrite=args.overwrite)

    # Import the data
    df = data_processor.import_data()
    
    # Validate the data
    data_processor.validate_data(df)
    
    # Transform the data
    df = data_processor.transform_data(df)
    
    # Profile the data
    data_processor.profile_data(df)
    
    # Export the data
    data_processor.export_data(df)

    print(f"Data imported from {args.input_file} and exported to {args.output_file} successfully.")
