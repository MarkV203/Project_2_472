import time
import random
from datetime import datetime
# import matplotlib.pyplot as plt
import pandas as pd
import populateListView as plv
import ListViewUI as lv

class Sensor:
    def __init__(self, id, data_queue, temp = None, humi = None, wind = None):
        self._id = id
        self._data_queue = data_queue
        self._temp = temp
        self._humi = humi
        self._wind = wind

    # Getter for id
    @property
    def getid(self):
        return self._id

    # Getter for temperature
    @property
    def temp(self):
        return self._temp

    # Setter for temperature
    @temp.setter
    def temp(self, value):
        self._temp = value

    # Getter for humidity
    @property
    def humi(self):
        return self._humi

    # Setter for humidity
    @humi.setter
    def humi(self, value):
        self._humi = value

    # Getter for wind
    @property
    def wind(self):
        return self._wind

    # Setter for wind
    @wind.setter
    def wind(self, value):
        self._wind = value
        
    
    # Method to simulate weather data collection for sensors
    # The method also puts the data into a CSV file
    def weatherCollection(self):
        # Initialize an empty DataFrame to store the weather data
        weather_data = pd.DataFrame(columns=['Timestamp', 'Temperature', 'Humidity', 'Wind Speed'])


        for _ in range (0, 10):
            # Simulate weather conditions
            temperature = random.uniform(-10, 35)  # Random temperature between -10 and 35 degrees Celsius
            self._temp = temperature
            humidity = random.uniform(30, 100)     # Random humidity between 30% and 100%
            self._humi = humidity
            wind_speed = random.uniform(0, 20)     # Random wind speed between 0 and 20 m/s
            self._wind = wind_speed
            
            # Record the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Create a new row as a dictionary
            new_data = {'id': self._id, 'Timestamp': timestamp, 'Temperature': temperature, 'Humidity': humidity, 'Wind Speed': wind_speed}

            # Add the new row to the DataFrame using pd.concat
            weather_data = pd.concat([weather_data, pd.DataFrame([new_data])], ignore_index=True)

            # Print the current data
            print(f"Sensor {self._id}: {timestamp} - Temp: {temperature:.2f}°C, Humidity: {humidity:.2f}%, Wind Speed: {wind_speed:.2f} m/s")
            
            # Update the ListView with the new data
            #plv.populate(self._id, f"{temperature:.2f}", f"{humidity:.2f}", f"{wind_speed:.2f}")
            self._data_queue.put(new_data)
            
            # Sleep for 1 second
            time.sleep(1)

            # Optional: Save data to a CSV file periodically (e.g., every 10 seconds or after X records)
            if len(weather_data) % 10 == 0:
                weather_data.to_csv(f"weather_data_{self._id}.csv", index=False)

            
