import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a pandas DataFrame
df = pd.read_excel("cleaned_data.xlsx", usecols=[1, 2], names=["откуда вы узнали о дне открытых дверей?", "с кем вы пришли на день открытых дверей?"])

# Remove rows with "Я пришел" in the second column
df = df[df["с кем вы пришли на день открытых дверей?"] != "Я пришел"]

# Rename the social media "Новостные издания (Kaktus Media)" to "Kaktus Media"
df["откуда вы узнали о дне открытых дверей?"] = df["откуда вы узнали о дне открытых дверей?"].replace("Новостные издания (Kaktus Media)", "Kaktus Media")

# Group by Social Media and Who, then count the occurrences
grouped_data = df.groupby(["откуда вы узнали о дне открытых дверей?", "с кем вы пришли на день открытых дверей?"]).size().reset_index(name='Count')

# Pivot the data to create a matrix of counts
pivot_table = grouped_data.pivot(index='откуда вы узнали о дне открытых дверей?', columns='с кем вы пришли на день открытых дверей?', values='Count').fillna(0)

# Define colors for the bars
colors = plt.cm.tab20.colors[:len(pivot_table.columns)]

# Plotting stacked bar chart
pivot_table.plot(kind='bar', stacked=True, color=colors)
plt.xlabel('Social Media')
plt.ylabel('Frequency')
plt.title('Relationship between Social Media and Who People Come With')
plt.legend(title='Who', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Print the analysis
print("Relationship between Social Media and Who People Come With:")
print(pivot_table)