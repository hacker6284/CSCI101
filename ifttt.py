import requests

def ifttt(name, value1, value2, value3, key):
    payload = "{ 'value1' : 'hello', 'value2' : 'hello', 'value3' : 'hello'}"
    requests.post("https://maker.ifttt.com/trigger/%s/with/key/%s"%(name, key), data=payload)
