import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics
from sklearn.metrics import ConfusionMatrixDisplay

import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('BTC-USD.csv')

plt.figure(figsize=(15, 5))
plt.plot(df['Close'])
plt.title('Bitcoin Close price.', fontsize=15)
plt.ylabel('Price in dollars.')
plt.xlabel('Days', fontsize=12)
plt.savefig('bitcoin_close_price.png')  # Save the graph as a PNG file
plt.show()

df[df['Close'] == df['Adj Close']].shape, df.shape

df = df.drop(['Adj Close'], axis=1)

df.isnull().sum()

features = ['Open', 'High', 'Low', 'Close']
plt.figure(figsize=(20, 10))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    sb.distplot(df[col])
    plt.title(f'Distribution of {col}', fontsize=20)  # Set title font size to 20
    plt.xlabel(col, fontsize=16)  # Set x-axis label font size to 16
    plt.ylabel('Density', fontsize=16)  # Set y-axis label font size to 16
    plt.xticks(fontsize=14)  # Set x-axis tick label font size to 14
    plt.yticks(fontsize=14)  # Set y-axis tick label font size to 14
plt.tight_layout()
plt.savefig('bitcoin_distribution_plots.png')
plt.show()

splitted = df['Date'].str.split('-', expand=True)

df['year'] = splitted[0].astype('int')
df['month'] = splitted[1].astype('int')
df['day'] = splitted[2].astype('int')
data_grouped = df.groupby('year').mean(numeric_only=True)

# Loop over each feature ('Open', 'High', 'Low', 'Close') to plot individual bar plots
for col in ['Open', 'High', 'Low', 'Close']:
    plt.figure(figsize=(10, 8))  # Create a new figure for each feature plot
    data_grouped[col].plot.bar()  # Plot the bar plot for the current feature

    plt.title(f'Mean {col} by Year', fontsize=20)  # Set a title for the current plot
    plt.xlabel('Year', fontsize=16)  # Set label for x-axis
    plt.ylabel('Mean Value', fontsize=16)  # Set label for y-axis
    plt.xticks(rotation=45, fontsize=12)  # Rotate and set font size for x-axis tick labels
    plt.yticks(fontsize=12)  # Set font size for y-axis tick labels

    plt.tight_layout()  # Adjust subplot layout to prevent overlap
    plt.savefig(f'bitcoin_{col}_bar_plot.png')  # Save the plot as a PNG file with a specific name
    plt.show()  # Display the plot (optional)

plt.figure(figsize=(20, 10))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    sb.boxplot(x=df[col], color='skyblue', width=0.5)  # Customize box plot appearance
    plt.title(f'Box Plot of {col}', fontsize=20)
    plt.xlabel(col, fontsize=16)
    plt.ylabel('Value', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
plt.tight_layout()
plt.show()

df['is_quarter_end'] = np.where(df['month']%3==0,1,0)

df['open-close'] = df['Open'] - df['Close']
df['low-high'] = df['Low'] - df['High']
df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

# Visualize target distribution
plt.figure(figsize=(6, 6))
plt.pie(df['target'].value_counts().values, labels=[0, 1], autopct='%1.1f%%')
plt.title('Target Distribution')
plt.savefig('bitcoin_pie_chart.png')  # Save the graph as a PNG file
plt.show()

# Select only numeric columns for correlation analysis
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Plot heatmap of correlation matrix
plt.figure(figsize=(10, 8))
sb.heatmap(df[numeric_cols].corr() > 0.9, annot=True, cbar=False)
plt.title('Correlation Heatmap')
plt.savefig('bicoin_correlation_heatmap.png')
plt.show()

features = df[['open-close', 'low-high', 'is_quarter_end']]
target = df['target']

scaler = StandardScaler()
features = scaler.fit_transform(features)

X_train, X_valid, Y_train, Y_valid = train_test_split(
    features, target, test_size=0.1, random_state=2022)
print(X_train.shape, X_valid.shape)

params = {}
models = [LogisticRegression(), SVC(kernel='poly', probability=True), XGBClassifier()]

for i in range(3):
    models[i].fit(X_train, Y_train)

    print(f'{models[i]} : ')
    print('Training Accuracy : ', metrics.roc_auc_score(Y_train, models[i].predict_proba(X_train)[:, 1]))
    print('Validation Accuracy : ', metrics.roc_auc_score(Y_valid, models[i].predict_proba(X_valid)[:, 1]))
    print()

def plot_confusion_matrix(model, X_valid, Y_valid):
    # Get predictions from the model
    y_pred = model.predict(X_valid)

    # Calculate the confusion matrix
    cm = metrics.confusion_matrix(Y_valid, y_pred)

    # Display the confusion matrix using ConfusionMatrixDisplay
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])
    disp.plot(cmap='Blues')
    plt.title(f'Confusion Matrix - {type(model).__name__}')  # Use model name in the title
    plt.savefig(f'bitcoin_{type(model).__name__}.png')  # Save the plot as PNG
    plt.show()

# Iterate over each model in the list and plot confusion matrix for validation data
for model in models:
    # Assuming models are already trained
    plot_confusion_matrix(model, X_valid, Y_valid)