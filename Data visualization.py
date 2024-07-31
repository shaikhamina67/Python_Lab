import matplotlib.pyplot as plt

# Given data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create a line plot
plt.plot(x, y, marker='o')  # marker='o' adds markers at data points

# Add title and labels
plt.title('Line Plot of Given Data')
plt.xlabel('x values')
plt.ylabel('y values')

# Show the plot
plt.grid(True)  # Optional: adds a grid for better readability
plt.show()
