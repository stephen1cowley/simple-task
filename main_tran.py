import json
import transformers
import torch

mytensor = torch.tensor([1.0 , 2.0])

# Creating a Python dictionary
data = {
    'name': 'test tensor',
    'tensor': str(mytensor),
    'shape': str(mytensor.shape)
}

# Converting the dictionary to a JSON object and saving it to a file
with open('data_tensor.json', 'w') as json_file:
    json.dump(data, json_file)

print("JSON object created and saved to 'data.json'")
