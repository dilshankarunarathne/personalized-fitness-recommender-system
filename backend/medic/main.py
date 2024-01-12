"""
    BMI Calculator
    --------------
    This module contains the functions to calculate the BMI of a patient.

    Functions
    ---------
    calculate_bmi(weight, height)
        Calculates the BMI of a patient.
"""


def calculate_dream_weight(weight, bmi):
    """Calculates the dream weight of a patient.

    Parameters
    ----------
    weight : int
        The weight of the patient in kilograms.
    bmi : float
        The BMI of the patient.

    Returns
    -------
    int
        The dream weight of the patient.
    """

    if bmi > 25:
        return weight * 0.95
    elif bmi < 18.5:
        return weight * 1.1
    else:
        return weight


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
