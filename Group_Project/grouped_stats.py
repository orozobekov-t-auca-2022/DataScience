import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = '../Group_Project/BFF(Group Project) statistics.xlsx'
output_directory = 'output_graphs'  # Directory to save the generated graphs

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path, index_col=0)

# Iterate over each column and create a bar graph
for column in df.columns:
    # Skip non-numeric columns (e.g., object type columns)
    if df[column].dtype not in ['int64', 'float64']:
        continue

    plt.figure(figsize=(12, 6))
    bars = plt.bar(df.index, df[column], alpha=0.7)
    plt.xlabel('Resources')
    plt.ylabel(column)
    plt.title(f'Bar Graph for {column}')

    plt.tight_layout()  # Adjust layout to prevent clipping of labels

    # Define the output file path for the bar graph
    output_file_path = os.path.join(output_directory, f'{column}_bar_chart.png')

    # Save the bar chart as an image file
    plt.savefig(output_file_path)

    # Display the plot
    plt.show()

print("All bar plots created and saved successfully!")

# Load a specific sheet named 'Come with' from the Excel file
df_come_with = pd.read_excel(file_path, index_col=0, sheet_name='Come with')

# Specify the column name for the pie chart
column_name = 'Percentage'

# Filter out rows where 'Percentage' column is not null or 0 (assuming it's a valid percentage)
filtered_df = df_come_with[df_come_with[column_name].notna() & (df_come_with[column_name] != 0)]

# Plotting a pie chart based on 'Percentage' column values
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(filtered_df[column_name], labels=filtered_df.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Percentages')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Define the output file path for the pie chart
output_file_path = os.path.join(output_directory, 'percentage_distribution_pie_chart.png')

# Save the pie chart as an image file
plt.savefig(output_file_path)

# Display the pie chart
plt.show()

print("Pie chart created and saved successfully!")
