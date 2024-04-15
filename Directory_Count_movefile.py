# importing os module
import os
# Directory
directory = ["train" ,"valid" ,"test"]
subdirectory = ["images" ,"labels"]

# directory = "train"

# Parent Directory path
parent = "C:/Users/Admin/PythonLession/python/CreateDirectoryFile"  # Main directory of main project
projname ="motor_plate1"       # project name
input_path = parent +"/" + "movefileTest"  # folder include image and txt file after annotated
set_train=65/100
set_valid=20/100


def createDirectory(parent_dir ,mdirectory):
    # Path
    path = os.path.join(parent_dir, mdirectory)

    # if directory is exited, do not create
    isExist = os.path.exists(path)
    print(isExist)
    # Create the directory
    # 'Nikhil'
    if not isExist:
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % mdirectory)
        except OSError as error:
            print("Directory '%s' can not be created" % mdirectory)
    else:
        print("Directory is availabled")
#----------------------------------------------
#MAIN PROGRAM
#Create Main project folder

isExist = os.path.exists(parent+"/"+projname)
if not isExist:
    createDirectory(parent ,projname)

    # Create sub directory for main project
    for i in directory:
        createDirectory(parent+"/"+projname ,i)
        # print (i)
        subpath = parent +"/" +projname+"/"+i
        print (subpath)
        for j in subdirectory:
            createDirectory(subpath ,j)
            print(j)
else:
    print ("project is availabel")
#-------------------------------------------------------------------
# Count number of files in folder, make sure train is 65% files, valid is 20% and the rest is test
# I will move file.jpg and txt to folder Images then move txt from Image to labels Folder

#count=0

for root, dirs, files in os.walk(input_path):
     for file in files:
        filename, extension = os.path.splitext(file)

print(len(files))
count = len(files)
train=0
valid=0
test=0

if (count % 2) == 0:
    train = int(count * set_train)   #65%
    if (train % 2) != 0:
        train +=1

    valid = int(count * set_valid)  # 65%
    if (valid % 2) != 0:
        valid += 1
    test = count - train-valid  # 15%
else:
    print("data fail")

print(train)
print(valid)
print(test)

#----------------------------------------------Complete check number of file--------------------
#Start Moving files

import shutil
train_img_path = parent+"/"+projname+"/train"+"/images"
train_lbl_path = parent+"/"+projname+"/train"+"/labels"
valid_img_path = parent+"/"+projname+"/valid"+"/images"
valid_lbl_path = parent+"/"+projname+"/valid"+"/labels"
test_img_path = parent+"/"+projname+"/test"+"/images"
test_lbl_path = parent+"/"+projname+"/test"+"/labels"

count_img_train=0
count_lbl_train=0
count_img_valid=0
count_lbl_valid=0
count_img_test=0
count_lbl_test=0

for root, dirs, files in os.walk(input_path):
     for file in files:
        filename, extension = os.path.splitext(file)
        if len(files)>0 or len(files)%2 !=0:
            if extension == '.txt':
                if count_lbl_train<train/2:
                    shutil.move(input_path+"/"+filename+".txt", train_lbl_path+"/"+filename+".txt")
                    count_lbl_train += 1
                elif count_lbl_valid<valid/2:
                    shutil.move(input_path + "/" + filename + ".txt", valid_lbl_path + "/" + filename + ".txt")
                    count_lbl_valid += 1
                else:
                    shutil.move(input_path + "/" + filename + ".txt", test_lbl_path + "/" + filename + ".txt")

            if extension == '.jpg':
                if count_img_train<train/2:
                    shutil.move(input_path+"/"+filename+".jpg", train_img_path+"/"+filename+".jpg")
                    count_img_train +=1
                elif count_img_valid<valid/2:
                    shutil.move(input_path + "/" + filename + ".jpg", valid_img_path + "/" + filename + ".jpg")
                    count_img_valid += 1
                else:
                    shutil.move(input_path + "/" + filename + ".jpg", test_img_path + "/" + filename + ".jpg")
        else:
            print("folder is empty or number of file is incorrect (odd) ")


