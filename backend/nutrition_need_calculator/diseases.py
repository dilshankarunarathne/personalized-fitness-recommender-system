def get_diseases(blood_sugar_level, bmi):
    diseases = []
    if blood_sugar_level is not None and blood_sugar_level > 140:
        diseases.append('diabeties')
    if bmi > 25:
        diseases.append('obesity')
