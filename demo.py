#demo.py
import pyodide_http
import requests
from js import console

# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()

def get_tp_data():
    response = requests.get("https://reqres.in/api/users?page=2")
    return response.json()

def run_comparison(*ags, **kws):
    json_data = get_tp_data()

    #Do something interesting with the data
    print(f"The highest id is {max(item['id'] for item in json_data['data'])}")
    console.log(json_data['data'])
    response = Element("response")
    response.element.value = json_data['data']