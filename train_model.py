import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load cleaned data
df = pd.read_csv("cleaned_dataset.csv")

# Step 1: Create Target column if not exists
if 'Target' not in df.columns:
    df['Target'] = df['Aircraft Lost'].apply(lambda x: 1 if x > 0 else 0)

# Drop rows where Target is missing
df = df.dropna(subset=["Target"])

# Step 2: Encode all object (categorical) columns
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# Step 3: Split data into features and label
X = df.drop(columns=["Target"])
y = df["Target"]

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Save model and features
joblib.dump(model, "ww2_model.pkl")
joblib.dump(X.columns.tolist(), "model_features.pkl")

print("✅ Model saved as ww2_model.pkl")
print("✅ Feature names saved as model_features.pkl")
