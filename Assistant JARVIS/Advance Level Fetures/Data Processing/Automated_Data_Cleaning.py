import pandas as pd
import numpy as np
import logging
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport

# Set up logging
logging.basicConfig(filename='data_cleaning.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class AutomatedDataCleaning:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        logging.info("Loaded data from %s", file_path)

    def profile_data(self):
        """Generate a summary of the dataset and save profiling report."""
        logging.info("Data profiling before cleaning.")
        profile = ProfileReport(self.df, title="Pandas Profiling Report", explorative=True)
        profile.to_file("data_profiling_report.html")
        print("Data profiling report saved as data_profiling_report.html")
    
    def visualize_missing_data(self):
        """Visualize missing data."""
        plt.figure(figsize=(10, 5))
        sns.heatmap(self.df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Heatmap')
        plt.show()

    def remove_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        initial_shape = self.df.shape
        self.df.drop_duplicates(inplace=True)
        logging.info("Removed duplicates: %d -> %d rows", initial_shape[0], self.df.shape[0])
        print(f"Removed duplicates: {initial_shape[0]} -> {self.df.shape[0]} rows")

    def handle_missing_values(self, method='drop'):
        """Handle missing values in the DataFrame."""
        missing_values = self.df.isnull().sum()
        logging.info("Missing values before handling:\n%s", missing_values[missing_values > 0])

        if method == 'drop':
            self.df.dropna(inplace=True)
            logging.info("Dropped rows with missing values.")
            print("Dropped rows with missing values.")
        elif method in ['mean', 'median', 'mode']:
            for column in self.df.columns:
                if self.df[column].isnull().any():
                    if self.df[column].dtype == 'object':
                        self.df[column].fillna(self.df[column].mode()[0], inplace=True)
                    else:
                        self.df[column].fillna(self.df[column].mean() if method == 'mean' else self.df[column].median(), inplace=True)
                    logging.info("Filled missing values in %s with %s", column, method)
            print(f"Filled missing values using {method} method.")
        else:
            print("Invalid method for handling missing values.")

    def convert_data_types(self):
        """Convert data types of columns."""
        for column in self.df.columns:
            if self.df[column].dtype == 'object':
                try:
                    self.df[column] = pd.to_numeric(self.df[column], errors='ignore')
                except ValueError:
                    pass  # Not convertible, ignore
        logging.info("Data types after conversion:\n%s", self.df.dtypes)
        print("Data types after conversion:\n", self.df.dtypes)

    def standardize_text_data(self):
        """Standardize text data to lowercase."""
        for column in self.df.select_dtypes(include=['object']).columns:
            self.df[column] = self.df[column].str.lower().str.strip()
        logging.info("Text data standardized to lowercase and stripped whitespace.")
        print("Text data standardized to lowercase and stripped whitespace.")

    def remove_outliers(self, method='zscore'):
        """Remove outliers using specified method."""
        if method == 'zscore':
            numerical_columns = self.df.select_dtypes(include=[np.number]).columns
            for column in numerical_columns:
                z_scores = (self.df[column] - self.df[column].mean()) / self.df[column].std()
                self.df = self.df[(z_scores > -3) & (z_scores < 3)]
                logging.info("Removed outliers from %s using Z-score method.", column)
                print(f"Removed outliers from {column} using Z-score method.")
        elif method == 'iqr':
            numerical_columns = self.df.select_dtypes(include=[np.number]).columns
            for column in numerical_columns:
                Q1 = self.df[column].quantile(0.25)
                Q3 = self.df[column].quantile(0.75)
                IQR = Q3 - Q1
                self.df = self.df[(self.df[column] >= (Q1 - 1.5 * IQR)) & (self.df[column] <= (Q3 + 1.5 * IQR))]
                logging.info("Removed outliers from %s using IQR method.", column)
                print(f"Removed outliers from {column} using IQR method.")
        elif method == 'winsorize':
            from scipy.stats import mstats
            numerical_columns = self.df.select_dtypes(include=[np.number]).columns
            for column in numerical_columns:
                self.df[column] = mstats.winsorize(self.df[column], limits=[0.05, 0.05])
                logging.info("Winsorized outliers from %s.", column)
                print(f"Winsorized outliers from {column}.")

    def encode_categorical(self, method='onehot'):
        """Encode categorical variables."""
        if method == 'onehot':
            self.df = pd.get_dummies(self.df, drop_first=True)
            logging.info("Encoded categorical variables using one-hot encoding.")
            print("Encoded categorical variables using one-hot encoding.")
        elif method == 'label':
            from sklearn.preprocessing import LabelEncoder
            for column in self.df.select_dtypes(include=['object']).columns:
                le = LabelEncoder()
                self.df[column] = le.fit_transform(self.df[column])
            logging.info("Encoded categorical variables using label encoding.")
            print("Encoded categorical variables using label encoding.")
        else:
            print("Invalid encoding method.")

    def save_cleaned_data(self, output_file_path):
        """Save the cleaned DataFrame to a new CSV file."""
        self.df.to_csv(output_file_path, index=False)
        logging.info("Cleaned data saved to %s", output_file_path)
        print(f"Cleaned data saved to {output_file_path}")

    def send_notification(self, recipient_email):
        """Send a notification email after cleaning is complete."""
        msg = MIMEText("Data cleaning process is complete. The cleaned data is ready.")
        msg['Subject'] = 'Data Cleaning Notification'
        msg['From'] = 'your_email@example.com'
        msg['To'] = recipient_email
        
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
            logging.info("Notification sent to %s", recipient_email)
            print(f"Notification sent to {recipient_email}")

if __name__ == "__main__":
    file_path = input("Enter the path of the CSV file to clean: ")
    output_file_path = input("Enter the path to save the cleaned CSV file: ")
    
    cleaner = AutomatedDataCleaning(file_path)
    cleaner.profile_data()
    cleaner.visualize_missing_data()
    cleaner.remove_duplicates()
    
    method = input("Choose method to handle missing values (drop/mean/median/mode): ")
    cleaner.handle_missing_values(method)
    
    cleaner.convert_data_types()
    cleaner.standardize_text_data()
    
    outlier_method = input("Choose method to remove outliers (zscore/iqr/winsorize): ")
    cleaner.remove_outliers(outlier_method)
    
    encoding_method = input("Choose encoding method for categorical variables (onehot/label): ")
    cleaner.encode_categorical(encoding_method)
    
    cleaner.save_cleaned_data(output_file_path)

    # Email notification
    notify = input("Do you want to send an email notification? (yes/no): ")
    if notify.lower() == 'yes':
        recipient_email = input("Enter the recipient email: ")
        cleaner.send_notification(recipient_email)
