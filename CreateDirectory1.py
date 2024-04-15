

# Python program to explain os.makedirs() method 
  
# importing os module 
import os 
  
# os.makedirs() method will raise 
# an OSError if the directory 
# to be created already exists 
# But It can be suppressed by 
# setting the value of a parameter 
# exist_ok as True 
  
# Directory 
directory = ["train","valid","test"]
subdirectory = ["images","labels"]

#directory = "train"
  
# Parent Directory path 
parent = "C:/Users/Admin/PythonLession/python/CreateDirectoryFile"
projname="carpark"

def createDirectory(parent_dir,mdirectory):
    # Path 
    path = os.path.join(parent_dir, mdirectory) 

    #if directory is exited, do not create
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



for i in directory:
    createDirectory(parent,i)
    #print (i)
    subpath=parent+"/"+i
    print (subpath)
    for j in subdirectory:
        createDirectory(subpath,j)
        print(j)

