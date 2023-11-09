# statistics.py

def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI).

    :param height: Height in meters.
    :param weight: Weight in kilograms.
    :return: BMI value.
    """
    return weight / (height ** 2)

def calculate_bmr(gender, age, weight, height):
    """
    Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation.

    :param gender: 'male' or 'female'.
    :param age: Age in years.
    :param weight: Weight in kilograms.
    :param height: Height in centimeters.
    :return: BMR value.
    """
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Use 'male' or 'female'.")
    return bmr

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

    :param bmr: Basal Metabolic Rate.
    :param activity_level: Activity level factor (e.g., 1.2 for sedentary, 1.55 for moderately active).
    :return: TDEE value.
    """
    tdee = bmr * activity_level
    return tdee

