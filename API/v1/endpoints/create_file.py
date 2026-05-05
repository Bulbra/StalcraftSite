from fastapi import APIRouter
import os
import subprocess
router = APIRouter(
    prefix="/create_file",
)


@router.get("/user_file")
async def generate_file(filename, text):
        subprocess.run(f"touch {filename}", shell=True)
        subprocess.run(f"echo {text} > {filename}")
