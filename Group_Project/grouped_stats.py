import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = '../Group_Project/BFF(Group Project) statistics.xlsx'
output_directory = 'output_graphs'  # Directory to save the generated graphs

os.makedirs(output_directory, exist_ok=True)

df = pd.read_excel(file_path, index_col=0)

for column in df.columns:
    if df[column].dtype not in ['int64', 'float64']:
        continue
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df.index, df[column], alpha=0.7)
    plt.xlabel('Resources')
    plt.ylabel(column)
    plt.title(f'Bar Graph for {column}')
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    output_file_path = os.path.join(output_directory, f'{column}_bar_chart.png')
    plt.savefig(output_file_path)
    plt.show()
df_come_with = pd.read_excel(file_path, index_col=0, sheet_name='Come with')
column_name = 'Percentage'
filtered_df = df_come_with[df_come_with[column_name].notna() & (df_come_with[column_name] != 0)]

plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(filtered_df[column_name], labels=filtered_df.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Percentages')
plt.axis('equal', fontsize = 15)  # Equal aspect ratio ensures that pie is drawn as a circle.

output_file_path = os.path.join(output_directory, 'percentage_distribution_pie_chart.png')

plt.savefig(output_file_path)
plt.show()
