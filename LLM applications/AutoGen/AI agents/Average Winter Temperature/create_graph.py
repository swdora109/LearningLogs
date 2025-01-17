# filename: create_graph.py
import matplotlib.pyplot as plt
import numpy as np

# Mock data: Average January temperatures for 2014-2024 in Korea
years = np.arange(2014, 2025)
temperatures = np.random.uniform(-5, 5, len(years))  # Generating mock temperatures

# Setting the ggplot style
plt.style.use('ggplot')

# Creating the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the data
ax.plot(years, temperatures, marker='o', linestyle='-', color='b')

# Setting the title and labels
ax.set_title('Changes in Average January Temperature in Korea (2014-2024)')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature (°C)')

# Setting the y-axis range and interval
ax.set_yticks(np.arange(-5, 5.5, 0.5))

# Annotating each point with its value
for year, temp in zip(years, temperatures):
    ax.annotate(f'{temp:.0f}°C', (year, temp), textcoords="offset points", xytext=(0,10), ha='center')

# Saving the graph
plt.savefig('winter_temperature_ENG.png')