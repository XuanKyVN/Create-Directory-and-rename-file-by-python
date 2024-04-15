import os

input_path = r'C:\Users\Admin\PythonLession\CarPlate\images\Bienxemay'

count=0

for root, dirs, files in os.walk(input_path):
     for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            count+=1
print (count)
print(len(files))


'''
for root, dirs, files in os.walk(input_path):
    for name in files:
        if os.path.splitext(name)[1] == '.TXT' or os.path.splitext(name)[1] == '.txt':
            datafiles.append(os.path.join(root,name))
    print(len(datafiles))

print (len(files))
'''