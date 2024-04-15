'''
import shutil
from datetime import date

today = str(date.today())

src = 'old_file.txt'
dst = 'new_path/new_file'+ today +'.txt'
ret = shutil.move(src, dst)

print(ret)
'''


# Rename Multiple Files with Python
import os

dir = 'files/'

for file in os.listdir(dir):
    old_filepath = os.path.join(dir, file)
    new_name = 'old_' + file
    new_filepath = os.path.join(dir, new_name)

    os.rename(old_filepath, new_filepath)