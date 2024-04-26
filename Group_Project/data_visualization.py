import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Untitled form (Responses).xlsx'
df = pd.read_excel(file_path)
df_cleaned = df.dropna()

df_cleaned.columns = df_cleaned.columns.str.strip().str.lower()
output_file_path = 'cleaned_data.xlsx'
df_cleaned.to_excel(output_file_path, index=False)

soc_network_category = df_cleaned['откуда вы узнали о дне открытых дверей?'].value_counts()
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(soc_network_category, labels=soc_network_category.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Social Network Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

plt.figure(figsize=(16, 8))  # Increased figure size
soc_network_category.plot(kind='bar', color='skyblue')
plt.title('Distribution of Social Network Categories')
plt.xlabel('Social Network')
plt.ylabel('Count')
plt.xticks(rotation=0, fontsize = 11.5)  # Rotate x labels for better readability
plt.tight_layout()  # Adjust layout to prevent labels from being cutoff
plt.show()

hum_engagement = df_cleaned['с кем вы пришли на день открытых дверей?'].value_counts()
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(hum_engagement, labels=hum_engagement.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Engagement of Applicants')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()