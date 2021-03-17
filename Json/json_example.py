import json



people_string = '''
{
	"people":[
		{
			"name": "John Smith",
			"phone": "997-998-999",
			"emails": ["johnsmith@gmail.com", "johnsmith@yahoo.com"],
			"has_license": false
		},
		{
			"name": "Muhamed Ali",
			"phone": "123-456-789",
			"emails": null,
			"has_license": true
		}
	]
}
'''

#Load json format
data = json.loads(people_string)
print(type(people_string))
print(type(data['people']))
print(data)

for person in data['people']:
	print(person['name'])

#Dump Python object into a json format
for person in data['people']:
	del person['phone']

#Use extra rgument in order to better see indentation
#We can also sors keys by adding sort_key argument
new_string = json.dumps(data,indent=2, sort_keys=True)
print(new_string)