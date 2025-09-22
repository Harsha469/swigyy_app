import os 
import json, csv
try:
    abs_path = os.path.abspath('output.csv')

    with open(abs_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [each for each in reader]
        print(data)

    with open('inputt.json', 'w') as f:
        json.dump(data,f, indent = 4)    

except:
    print('file not exist')