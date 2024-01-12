import cv2
import numpy as np

from fastapi import APIRouter, Form, UploadFile, File

from backend.blood_report_analyzer.main import analyze_blood_sugar_report
from backend.medic.bmi import calculate_bmi

router = APIRouter(
    prefix="/api",
    tags=["core"],
    responses={404: {"description": "The requested URL was not found"}},
)


@router.post("/")
async def root(
        height: int = Form(...),
        weight: int = Form(...),
        image: UploadFile = File(...)
):
    if image.content_type != "image/jpeg":
        return {300: {"description": "Only jpeg images are supported"}}

    contents = await image.read()
    nparray = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    bmi = calculate_bmi(weight, height)
    blood_sugar_level = analyze_blood_sugar_report(img)

    # TODO
    need = 

    return {"message": "Hello World"}
