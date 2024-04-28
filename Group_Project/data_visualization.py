import textwrap
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Untitled form (Responses).xlsx'
df = pd.read_excel(file_path)
df_cleaned = df.dropna()

df_cleaned.columns = df_cleaned.columns.str.strip().str.lower()
output_file_path = 'cleaned_data.xlsx'
df_cleaned.to_excel(output_file_path, index=False)

soc_network_category = df_cleaned['откуда вы узнали о дне открытых дверей?'].value_counts()
plt.figure(figsize=(16, 8))
bars = plt.bar(range(len(soc_network_category)), soc_network_category, color='skyblue')
plt.xticks(range(len(soc_network_category)), [textwrap.fill(label, 20) for label in soc_network_category.index], rotation=0, fontsize=11.5)

plt.title('Distribution of Social Network Categories',fontsize=15)
plt.xlabel('Social Network', fontsize=13)
plt.ylabel('Count', fontsize=13)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', fontsize=12)
plt.tight_layout()
plt.show()

hum_engagement = df_cleaned['с кем вы пришли на день открытых дверей?'].value_counts()

plt.figure(figsize=(12, 6))  # Set the figure size
bars = hum_engagement.plot(kind='bar', color='salmon', fontsize=15)

for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

plt.title('Distribution of Engagement of Applicants')
plt.xlabel('Engagement', fontsize=13)
plt.ylabel('Count', fontsize=13)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
