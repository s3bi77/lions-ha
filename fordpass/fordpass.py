import requests
import os
import time



# Parameters
fordpassuser = os.environ.get('fordpassuser')
fordpasspassword = os.environ.get('fordpasspassword')
fordpassvin = os.environ.get('fordpassvin')
mqtthost = os.environ.get('mqtthost')
mqttuser = os.environ.get('mqttuser')
mqttpassword = os.environ.get('mqttpassword')



def loop():
    while True:
        print("bluppstart")
        time.sleep(5)

if __name__ == '__main__':
    print("bluppstart")
    loop()
    print("bluppstop")