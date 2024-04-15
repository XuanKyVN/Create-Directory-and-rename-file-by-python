import yaml

data = {'train' :  '/content/hamster_Data/train/images',
        'val' :  '/content/hamster_Data/valid/images',
        'test' :  '/content/hamster_Data/test/images',
        'nc': 1,
        'names': ['hamster'],
        'numbers': [ 1,   2,   3,  4  ],
        'string1': [{['car', 'truck'],['car', 'truck']}]
        }

# overwrite the data to the .yaml file
with open(r'C:\Users\Admin\PythonLession\python\CreateDirectoryFile\output1.yaml', 'w') as f:
    yaml.dump(data, f)
'''
# read the content in .yaml file
with open('/content/hamster_Data/hamster_data.yaml', 'r') as f:
    hamster_yaml = yaml.safe_load(f)
    display(hamster_yaml)
'''