import requests
import time

def ifttt(name, value1, value2, key):
    payload = { 'value1' : value1, 'value2' : value2}
    requests.post("https://maker.ifttt.com/trigger/%s/with/key/%s"%(name, key), data=payload)

folder = raw_input("Name of folder: ")
number = int(raw_input("How many images?"))
key = raw_input("Enter Key: ")
for i in range(number):
    print i
    ifttt("randomimage", i, folder, key)
    time.sleep(3)
