import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000") # using url above

# TODO: print the status code
print('Status Code Value:', r.status_code)
# TODO: print the welcome message
print(r.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = requests.post('http://127.0.0.1:8000/data', data = json.dumps(data)) 
# post function for url with jason

# TODO: print the status code
print('Status Code Value:', r.status_code)
# TODO: print the result
print(r.json())

#adding comment for gitaction testing
#adding another comment
#adding another comment
#adding line for comment
#adding line for comment
#adding line for git ation test
#test 2
#updating code testing