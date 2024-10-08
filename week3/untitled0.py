# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mL_WfudwjdaLEJwpXBKg18GOtTqJ86lT
"""

import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('seaborn-whitegrid')
second = 'ggplot'

x = np.linspace(-2, 4, 100)
y = x**2 - 2*x + 1

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function f(x) = x^2 - 2x + 1')
plt.grid(True)
plt.show()

x = np.linspace(-2, 4, 100)
y_f = x**3
y_g = np.exp(x)
x_h = np.linspace(0.1, 4, 100)  # log(x) is undefined for x <= 0
y_h = np.log(x_h)


plt.plot(x, y_f, label='f(x) = x^3', color='blue')
plt.plot(x, y_g, label='g(x) = e^x', color='red')
plt.plot(x_h, y_h, label='h(x) = log(x)', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), g(x), and h(x)')
plt.grid(True)
plt.legend()
plt.show()

x = np.linspace(-2, 2, 100)
y_f = x**2
y_g = x**3
y_h = x**4
y_i = x**5

plt.plot(x, y_f, label='f(x) = x^2', color='blue', linestyle='-')  # Color by name
plt.plot(x, y_g, label='g(x) = x^3', color='r', linestyle='--')   # Color by abbreviation
plt.plot(x, y_h, label='h(x) = x^4', color=(0.5, 0.2, 0.8), linestyle=':') # Color by RGB tuple
plt.plot(x, y_i, label='i(x) = x^5', color='#FF8C00', linestyle='-.') # Color by hex code

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), g(x), h(x), and i(x)')
plt.grid(True)
plt.legend()
plt.show()

# Create x and y values
x = np.linspace(-2, 4, 100)
y = x**2 - 2*x + 1

# Plot the quadratic function
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function f(x) = x^2 - 2x + 1')
plt.grid(True)
plt.show()

# Create x values for the functions f(x), g(x), and h(x)
x = np.linspace(-2, 4, 100)
# Calculate y values for functions
y_f = x**3
y_g = np.exp(x)
# Create x values for h(x) = log(x) (log(x) is undefined for x <= 0)
x_h = np.linspace(0.1, 4, 100)
# Calculate y values for h(x) = log(x)
y_h = np.log(x_h)


# Plot f(x), g(x), and h(x) with labels and colors
plt.plot(x, y_f, label='f(x) = x^3', color='blue')
plt.plot(x, y_g, label='g(x) = e^x', color='red')
plt.plot(x_h, y_h, label='h(x) = log(x)', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), g(x), and h(x)')
plt.grid(True)
plt.legend()
plt.show()

# Math for the functions f(x), g(x), h(x), and i(x)
x = np.linspace(-2, 2, 100)
y_f = x**2
y_g = x**3
y_h = x**4
y_i = x**5

# Plotting functions with all variance needed
plt.plot(x, y_f, label='f(x) = x^2', color='blue', linestyle='-')  # Color by name
plt.plot(x, y_g, label='g(x) = x^3', color='r', linestyle='--')   # Color by abbreviation
plt.plot(x, y_h, label='h(x) = x^4', color=(0.5, 0.2, 0.8), linestyle=':') # Color by RGB tuple
plt.plot(x, y_i, label='i(x) = x^5', color='#FF8C00', linestyle='-.') # Color by hex code

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), g(x), h(x), and i(x)')
plt.grid(True)
plt.legend()
plt.show()

x = np.linspace(-10, 10, 400)
y = 1 / (x**2 + 1)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(x^2 + 1)')
plt.xlim([-10, 10])  # Set x-axis limits
plt.ylim([0, 1])    # Set y-axis limits
plt.grid(True)
plt.show()


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(x^2 + 1) with Reversed Axes')
plt.gca().invert_xaxis()  # Reverse x-axis
plt.gca().invert_yaxis()  # Reverse y-axis
plt.grid(True)
plt.show()


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(x^2 + 1) with plt.axis("tight")')
plt.axis('tight')
plt.grid(True)
plt.show()


plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(x^2 + 1) with plt.axis("equal")')
plt.axis('equal')
plt.grid(True)
plt.show()

# Generate values from 0-10
x = np.linspace(0, 10, 100)

# Calculate y values for functions
y_f = [math.sqrt(xi) for xi in x]
y_g = [xi**(1/3) for xi in x]


# plottinh
plt.plot(x, y_f, label='f(x) = √x', color='blue')  # Plot f(x)
plt.plot(x, y_g, label='g(x) = x^(1/3)', color='red')  # Plot g(x)

# title, labels, and legend
plt.title('Plot of f(x) = √x and g(x) = x^(1/3)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# show plot
plt.grid(True)
plt.show()

# 50 random points
x = np.random.rand(50)
y = np.random.rand(50)

# catter plot using plt.plot()
plt.plot(x, y, 'o')
plt.title('Scatter Plot using plt.plot()')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Second scatter plot using plt.scatter()
plt.scatter(x, y)
plt.title('Scatter Plot using plt.scatter()')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Generate x values from 0 to 4π
x = np.linspace(0, 4 * np.pi, 100)

# Calculate y values
y = x * np.sin(x)

# Create a scatter plot with a line connecting the points
plt.plot(x, y, marker='o', linestyle='-',
         markersize=5, linewidth=1,
         markerfacecolor='blue',
         markeredgecolor='red',
         markeredgewidth=1)


# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Scatter Plot with Line for f(x) = x * sin(x)')


# Show the plot
plt.grid(True)
plt.show()

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calculate y values
y = x * np.cos(x)

# Plot the function as a line
plt.plot(x, y, label='f(x) = x * cos(x)', color='blue', linestyle='--')

# Generate x values for points at intervals of π/4
x_scatter = np.arange(-2 * np.pi, 2 * np.pi + np.pi / 4, np.pi / 4)

# Calculate y values for points
y_scatter = x_scatter * np.cos(x_scatter)

# Add points
plt.scatter(x_scatter, y_scatter, color='red', marker='o', label='Scatter Points')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x * cos(x) with Scatter Points')
plt.legend()
plt.grid(True)
plt.show()

plt.style.use('ggplot')
x = np.linspace(-5, 5, 400)

# Define functions
def f(x):
  return np.tan(x)

def g(x):
  return x / np.exp(-x**2)

def h(x):
  y = np.sin(x) / x
  y[x == 0] = 1  # Handle x=0 for h(x)
  return y

def i(x):
  return np.arctan(x)

def j(x):
  return 1 / (1 + np.exp(-x))


# Plot functions
plt.plot(x, f(x), label='f(x) = tan(x)', color='blue', linestyle='-')
plt.plot(x, g(x), label='g(x) = x / e^(-x^2)', color='red', linestyle='--')
plt.plot(x, h(x), label='h(x) = sin(x) / x', color='green', linestyle=':')
plt.plot(x, i(x), label='i(x) = arctan(x)', color='orange', linestyle='-.')

# Add scatter points
x_scatter = np.linspace(-5, 5, 20)
y_scatter = j(x_scatter)
plt.scatter(x_scatter, y_scatter, color='purple', marker='o', label='j(x) = 1 / (1 + e^-x)')

# Customize the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Multiple Functions')
plt.xlim([-4, 4])  # Set x-axis limits
plt.ylim([-5, 5])  # Set y-axis limits
plt.grid(True)
plt.legend()

plt.show()

plt.style.use('ggplot')

x = np.linspace(-2, 4, 100)
y_f = x**3
y_g = np.exp(x)
x_h = np.linspace(0.1, 4, 100)  # log(x) is undefined for x <= 0
y_h = np.log(x_h)

plt.plot(x, y_f, label='f(x) = x^3', color='blue')
plt.plot(x, y_g, label='g(x) = e^x', color='red')
plt.plot(x_h, y_h, label='h(x) = log(x)', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), g(x), and h(x)')
plt.grid(True)
plt.legend()
plt.show()


# seaborn-whitegrid is definitely better as this ggplot is a more aesthetic choice.
# the whitegrid allows clearer data visualition, ggplot would be better for these lines,
# while whitegrid would be better for specific points on scatter plots.