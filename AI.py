# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load and Explore Data
titanic_data = pd.read_csv("titanic.csv") # Replace "titanic.csv" with your file path

# Explore the first few rows and data structure
print(titanic_data.head())
print(titanic_data.info())

# Step 3: Data Cleaning and Preprocessing
# 1. Handle missing values
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True) # Fill Age with median
titanic_data.dropna(subset=['Embarked'], inplace=True) # Drop rows with missing Embarked

# 2. Encode categorical variables
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})
titanic_data['Embarked'] = pd.factorize(titanic_data['Embarked'])[0] # Factorize Embarked

# 3. Select features (adjust as needed)
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = titanic_data[features]
y = titanic_data['Survived']

# Step 4: Train Logistic Regression Model
# 1. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Evaluate the model's performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
auc = roc_auc_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"AUC: {auc}")

# Step 5: Visualizations
# 1. Histograms and count plots
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(titanic_data['Age'], hue=titanic_data['Survived'], kde=True)
plt.title('Age Distribution by Survival')
plt.subplot(1, 2, 2)
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)
plt.title('Survival Rate by Passenger Class')
plt.show()

# 2. Confusion matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Not Survived', 'Survived'], 
            yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

# 3. ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')  # Random guess line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show(
