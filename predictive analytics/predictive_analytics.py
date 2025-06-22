import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Load the dataset
df = pd.read_csv("data.csv")

# Convert diagnosis to priority label
df['priority'] = df['diagnosis'].map({'M': 'high', 'B': 'low'})

# Drop unused columns
X = df.drop(columns=['diagnosis', 'priority', 'id', 'Unnamed: 32'], errors='ignore')
y = df['priority']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Define and train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred, average='weighted'))
print(classification_report(y_test, y_pred))
