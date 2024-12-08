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


        # Simulate weather conditions
        temperature = round(random.uniform(-10, 35), 2)  # Random temperature between -10 and 35 degrees Celsius
        humidity = round(random.uniform(30, 100), 2)     # Random humidity between 30% and 100%
        wind_speed = round(random.uniform(0, 20), 2)     # Random wind speed between 0 and 20 m/s
        
        # save current data for possible use
        self._temp = temperature
        self._humi = humidity
        self._wind = wind_speed
    
        # Record the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for _ in range (0, 20):
            

            # Create a new row as a dictionary
            new_data = {'id': self._id, 'Timestamp': timestamp, 'Temperature': self._temp, 'Humidity': self._humi, 'Wind Speed': self._wind}

            # Add the new row to the DataFrame using pd.concat
            weather_data = pd.concat([weather_data, pd.DataFrame([new_data])], ignore_index=True)

            # Print the current data
            print(f"Sensor {self._id}: {timestamp} - Temp: {self._temp:.2f}°C, Humidity: {self._humi:.2f}%, Wind Speed: {self._wind:.2f} m/s")
            
            # Update the ListView with the new data
            #plv.populate(self._id, f"{temperature:.2f}", f"{humidity:.2f}", f"{wind_speed:.2f}")
            self._data_queue.put(new_data)
            
            # Sleep for 1 second
            time.sleep(1)

            # Optional: Save data to a CSV file periodically (e.g., every 10 seconds or after X records)
            if len(weather_data) % 10 == 0:
                weather_data.to_csv(f"weather_data_{self._id}.csv", index=False)
                
             # Randomly increment or decrement the values by 1, rounded to two decimals
            self._temp = round(self._temp + random.choice([-1, 1, -1.03, 0.2, 0, 0, 0, 0]), 2)
            self._humi = round(self._humi + random.choice([-1, 1, -1.03, 0.2, 0, 0, 0, 0]), 2)
            self._wind = round(self._wind + random.choice([-1, 1, -1.03, 0.2, 0, 0, 0, 0]), 2)

            # Clamp the values to ensure they stay within the expected range
            self._temp = max(-10, min(self._temp, 35))
            self._humi = max(30, min(self._humi, 100))
            self._wind = max(0, min(self._wind, 20))

            # Record the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            
