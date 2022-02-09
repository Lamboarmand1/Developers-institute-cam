import requests,  json

url=f'http://api.weatherstack.com/current?access_key=a8180b42b7314d989b18bdb28fb3507a&query=Yaounde'

'''r= requests.get(url)
print(r.text)
data = r.json()
print(data)
print('Info about time')
print(data['location']['localtime'])
'''
my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)

    