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


def get_dietary_plan(
        weight_kg: int, height_cm: int, age: int, gender: str
):
    # Asking user for their details
    weight = float(input("Please enter your weight in kilograms: "))
    age = int(input("Please enter your age in years: "))
    height = float(input("Please enter your height in centimeters: "))
    gender = input("Please enter your gender (male/female): ").lower()

    # Calculate caloric needs
    daily_calories = calculate_caloric_needs(weight, age, height, gender)

    # Dietary plan
    print("\nBased on your input, your estimated daily caloric needs are approximately {:.0f} calories.".format(
        daily_calories))
    print("A balanced diet for you might include:")
    print("- Carbohydrates: {:.0f}% of daily calories".format(daily_calories * 0.55 / 4))
    print("- Proteins: {:.0f} grams".format(weight * 1.2))  # Assuming 1.2g per kg of body weight
    print("- Fats: {:.0f} grams".format(daily_calories * 0.25 / 9))  # 25% of daily calories from fats
