import shutil
import os
# absolute path
src_path = r"C:\Users\Admin\PythonLession\CarPlate\movefileTest"
dst_path = r"C:\Users\Admin\PythonLession\CarPlate\movedest"
count=0


for root, dirs, files in os.walk(src_path):
     for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            count+=1
            shutil.move(src_path+"/"+filename+".txt", dst_path+"/"+filename+".txt")

print (count)
print(len(files))





