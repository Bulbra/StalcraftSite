import os

filesize = os.path.getsize("main.log")

if filesize > 100:
    os.remove("main.log")