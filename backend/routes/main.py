import cv2
import numpy as np

from fastapi import APIRouter, Form, UploadFile, File

from backend.blood_report_analyzer.main import analyze_blood_sugar_report
from backend.diet_plan_recommender.main import get_meal_plan
from backend.nutrition_need_calculator.diseases import get_diseases
from backend.nutrition_need_calculator.need_calculator import get_dietary_need
from backend.medic.main import calculate_bmi, calculate_dream_weight
from backend.workout_routine_recommender.recommender import predict_workout_plan

router = APIRouter(
    prefix="/api",
    tags=["core"],
    responses={404: {"description": "The requested URL was not found"}},
)


@router.post("/")
async def root(
        height: int = Form(...),
        weight: int = Form(...),
        age: int = Form(...),
        gender: str = Form(...),
        image: UploadFile = File(...),
        diseases_info: str = Form(None),
):
    print("data: ", )
    bmi = calculate_bmi(weight, height)
    dream_weight = calculate_dream_weight(weight, bmi)

    if image and image.content_type != "image/jpeg":
        # return {300: {"description": "Only jpeg images are supported"}} # TODO fix this
        diseases = get_diseases(None, bmi)
    else:
        contents = await image.read()
        if contents:  # Check if the image file is not empty
            nparray = np.fromstring(contents, np.uint8)
            img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

            blood_sugar_level = analyze_blood_sugar_report(img)
            diseases = get_diseases(blood_sugar_level, bmi)
        else:
            diseases = get_diseases(None, bmi)

    nutrition_need = get_dietary_need(weight, height, age, gender.lower())  # 'male' 'female'
    workout_plan = predict_workout_plan(gender, age, weight, dream_weight, bmi)  # TODO gender - 'Male' 'Female'

    meal_plan = get_meal_plan(['low_sodium_diet', 'low_fat_diet'], diseases, ['calcium', 'vitamin_c'], ['non-veg'],
                              'i love indian')
    # ['low_sodium_diet','low_fat_diet'], ['diabeties'], ['calcium','vitamin_c'], ['non-veg'],'i love indian'

    if diseases_info is not None:
        workout_plan = "Not recommended until be validated by a doctor! " + workout_plan

    return {
        "need": nutrition_need,
        "workout_plan": workout_plan,
        "meal_plan": meal_plan,
    }
