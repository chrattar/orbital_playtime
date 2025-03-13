import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

class RanPlot:
    def __init__(self, num_points = 1000):
        self.num_points = num_points
        self.fig = plt.figure(figsize=(12,12))
        self.ax = self.fig.add_subplot(111, projection="3d")

    def create_random_data(self):
        x = [random.randint(0,1000) for _ in range(self.num_points)]
        y = [random.randint(0,1000) for _ in range(self.num_points)]
        z = [random.randint(0,1000) for _ in range(self.num_points)]
        return x, y, z
    
    def plot_data(self, x=None, y = None, z=None):
        if x is None or y is None or z is None:
            x,y,z = self.create_random_data()
            self.ax.clear()
            self.ax.scatter(x,y,z, c ="b", marker="o")
            self.ax.set_xlabel = ("X-Axis")
            self.ax.set_ylabel = ("y-axis")
            self.ax.set_zlabel = ("z-Axis")
            self.ax.set_xlabel = ("X-Axis")
            self.ax.set_title("Ploty")
            self.ax.set_facecolor('gray')

    def plot_iterations(self, iterations=5):
        for i in range(iterations):
            x,y,z = self.create_random_data()
            self.plot_data()

    def show_plot(self):
        plt.show()

if __name__ == "__main__":
    plotter = RanPlot(num_points=1000)
    plotter.plot_data()
    plotter.show_plot()
