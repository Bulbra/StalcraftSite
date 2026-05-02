from fastapi import APIRouter
import os
router = APIRouter(
    prefix="/createfile",
)


@router.get("/generate_password")
async def generate_password(filename, text):
    if not os.Path.Exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.Write('Файл создан\n')
            print(f'Файл {filename} создан')
    else:
        print(f'Файл {filename} уже существует')
