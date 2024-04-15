'''
# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

	folder = "xyz"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"Hostel {str(count)}.jpg"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"

		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

	# Calling main() function
	main()


'''
import os
from os import path
import shutil

Source_Path = 'C:/Users/Admin/PythonLession/CarPlate/images/test4'
Destination = 'C:/Users/Admin/PythonLession/CarPlate/images/test4'
#dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  "Pic_" + str(count) + ".jpg"

        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()