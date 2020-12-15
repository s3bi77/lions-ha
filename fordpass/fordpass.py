import requests
import os



# Parameters
fordpassuser = os.environ.get('fordpassuser')
fordpasspassword = os.environ.get('fordpasspassword')
fordpassvin = os.environ.get('fordpassvin')
mqtthost = os.environ.get('mqtthost')
mqttuser = os.environ.get('mqttuser')
mqttpassword = os.environ.get('mqttpassword')



def do_something():
    while True:
        print("bluppstart")
        time.sleep(5)

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == '__main__':
    print("bluppstart")
    run()
    print("bluppstop")