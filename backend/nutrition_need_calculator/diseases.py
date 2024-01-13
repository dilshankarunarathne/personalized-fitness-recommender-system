def get_diseases():
    diseases = []
    if blood_sugar_level > 140:
        diseases.append('diabeties')
    if bmi > 25:
        diseases.append('obesity')