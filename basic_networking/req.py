import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code==200:
    print('Response received successfully!')
    print('Response content:',response.json())
else:
    print('Failed to receive response. Status code:',response.status_code)
    