from tkinter import *
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def animate(i):

    iss_api_url = "https://api.wheretheiss.at/v1/satellites/25544"

    try:
        response = requests.get(iss_api_url)
    except:
        #Too much api requests
        time.sleep(10)

    iss_data = response.json()

    iss_latitude = iss_data['latitude']
    iss_longitude = iss_data['longitude']
    iss_altitude = iss_data['altitude']
    iss_velocity = iss_data['velocity']

    print("Latitude: " + str(iss_latitude) + " Longitude: " + str(iss_longitude) + " Altitude: " + str(iss_altitude) + " Speed: " + str(iss_velocity))

    plt.plot(iss_longitude, iss_latitude, 'ro', markersize=1)

figure = plt.figure()
ani = animation.FuncAnimation(figure, animate, fargs=(), interval=1000)
plt.xlim([-150, 180])
plt.ylim([-80, 80])
plt.show()







