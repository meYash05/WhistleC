import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ---- LOAD FEATURES ----
features_file = r"C:\Users\Yash Singh\Desktop\WhistleML\Whistle_Features.csv"
df = pd.read_csv(features_file)

# ---- SPLIT FEATURES AND LABELS ----
X = df.drop('label', axis=1)
y = df['label']

# ---- SPLIT INTO TRAIN AND TEST ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ---- BUILD MODEL ----
model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
model.fit(X_train, y_train)

# ---- EVALUATE MODEL ----
y_pred = model.predict(X_test)
print(f"🎯 Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred))

# ---- SAVE MODEL ----
model_path = r"C:\Users\Yash Singh\Desktop\WhistleML\Whistle_Detector_Model.pkl"
joblib.dump(model, model_path)

print(f"\n✅ Model saved successfully at: {model_path}")
