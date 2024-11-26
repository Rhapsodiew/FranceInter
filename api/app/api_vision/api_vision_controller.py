from fastapi import APIRouter
from ..shared.classes_list import Img
from .api_vision_service import people_in_img, is_too_much_ppl

router = APIRouter(
    prefix="/vision",
    tags=["vision"]
)

@router.post("/")
async def find_people(img: Img) -> bool:
    nb_of_ppl = people_in_img(img.path)
    too_much = is_too_much_ppl(nb_of_ppl,img.ppl)
    return too_much
    