import os
from sys import argv
import zipfile

for i in os.listdir(argv[1]):
    if ".zip" in i:
        print(f"Extracting: {argv[1] + i}")

        folder_name = argv[1] + i.split('.zip')[0]
        zip_file = argv[1] + i

        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        with zipfile.ZipFile(zip_file, 'r') as zip:
            zip.extractall(folder_name)
        print('Success!')
        print(f'\tDeleting {zip_file}')
        #qos.remove(zip_file)