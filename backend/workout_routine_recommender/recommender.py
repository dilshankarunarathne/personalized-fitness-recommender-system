import joblib
import pandas as pd

# Define the categorical and numerical features
cat_features = ['Gender']
num_features = ['Dream Weight', 'Actual Weight', 'Age', 'BMI']

# Load the model
loaded_model = joblib.load('model.pkl')

# Load the LabelEncoder
loaded_le = joblib.load('label_encoder.pkl')


def predict_workout_plan(
    gender: str,    # 'Male' / 'Female'
    age: int,
    actual_weight: int,
    dream_weight: int,
    bmi: float
):
    # Define a new observation as a DataFrame
    # Replace 'Male' with the actual encoded value for the gender
    new_observation = pd.DataFrame([['Male', 25, 70, 45, 29]],  # Gender, Age, Actual Weight, Dream Weight, BMI
                                   columns=cat_features + num_features)

    # Use the model to predict the exercise and intensity
    exercise_encoded, intensity, duration = loaded_model.predict(new_observation)[0]

    # Decode 'Exercise' back to its original form
    exercise = loaded_le.inverse_transform([int(exercise_encoded)])[0]

    return f"Predicted Exercise: {exercise}, Intensity: {intensity}, Duration: {duration}"

print()
