import joblib
import pandas as pd

from backend.config import get

model_path = get('model', 'model')
label_encoder_path = get('model', 'label_encoder')

# Define the categorical and numerical features
cat_features = ['Gender']
num_features = ['Dream Weight', 'Actual Weight', 'Age', 'BMI']

# Load the model
loaded_model = joblib.load(model_path)

# Load the LabelEncoder
loaded_le = joblib.load(label_encoder_path)


def predict_workout_plan(
    gender: str,    # 'Male' / 'Female'
    age: int,
    actual_weight: int,
    dream_weight: int,
    bmi: float
) -> str:
    # Define a new observation as a DataFrame
    # Replace 'Male' with the actual encoded value for the gender
    # data = ['Male', 25, 70, 45, 29]
    new_observation = pd.DataFrame([[gender, age, actual_weight, dream_weight, bmi]],
                                   # Gender, Age, Actual Weight, Dream Weight, BMI
                                   columns=cat_features + num_features)

    # Use the model to predict the exercise and intensity
    exercise_encoded, intensity, duration = loaded_model.predict(new_observation)[0]

    # Decode 'Exercise' back to its original form
    exercise = loaded_le.inverse_transform([int(exercise_encoded)])[0]

    return f"Predicted Exercise: {exercise}, Intensity: {intensity}, Duration: {duration}"
