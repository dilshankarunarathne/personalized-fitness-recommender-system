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


def get_dietary_need(
        weight_kg: int, height_cm: int, age: int, gender: str
):
    # Calculate caloric needs
    daily_calories = calculate_caloric_needs(weight_kg, age, height_cm, gender)

    # Dietary plan
    plan = "Based on your input, your estimated daily caloric needs are approximately {:.0f} calories.".format(daily_calories)
    plan += "A balanced diet for you might include:"
    plan += "- Carbohydrates: {:.0f}% of daily calories".format(daily_calories * 0.55 / 4)
    plan += "- Proteins: {:.0f} grams".format(weight_kg * 1.2)  # Assuming 1.2g per kg of body weight
    plan += "- Fats: {:.0f} grams".format(daily_calories * 0.25 / 9)  # 25% of daily calories from fats

    return plan
