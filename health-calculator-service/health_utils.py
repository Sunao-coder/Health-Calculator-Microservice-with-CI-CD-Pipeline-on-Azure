def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    return weight / (height ** 2)

def calculate_bmr(height_cm, weight_kg, age, gender):
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'")
