import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = 'Untitled form (Responses).xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

print("\nMissing values:")
print(df.isnull().sum())

# Drop rows with any missing values (if needed)
df_cleaned = df.dropna()

# Example: Cleaning column names (strip whitespace and convert to lowercase)
df_cleaned.columns = df_cleaned.columns.str.strip().str.lower()

output_file_path = 'cleaned_data.xlsx'
df_cleaned.to_excel(output_file_path, index=False)

# Plotting and saving the pie chart for 'откуда вы узнали о дне открытых дверей?'
soc_network_category = df_cleaned['откуда вы узнали о дне открытых дверей?'].value_counts()
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(soc_network_category, labels=soc_network_category.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Social Network Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('social_network_categories.png')  # Save the pie chart as an image
plt.show()

# Plotting and saving the pie chart for 'с кем вы пришли на день открытых дверей?'
hum_engagement = df_cleaned['с кем вы пришли на день открытых дверей?'].value_counts()
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(hum_engagement, labels=hum_engagement.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Engagement of Applicants')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('engagement_of_applicants.png')  # Save the pie chart as an image
plt.show()

print("Plots saved as 'social_network_categories.png' and 'engagement_of_applicants.png'")
