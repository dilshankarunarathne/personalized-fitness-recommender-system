import cv2
import numpy as np
from fastapi import APIRouter, Form, UploadFile, File

router = APIRouter(
    prefix="/api",
    tags=["core"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/")
async def root(
        height: int = Form(...),
        weight: int = Form(...),
        image: UploadFile = File(...)
):
    if image.content_type != "image/jpeg":
        return "Only jpeg images are supported"

    contents = await image.read()
    nparray = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    # TODO

    return {"message": "Hello World"}
