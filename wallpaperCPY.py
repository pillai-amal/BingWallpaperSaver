import os
import shutil
from pathlib import Path

src = str(Path.home()) + "/AppData/Local/Microsoft/BingWallpaperApp/WPImages"
dest = str(Path.home()) + "/BingWallpapers"

list_of_wallpapers = os.listdir(src)
images = []
for name in list_of_wallpapers:
    if name.endswith('.jpg'):
        images.append(name)

print('Starting to copy files ...')
os.chdir(src)
for image in images:
    shutil.copy(image, dest)
    print('copied', image)
print(len(images), 'images copied to', dest)