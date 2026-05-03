from fastapi import APIRouter
import os
router = APIRouter(
    prefix="/create_file",
)


@router.get("/user_file")
async def generate_password(filename, text):
    if not os.Path.Exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.Write(f'{text}\n')
            print(f'Файл {filename} создан')
    else:
        print(f'Файл {filename} уже существует')
