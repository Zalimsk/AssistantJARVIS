import pandas as pd
import numpy as np
import logging
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

# Set up logging
logging.basicConfig(filename='data_sampling.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataSampler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.df = None

    def load_data(self):
        """Load data from a CSV file."""
        try:
            self.df = pd.read_csv(self.input_file)
            logging.info("Successfully loaded data from %s", self.input_file)
        except Exception as e:
            logging.error("Error loading data from %s: %s", self.input_file, e)
            raise

    def random_sample(self, sample_size, replace=False):
        """Get a random sample of the data."""
        if sample_size > len(self.df):
            logging.warning("Sample size %d exceeds the total number of records %d. Adjusting to %d.", sample_size, len(self.df), len(self.df))
            sample_size = len(self.df)

        sample = self.df.sample(n=sample_size, replace=replace)
        logging.info("Random sample of size %d obtained (replace=%s).", sample_size, replace)
        return sample

    def stratified_sample(self, sample_sizes, stratify_column):
        """Get a stratified random sample of the data."""
        if stratify_column not in self.df.columns:
            logging.error("Stratify column '%s' not found in the data.", stratify_column)
            raise ValueError(f"Stratify column '{stratify_column}' not found in the data.")

        stratified_samples = []
        for category, size in sample_sizes.items():
            category_data = self.df[self.df[stratify_column] == category]
            sample_size = min(size, len(category_data))
            stratified_samples.append(category_data.sample(n=sample_size, replace=False))

        return pd.concat(stratified_samples).reset_index(drop=True)

    def systematic_sample(self, k):
        """Get a systematic sample of the data."""
        sample_indices = np.arange(0, len(self.df), k)
        sample = self.df.iloc[sample_indices]
        logging.info("Systematic sample obtained with step size %d.", k)
        return sample

    def export_sample(self, sample, output_file):
        """Export the sampled data to a CSV file."""
        try:
            sample.to_csv(output_file, index=False)
            logging.info("Successfully exported sampled data to %s", output_file)
        except Exception as e:
            logging.error("Error exporting sampled data to %s: %s", output_file, e)
            raise

    def summary_statistics(self, sample):
        """Print summary statistics of the original and sampled datasets."""
        original_stats = self.df.describe(include='all')
        sampled_stats = sample.describe(include='all')
        logging.info("Original data summary:\n%s", original_stats)
        logging.info("Sampled data summary:\n%s", sampled_stats)
        print("Original Data Summary:\n", original_stats)
        print("Sampled Data Summary:\n", sampled_stats)

    def visualize_distributions(self, sample, output_file):
        """Visualize distributions of the original and sampled datasets."""
        plt.figure(figsize=(12, 6))

        # Plot original data
        plt.subplot(1, 2, 1)
        sns.histplot(self.df, kde=True)
        plt.title('Original Data Distribution')
        plt.xlabel('Values')
        plt.ylabel('Frequency')

        # Plot sampled data
        plt.subplot(1, 2, 2)
        sns.histplot(sample, kde=True)
        plt.title('Sampled Data Distribution')
        plt.xlabel('Values')
        plt.ylabel('Frequency')

        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()
        logging.info("Distribution visualizations saved to %s", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform data sampling on a CSV file.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('--sample_size', type=int, default=100, help='Size of the random sample to take')
    parser.add_argument('--replace', action='store_true', help='Whether to sample with replacement')
    parser.add_argument('--stratify', type=str, help='Column name for stratified sampling')
    parser.add_argument('--stratified_sizes', type=str, help='JSON string for sample sizes by category')
    parser.add_argument('--systematic_k', type=int, help='Step size for systematic sampling')
    parser.add_argument('--output_file', type=str, help='Path to the output CSV file for the sampled data')
    parser.add_argument('--summary', action='store_true', help='Print summary statistics')
    parser.add_argument('--visualize', type=str, help='Path to save distribution visualizations')

    args = parser.parse_args()

    sampler = DataSampler(args.input_file)

    # Load data
    sampler.load_data()

    # Determine the sample method to use
    if args.stratify:
        import json
        stratified_sizes = json.loads(args.stratified_sizes)
        sample = sampler.stratified_sample(stratified_sizes, args.stratify)
    elif args.systematic_k:
        sample = sampler.systematic_sample(args.systematic_k)
    else:
        sample = sampler.random_sample(args.sample_size, replace=args.replace)

    # Export the sampled data
    if args.output_file:
        sampler.export_sample(sample, args.output_file)

    # Print summary statistics if requested
    if args.summary:
        sampler.summary_statistics(sample)

    # Visualize distributions if requested
    if args.visualize:
        sampler.visualize_distributions(sample, args.visualize)

    print(f"Sampled data exported to {args.output_file} successfully.")
