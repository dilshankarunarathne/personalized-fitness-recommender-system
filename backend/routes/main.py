import cv2
import numpy as np

from fastapi import APIRouter, Form, UploadFile, File

from backend.blood_report_analyzer.main import analyze_blood_sugar_report
from backend.meal_plan_recommender.need_calculator import get_dietary_plan
from backend.medic.bmi import calculate_bmi
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
        gender: str = Form(...),    # male, female
        image: UploadFile = File(...)
):
    if image.content_type != "image/jpeg":
        return {300: {"description": "Only jpeg images are supported"}}

    contents = await image.read()
    nparray = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    bmi = calculate_bmi(weight, height)
    dream_weight = calculate_dream_weight(weight, bmi)
    blood_sugar_level = analyze_blood_sugar_report(img)

    # TODO
    need = get_dietary_plan(weight, height, age, gender)
    workout_plan = predict_workout_plan(gender, age, weight, dream_weight, bmi)   # Gender, Age, Actual Weight, Dream Weight, BMI

    return {
        "need": need,
    }
