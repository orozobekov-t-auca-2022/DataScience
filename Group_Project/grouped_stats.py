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
    plt.xlabel('Resources', fontsize=14)  # Increase font size for x-axis label
    plt.ylabel(column, fontsize=14)  # Increase font size for y-axis label
    plt.title(f'Bar Graph for {column}', fontsize=16)  # Increase font size for title
    plt.xticks(fontsize=11)  # Increase font size for x-axis tick labels
    plt.yticks(fontsize=11)  # Increase font size for y-axis tick labels

    # Annotate numbers on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', fontsize=10)

    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    output_file_path = os.path.join(output_directory, f'{column}_bar_chart.png')
    plt.savefig(output_file_path)
    plt.show()

df_come_with = pd.read_excel(file_path, index_col=0, sheet_name='Come with')
column_name = 'Percentage'
filtered_df = df_come_with[df_come_with[column_name].notna() & (df_come_with[column_name] != 0)]
