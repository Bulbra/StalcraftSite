import logging
from datetime import timedelta
from logging.handlers import TimedRotatingFileHandler
import os
from pathlib import Path
import datetime

log_path = os.path.join("logs", "main.log")

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("MinuteLogger")
logger.setLevel(logging.DEBUG)
logger.handlers.clear()


handler = TimedRotatingFileHandler(
    filename=log_path,
    when="M",
    interval=1,
    backupCount=0,
    encoding='utf-8'
)


handler.suffix = "%Y-%m-%d_%H-%M"

handler.extMatch = r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}"


formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def cleanup_old_logs():

    now = datetime.now()
    cutoff_time = now - timedelta(minutes=5)

    for file_path in Path("logs").glob("app_*.log"):
        try:
            filename = file_path.name
            date_str = filename.replace("app_", "").replace(".log", "")
            file_datetime = datetime.strptime(date_str, "%Y-%m-%d_%H-%M")

            if file_datetime < cutoff_time:
                file_path.unlink()
                print(f"Удален старый лог: {file_path}")
        except (ValueError, OSError) as e:
            print(f"Ошибка при {file_path}: {e}")

current_time = datetime.now().strftime('%H:%M:%S')
logger.info(f"РФРФЫЛОРАЛФЫРАЛФЫРАЛФРЫАЛФРЫАЛОРЫФОАРФЫОЛАРОЫФР")
cleanup_old_logs()


