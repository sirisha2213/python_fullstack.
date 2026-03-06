# json file

import json
'''
# write
with open('demo.json','w') as file:
    data=[
    {'id':'1','name':'saaketh'},
    {'id':'2','name':'swapnil'},
    {'id':'3','name':'praveen'},
    {'id':'4','name':'dileep'},
    ]
    json.dump(data,file,indent=4)
    print('data saved successfully')
'''
#read
with open('demo.json','r') as file:
    data = json.load(file)
data.append({'id':'5','name':'sirisha'})

with open('demo.json','w') as file:
    json.dump(data,file,indent=4)
