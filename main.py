import threading
import random
from time import sleep
import tkinter as tk
from ui import WildfireMonitoringUI

# Mutex lock for sensor data updates
sensor_lock = threading.Lock()

# Simulate sensor updates
def update_sensors(ui):
    flagged_sensors = set()  # Track sensors with abnormal values

    while True:
        with sensor_lock:
            for sensor in ui.sensor_data:
                if sensor in flagged_sensors:
                    # Skip updates for flagged sensors
                    continue

                # Simulate new sensor readings
                ui.sensor_data[sensor]["temperature"] = random.uniform(70.0, 90.0)
                ui.sensor_data[sensor]["humidity"] = random.uniform(15.0, 35.0)
                ui.sensor_data[sensor]["wind_speed"] = random.uniform(10.0, 25.0)
                ui.sensor_data[sensor]["soil_saturation"] = random.uniform(20.0, 50.0)

                # Check for abnormal values
                if (
                    ui.sensor_data[sensor]["temperature"] > 85.0 or
                    ui.sensor_data[sensor]["humidity"] < 20.0 or
                    ui.sensor_data[sensor]["wind_speed"] > 22.0 or
                    ui.sensor_data[sensor]["soil_saturation"] < 25.0
                ):
                    flagged_sensors.add(sensor)

            # Log the updated data
            ui.log_new_data(ui.sensor_data)

        # Recheck flagged sensors periodically
        for sensor in list(flagged_sensors):
            with sensor_lock:
                if (
                    ui.sensor_data[sensor]["temperature"] <= 85.0 and
                    ui.sensor_data[sensor]["humidity"] >= 20.0 and
                    ui.sensor_data[sensor]["wind_speed"] <= 22.0 and
                    ui.sensor_data[sensor]["soil_saturation"] >= 25.0
                ):
                    flagged_sensors.remove(sensor)
        sleep(5)  # Periodic updates

if __name__ == "__main__":
    root = tk.Tk()
    app = WildfireMonitoringUI(root)

    # Start sensor update thread
    sensor_thread = threading.Thread(target=update_sensors, args=(app,), daemon=True)
    sensor_thread.start()

    root.mainloop()
