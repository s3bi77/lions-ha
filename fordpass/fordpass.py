import requests
import os


# Parameters
fordpassuser = os.environ.get('fordpassuser')
fordpasspassword = os.environ.get('fordpasspassword')
fordpassvin = os.environ.get('fordpassvin')
mqtthost = os.environ.get('mqtthost')
mqttuser = os.environ.get('mqttuser')
mqttpassword = os.environ.get('mqttpassword')




if __name__ == '__main__':
    print(fordpassuser)