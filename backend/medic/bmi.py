"""
    BMI Calculator
    --------------
    This module contains the functions to calculate the BMI of a patient.

    Functions
    ---------
    calculate_bmi(weight, height)
        Calculates the BMI of a patient.
"""


def calculate_bmi(weight, height):
    """Calculates the BMI of a patient.

    Parameters
    ----------
    weight : int
        The weight of the patient in kilograms.
    height : int
        The height of the patient in centimeters.

    Returns
    -------
    float
        The BMI of the patient.
    """
    return weight / ((height / 100) ** 2)
