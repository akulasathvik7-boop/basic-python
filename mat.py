import matplotlib.pyplot as plt
# x=[2022,2023,2024,2025,2026]
# y=[122,44,177,11,99]
# plt.pie(x,y)
# plt.title("Analysing the records in every year")
# # plt.xlabel("Years")
# # plt.ylabel("sales")
# plt.show()

import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [35, 25, 25, 15]  # The values for each slice
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']  # The labels for each slice
colors = ['#ff9999', '#66b2ff', '#99ff99', '#ffcc99'] # Optional: custom colors
explode = (0.1, 0, 0, 0) # Optional: "explode" the first slice

# Create the pie chart
plt.figure(figsize=(8, 6)) # Optional: set the figure size
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%', # Display percentage values with one decimal point
    shadow=True, # Add a shadow effect
    startangle=90, # Start the first slice at 90 degrees (top of the circle)
    explode=explode # Apply the explode effect
)

plt.title('Fruit Preferences Survey Results') # Add a title to the chart
plt.axis('equal')  # Ensures the pie chart is drawn as a perfect circle
plt.legend(labels, loc="best") # Add a legend

# Display the chart
plt.show()
