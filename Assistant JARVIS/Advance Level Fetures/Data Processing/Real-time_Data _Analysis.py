import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class RealTimeDataAnalyzer:
    def __init__(self, num_streams=1, window_size=20):
        self.data = [[] for _ in range(num_streams)]
        self.window_size = window_size
        self.num_streams = num_streams
        self.csv_data = []

    def generate_data(self):
        """Generate random data for analysis."""
        return [random.uniform(1, 100) for _ in range(self.num_streams)]

    def update_data(self, new_values):
        """Update the data lists and maintain the window size."""
        for i, new_value in enumerate(new_values):
            self.data[i].append(new_value)
            if len(self.data[i]) > self.window_size:
                self.data[i].pop(0)  # Keep only the last `window_size` elements

    def analyze_data(self):
        """Perform statistical analysis on the data."""
        analysis_results = []
        for stream in self.data:
            if not stream:
                analysis_results.append((0, 0, 0, 0))
                continue
            mean_value = np.mean(stream)
            max_value = np.max(stream)
            min_value = np.min(stream)
            std_dev = np.std(stream)
            analysis_results.append((mean_value, max_value, min_value, std_dev))
        return analysis_results

    def plot_data(self):
        """Plot the real-time data for all streams."""
        plt.clf()  # Clear the current figure
        for i in range(self.num_streams):
            plt.plot(self.data[i], label=f'Stream {i + 1}')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Real-time Data Analysis')
        plt.legend()
        plt.pause(0.1)  # Pause to update the plot

    def log_data(self, new_values):
        """Log data to CSV."""
        self.csv_data.append(new_values)
        df = pd.DataFrame(self.csv_data, columns=[f'Stream {i + 1}' for i in range(self.num_streams)])
        df.to_csv('real_time_data_log.csv', index=False)

if __name__ == "__main__":
    num_streams = int(input("Enter number of data streams: "))
    window_size = int(input("Enter window size for analysis: "))
    update_frequency = float(input("Enter update frequency in seconds: "))

    analyzer = RealTimeDataAnalyzer(num_streams=num_streams, window_size=window_size)

    plt.ion()  # Enable interactive mode
    plt.figure(figsize=(10, 5))

    try:
        while True:
            new_data = analyzer.generate_data()
            analyzer.update_data(new_data)
            analysis_results = analyzer.analyze_data()  # Use this line

            for i in range(num_streams):
                mean, max_val, min_val, std_dev = analysis_results[i]  # Unpack values for each stream
                print(f"Stream {i + 1} - New Data: {new_data[i]:.2f} | "
                      f"Mean: {mean:.2f} | Max: {max_val:.2f} | "
                      f"Min: {min_val:.2f} | Std Dev: {std_dev:.2f}")
            
            analyzer.plot_data()
            analyzer.log_data(new_data)
            time.sleep(update_frequency)  # Wait for the specified update frequency
    except KeyboardInterrupt:
        print("\nStopping the real-time analysis.")
        plt.ioff()  # Disable interactive mode
        plt.show()  # Show the final plot
