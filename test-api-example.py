import requests
from datetime import datetime
import time
import sys

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=vilnius&appid=c06a9eb2ed3be12a650fb8c322805625")
url_text = response.json()

loop_state = True
time_delay = 1
iteration = 1

def write_in_file(iteration, current_time, current_temp):
    file = open(r"C:\DOCS\Python mokymai\read-weather-data\export-data.txt","a")
    file.write(iteration + ','+ current_time + ',' + current_temp + "\n")
    file.close()
    return None

while loop_state:
    #Time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time:", current_time)

    #Temperature read
    current_temp = url_text['main']['temp']
    print('temperature:',current_temp)

    #convert into string to write data
    iteration = str(iteration)
    current_temp = str(current_temp)

    write_in_file(iteration, current_time, current_temp)

    iteration = int(iteration)
    iteration += 1
    time.sleep(time_delay)

# r.status_code
# r.headers
# r.encoding
# r.text
# r.json()
# test