import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

class DataVisualizer:
    def __init__(self, num_points=100):
        self.num_points = num_points
        self.data = self.generate_data()

    def generate_data(self):
        """Generate random data for visualization."""
        x = np.linspace(0, 10, self.num_points)
        y = np.sin(x) + np.random.normal(0, 0.1, self.num_points)  # Sine wave with noise
        return x, y

    def user_defined_data(self):
        """Get user-defined data."""
        x = list(map(float, input("Enter X values separated by commas: ").split(',')))
        y = list(map(float, input("Enter Y values separated by commas: ").split(',')))
        return x, y

    def normalize_data(self, data):
        """Normalize the data to the range [0, 1]."""
        return (data - np.min(data)) / (np.max(data) - np.min(data))

    def line_plot(self, x=None, y=None, title='Line Plot', color='blue'):
        """Create a line plot."""
        if x is None or y is None:
            x, y = self.data
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label='Data', color=color)
        plt.title(title)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid()
        plt.show()

    def bar_chart(self):
        """Create a bar chart."""
        categories = ['A', 'B', 'C', 'D', 'E']
        values = np.random.randint(1, 10, size=len(categories))

        plt.figure(figsize=(10, 5))
        plt.bar(categories, values, color='orange')
        plt.title('Bar Chart Example')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.show()

    def scatter_plot(self):
        """Create a scatter plot."""
        x, y = self.data
        plt.figure(figsize=(10, 5))
        plt.scatter(x, y, color='green', alpha=0.5)
        plt.title('Scatter Plot of Data Points')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid()
        plt.show()

    def histogram(self):
        """Create a histogram."""
        data = np.random.randn(self.num_points)
        plt.figure(figsize=(10, 5))
        plt.hist(data, bins=20, color='purple', alpha=0.7)
        plt.title('Histogram of Random Data')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

    def pie_chart(self):
        """Create a pie chart."""
        categories = ['Category A', 'Category B', 'Category C', 'Category D']
        values = [15, 30, 45, 10]

        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart Example')
        plt.show()

    def box_plot(self):
        """Create a box plot."""
        data = [np.random.normal(size=self.num_points) for _ in range(4)]
        plt.figure(figsize=(10, 5))
        plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4'])
        plt.title('Box Plot of Random Data')
        plt.ylabel('Value')
        plt.show()

    def interactive_plot(self):
        """Create an interactive scatter plot using Plotly."""
        x, y = self.data
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(color='blue', size=10)))
        fig.update_layout(title='Interactive Scatter Plot', xaxis_title='X-axis', yaxis_title='Y-axis')
        fig.show()

if __name__ == "__main__":
    visualizer = DataVisualizer(num_points=100)

    while True:
        print("\nChoose a visualization type:")
        print("1. Line Plot")
        print("2. User Defined Line Plot")
        print("3. Bar Chart")
        print("4. Scatter Plot")
        print("5. Histogram")
        print("6. Pie Chart")
        print("7. Box Plot")
        print("8. Interactive Plot")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            visualizer.line_plot()
        elif choice == '2':
            x, y = visualizer.user_defined_data()
            visualizer.line_plot(x, y, title='User Defined Line Plot', color='orange')
        elif choice == '3':
            visualizer.bar_chart()
        elif choice == '4':
            visualizer.scatter_plot()
        elif choice == '5':
            visualizer.histogram()
        elif choice == '6':
            visualizer.pie_chart()
        elif choice == '7':
            visualizer.box_plot()
        elif choice == '8':
            visualizer.interactive_plot()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
