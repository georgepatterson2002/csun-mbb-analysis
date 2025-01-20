import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

#Load Data
data = pd.read_csv('/Users/george/Desktop/mbb-ml/cbb.csv')

# Drop unnecessary columns
columns_to_drop = ['CONF', 'POSTSEASON', 'G', 'W', 'TEAM', 'BARTHAG', 'WAB', 'EFG_O', 'EFG_D', 'YEAR']
data = data.drop(columns = columns_to_drop, errors='ignore')

# Handle missing values
data = data.dropna()

# Create new interactiction metrics
##data['Efficiency_Margin'] = data['ADJOE'] - data['ADJDE']

# Categorize Seed
bins = [0, 4, 8, 16]
labels = ['High', 'Medium', 'Low'] ## 1 = High, 2 = Medium, 3 = Low
data['Seed_Category'] = pd.cut(data['SEED'], bins=bins, labels=labels)

# Separate features and target
X = data.drop(['SEED', 'Seed_Category'], axis=1)
y = data['Seed_Category']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Select only numeric columns
data_numeric = data.select_dtypes(include=['number'])

# Correlation matrix for feature refinement
correlation_matrix = data_numeric.corr()
plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Refined Feature Correlation Matrix")
plt.show()

# Initialize model
clf = RandomForestClassifier(random_state=42)

# Train model
clf.fit(X_train, y_train)

# Predicy on test data
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Feature importance
importances = clf.feature_importances_
feature_names = X.columns

# Sort and plot
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Feature Importance')
plt.show()

# Remove Efficiency Margin for model (Derived from ADJOE and ADJDE)
##X=X.drop('Efficiency_Margin', axis=1)

# setup SVC model
svc_model = SVC(kernel='linear', random_state=42)

# Train SVC
svc_model.fit(X_train, y_train)

# Make predictions
y_pred = svc_model.predict(X_test)

# Evaluate the model
print(f"Accuracy on test set: {accuracy_score(y_test, y_pred):.4f}")



