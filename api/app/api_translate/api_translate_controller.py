from fastapi import APIRouter
from ..shared.classes_list import Text
from .api_translate_service import translate_text



router = APIRouter(
    prefix="/translate",
    tags=["translate"]
)

@router.post("/")
async def translate(text: Text) -> Text:
    translated, original = translate_text(text.msg, text.ppl, text.lang) 
    text.translated = translated
    text.msg = original
    # print(text)
    return text