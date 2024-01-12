from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/api",
    tags=["core"],
    responses={404: {"description": "The requested page was not found"}},
)


@router.post("/")
async def root(
        height: int = Form(...),
        weight: int = Form(...),
        file: UploadFile = File(...)
):
    return {"message": "Hello World"}
