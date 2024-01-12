import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, Normalizer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
import joblib

# Load the dataset
df = pd.read_csv('dataset.csv')

# Define the categorical and numerical features
cat_features = ['Gender']
num_features = ['Dream Weight', 'Actual Weight', 'Age', 'BMI']

# Define the target variables
output_features = ['Exercise', 'Exercise Intensity', 'Duration']

# Encode 'Exercise' column
le = LabelEncoder()
df['Exercise'] = le.fit_transform(df['Exercise'])

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    df[cat_features + num_features],
    df[output_features],
    test_size=0.33,
    random_state=42
)

# Define the transformers
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('normalizer', Normalizer())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OrdinalEncoder())
])

# Combine the transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('numeric', numeric_transformer, num_features),
        ('categorical', categorical_transformer, cat_features)
    ]
)

# Define the model
model = MultiOutputRegressor(GradientBoostingRegressor())

# Define the pipeline
pipeline = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('reg', model)
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, 'model.pkl')

# Save the LabelEncoder
joblib.dump(le, 'label_encoder.pkl')

# Load the model
loaded_model = joblib.load('model.pkl')

# Load the LabelEncoder
loaded_le = joblib.load('label_encoder.pkl')

# Define a new observation as a DataFrame
# Replace 'Male' with the actual encoded value for the gender
new_observation = pd.DataFrame([['Male', 25, 70, 45, 29]],  # Gender, Age, Actual Weight, Dream Weight, BMI
                               columns=cat_features + num_features)

# Use the model to predict the exercise and intensity
exercise_encoded, intensity, duration = loaded_model.predict(new_observation)[0]

# Decode 'Exercise' back to its original form
exercise = loaded_le.inverse_transform([int(exercise_encoded)])[0]

print(f"Predicted Exercise: {exercise}, Intensity: {intensity}, Duration: {duration}")
