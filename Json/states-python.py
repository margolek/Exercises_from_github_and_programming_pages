import json

filename = 'states.json'

with open(filename) as json_obj:
	data = json.load(json_obj)

for state in data['states']:
	print(state['name'])


#Remove 'area_codes' key and then write to new file

for state in data['states']:
	del state['area_codes']

with open('new_states.json','w') as json_obj:
	json.dump(data, json_obj,indent=2)

