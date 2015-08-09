import requests

def get_data():
    response = requests.get('http://httpbin.org/get')
    return response.status_code

print get_data()