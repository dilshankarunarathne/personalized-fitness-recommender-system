def calculate_caloric_needs(weight_kg, age_years, height_cm, gender):
    """
    Calculate the Basal Metabolic Rate (BMR) using the Harris-Benedict Equation.
    This function assumes the user is moderately active.

    Parameters:
    weight_kg (float): Weight in kilograms
    age_years (int): Age in years
    height_cm (float): Height in centimeters
    gender (str): Gender of the user ("male" or "female")

    Returns:
    float: Estimated daily caloric needs
    """

    # Harris-Benedict Equation
    if gender == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age_years)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age_years)

    # Assuming moderate activity level
    return bmr * 1.55

