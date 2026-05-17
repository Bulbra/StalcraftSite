from fastapi import FastAPI
from API.v1 import router as api_v1_router
import uvicorn
import logging

logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("main.log", encoding="utf-8")

logger.addHandler(file_handler)



app = FastAPI()

app.include_router(api_v1_router)

@app.get("/")
async def generate_file():
    logger.debug("FAHLASHFASHFL")
    return ""

uvicorn.run(app)
