from .api_speech import api_speech_controller
from .api_translate import api_translate_controller
from .api_vision import api_vision_controller
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3002"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_vision_controller.router)
app.include_router(api_speech_controller.router)
app.include_router(api_translate_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)