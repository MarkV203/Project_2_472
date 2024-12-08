import threading
import random
import time
import tkinter as tk
from ui import WildfireMonitoringUI
import weatherGeneration as wg
import populateListView as plv

# test for sensor data with threading
thread_count = 5
Data_Sensors = []
Displays_Lists = []

app = plv.ListViewApp(thread_count)

for i in range(thread_count):
    # create the sensor object for each thread
    sensor = wg.Sensor(i + 1, app.data_queue)
    ds = threading.Thread(target=sensor.weatherCollection)
    ds.start()
    Data_Sensors.append(ds)

if __name__ == "__main__":

    app.list_view.root.mainloop()
    
for threads in Data_Sensors:
    threads.join()

# Mutex lock for sensor data updates
# sensor_lock = threading.Lock()

# def update_sensor(sensor_name, ui, interval):
#     """
#     Thread function to update a specific sensor at a given interval.
#     :param sensor_name: Name of the sensor to update.
#     :param ui: WildfireMonitoringUI instance.
#     :param interval: Time in seconds between updates.
#     """
#     while True:
#         with sensor_lock:
#             # Simulate new sensor readings
#             ui.sensor_data[sensor_name]["temperature"] = random.uniform(70.0, 90.0)
#             ui.sensor_data[sensor_name]["humidity"] = random.uniform(15.0, 35.0)
#             ui.sensor_data[sensor_name]["wind_speed"] = random.uniform(10.0, 25.0)
#             ui.sensor_data[sensor_name]["soil_saturation"] = random.uniform(20.0, 50.0)

#             # Log the updated data
#             ui.log_new_data({sensor_name: ui.sensor_data[sensor_name]})

#         time.sleep(interval)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WildfireMonitoringUI(root)

#     # Define sensor update intervals (in seconds)
#     sensor_intervals = {
#         "Sensor 1": 60,  # 1 minute
#         "Sensor 2": 120, # 2 minutes
#         "Sensor 3": 180, # 3 minutes
#     }

#     # Start a thread for each sensor
#     for sensor_name, interval in sensor_intervals.items():
#         sensor_thread = threading.Thread(target=update_sensor, args=(sensor_name, app, interval), daemon=True)
#         sensor_thread.start()

#     root.mainloop()
