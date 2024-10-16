import json

# Creating a Python dictionary
data = {
    'name': 'Copilot',
    'age': 1,
    'location': 'Microsoft Cloud'
}

# Converting the dictionary to a JSON object and saving it to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

print("JSON object created and saved to 'data.json'")
