import numpy as np
import requests as rq
print('project 2')
print(np.abs(-2))
response = rq.get('https://jsonplaceholder.typicode.com/users')
print(response.json())