import os
for filename in os.listdir("home/artem_l/StalcraftSite/logs"):
    os.remove(os.path.join("home/artem_l/StalcraftSite/logs", filename))