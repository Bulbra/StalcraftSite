import os
import sys

result = os.system('git -C StalcraftSite pull')

if result != 0:
    print("ошибка гита")
    sys.exit(1)

os.system('pkill -HUP -f uvicorn')