from fastapi import APIRouter
from ..shared.classes_list import Text
from .api_speech_service import speech_text
router = APIRouter(
    prefix = "/speech",
    tags = ["speech"],
)

@router.post("/")
async def speech(text: Text) -> Text:
    speech_text(text.msg)
    if text.translated:                 
        speech_text(text.translated)
    return text
