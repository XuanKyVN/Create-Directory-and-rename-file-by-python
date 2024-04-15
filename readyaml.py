# fruits.yaml file
'''
apples: 20
mangoes: 2
bananas: 3
grapes: 100
pineapples: 1

# categories.yaml file

sports:

  - soccer
  - football
  - basketball
  - cricket
  - hockey
  - table tennis

countries:

  - Pakistan
  - USA
  - India
  - China
  - Germany
  - France
  - Spain

  '''

# process_yaml.py file

import yaml

with open(r'C:\Users\Admin\PythonLession\python\CreateDirectoryFile\data.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    readdata = yaml.load(file, Loader=yaml.FullLoader)

    print(readdata)




import yaml

#dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
#{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]


#dict_file= ["train: ../train/images","valid: ../valid/images"]

def write_yaml_to_file(py_obj,filename):
    with open(f'{filename}.yaml', 'w',) as f :
        yaml.dump(py_obj,f,sort_keys=False)
    print('Written to file successfully')


names = {0: 'LicensePlate',1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:'A', 12:'B', 13:'C',
         14:'D', 15:'E', 16:'F', 17:'G', 18:'H', 19:'I',20:'J',21:'K', 22:'L', 23:'M', 24:'N',
         25:'O',26:'P',27:'Q', 28:'R', 29:'S', 30:'T', 31:'U', 32:'V',33: 'W',34:'X', 35:'Y', 36:'Z'}



dict_file ={'train': '../train/images', 'valid':'../valid/images','test':'../test/images', 'nc':37, 'names': names}

write_yaml_to_file(dict_file, 'output1')
