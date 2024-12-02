import tkinter as tk
from tkinter import ttk
import random  # Simulate sensor data changes for demonstration
from datetime import datetime

class WildfireMonitoringUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wildfire Monitoring Dashboard")
        
        # Sample sensor data
        self.sensor_data = {
            "Sensor 1": {"temperature": 75.0, "humidity": 25.0, "wind_speed": 15.0, "soil_saturation": 35.6},
            "Sensor 2": {"temperature": 85.0, "humidity": 18.0, "wind_speed": 22.0, "soil_saturation": 40.2},
            "Sensor 3": {"temperature": 78.0, "humidity": 21.0, "wind_speed": 19.0, "soil_saturation": 25.0},
        }
        
        # Create Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)
        
        # Create Frames for each tab
        self.monitoring_tab = ttk.Frame(self.notebook)
        self.log_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.monitoring_tab, text="Monitoring")
        self.notebook.add(self.log_tab, text="Log")

        # Set up Monitoring Tab
        self.setup_monitoring_tab()

        # Set up Log Tab
        self.setup_log_tab()

        # Schedule periodic updates every 5 minutes (300,000 ms)
        self.schedule_data_update()

    def setup_monitoring_tab(self):
        # Frames within the Monitoring Tab
        self.selection_frame = ttk.Frame(self.monitoring_tab, padding="10")
        self.selection_frame.grid(row=0, column=0, sticky="EW")
        
        self.display_frame = ttk.Frame(self.monitoring_tab, padding="10")
        self.display_frame.grid(row=1, column=0, sticky="EW")
        
        # Current selected sensor
        self.selected_sensor = tk.StringVar(value="Sensor 1")
        
        # Create the dropdown and display section
        self.create_selection_section()
        self.create_display_section()
        self.update_display()

    def setup_log_tab(self):
        # Log display in the Log Tab
        self.log_display = tk.Text(self.log_tab, width=80, height=20, font=("Arial", 12))
        self.log_display.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)
        self.log_display.config(state=tk.DISABLED)

    def create_selection_section(self):
        ttk.Label(self.selection_frame, text="Select Sensor:").grid(row=0, column=0, sticky="W", padx=5)
        
        # Dropdown for selecting sensors
        sensor_menu = ttk.OptionMenu(
            self.selection_frame, 
            self.selected_sensor, 
            "Sensor 1", 
            *self.sensor_data.keys(), 
            command=self.update_display
        )
        sensor_menu.grid(row=0, column=1, sticky="W", padx=5)
    
    def create_display_section(self):
        self.display_label = tk.Text(self.display_frame, width=50, height=10, font=("Arial", 14))
        self.display_label.grid(row=0, column=0, sticky="W")
        self.display_label.config(state=tk.DISABLED)

    def update_display(self, event=None):
        # Fetch data for the selected sensor
        sensor_name = self.selected_sensor.get()
        data = self.sensor_data[sensor_name]

        # Enable text box for updating
        self.display_label.config(state=tk.NORMAL)
        self.display_label.delete(1.0, tk.END)

        # Add formatted display with color-coding
        self.add_colored_text("Sensor: {}\n".format(sensor_name), "black")
        self.add_colored_text("Temperature: {:.1f} °F\n".format(data["temperature"]), self.get_color(data["temperature"], [75, 80]))
        self.add_colored_text("Humidity: {:.1f} %\n".format(data["humidity"]), self.get_color(data["humidity"], [25, 20], reverse=True))
        self.add_colored_text("Wind Speed: {:.1f} mph\n".format(data["wind_speed"]), self.get_color(data["wind_speed"], [15, 20]))
        self.add_colored_text("Soil Saturation: {:.1f} %\n".format(data["soil_saturation"]), "black")  # No threshold for soil

        # Disable text box after updating
        self.display_label.config(state=tk.DISABLED)

    def add_colored_text(self, text, color):
        self.display_label.tag_configure(color, foreground=color)
        self.display_label.insert(tk.END, text, color)
    
    def get_color(self, value, thresholds, reverse=False):
        """
        Determine the color based on thresholds.
        :param value: Value to evaluate.
        :param thresholds: List [low, high] thresholds for yellow and red.
        :param reverse: If True, low values are dangerous (e.g., humidity).
        :return: Color as a string ("green", "yellow", or "red").
        """
        low, high = thresholds
        if reverse:
            if value < high:
                return "red"
            elif value < low:
                return "yellow"
            else:
                return "green"
        else:
            if value > high:
                return "red"
            elif value > low:
                return "yellow"
            else:
                return "green"

    def fetch_new_sensor_data(self):
        """
        Simulate fetching new data from sensors.
        Will need to feed the actual data through this eventually
        """
        for sensor in self.sensor_data:
            self.sensor_data[sensor]["temperature"] = random.uniform(70.0, 90.0)
            self.sensor_data[sensor]["humidity"] = random.uniform(15.0, 35.0)
            self.sensor_data[sensor]["wind_speed"] = random.uniform(10.0, 25.0)
            self.sensor_data[sensor]["soil_saturation"] = random.uniform(20.0, 50.0)
        self.log_new_data()

    def log_new_data(self):
        """
        Log the updated data for all sensors in the log tab.
        """
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, f"Update at {now}:\n")
        for sensor, data in self.sensor_data.items():
            log_entry = (
                f"{sensor}: Temp={data['temperature']:.1f}°F, "
                f"Humidity={data['humidity']:.1f}%, "
                f"Wind={data['wind_speed']:.1f} mph, "
                f"Soil={data['soil_saturation']:.1f}%\n"
            )
            self.log_display.insert(tk.END, log_entry)
        self.log_display.insert(tk.END, "\n")
        self.log_display.config(state=tk.DISABLED)

    def schedule_data_update(self):
        """
        Schedule periodic updates to fetch and display new sensor data
        """
        self.fetch_new_sensor_data()  # Fetch new data
        self.update_display()        # Update display for the currently selected sensor
        # Schedule the next update in 5 minutes (300,000 ms)
        self.root.after(30000, self.schedule_data_update)

if __name__ == "__main__":
    root = tk.Tk()
    app = WildfireMonitoringUI(root)
    root.mainloop()
