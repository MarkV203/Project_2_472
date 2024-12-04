import tkinter as tk
from tkinter import ttk
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
        """
        Update the display with color-coded sensor values and fire likelihood.
        """
        # Fetch data for the selected sensor
        sensor_name = self.selected_sensor.get()
        data = self.sensor_data[sensor_name]

        # Enable the display label for editing
        self.display_label.config(state=tk.NORMAL)
        self.display_label.delete(1.0, tk.END)

        # Add color-coded information for each sensor value
        self.add_colored_text(f"Sensor: {sensor_name}\n", "black")
        temp_color = self.get_color(data["temperature"], thresholds=[75, 80])
        self.add_colored_text(f"Temperature: {data['temperature']:.1f} °F\n", temp_color)
        humidity_color = self.get_color(data["humidity"], thresholds=[25, 20], reverse=True)
        self.add_colored_text(f"Humidity: {data['humidity']:.1f} %\n", humidity_color)
        wind_color = self.get_color(data["wind_speed"], thresholds=[15, 20])
        self.add_colored_text(f"Wind Speed: {data['wind_speed']:.1f} mph\n", wind_color)
        soil_color = self.get_color(data["soil_saturation"], thresholds=[30, 40])
        self.add_colored_text(f"Soil Saturation: {data['soil_saturation']:.1f} %\n", soil_color)

        # Fire likelihood message
        fire_likelihood = "Fire Likely." if "red" in [temp_color, humidity_color, wind_color, soil_color] else "Fire Unlikely."
        self.add_colored_text(f"\n{fire_likelihood}\n", "green" if "Unlikely" in fire_likelihood else "red")

        # Disable editing after updates
        self.display_label.config(state=tk.DISABLED)

    def add_colored_text(self, text, color):
        self.display_label.tag_configure(color, foreground=color)
        self.display_label.insert(tk.END, text, color)

    def get_color(self, value, thresholds, reverse=False):
        """
        Determine the color based on thresholds
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

    def log_new_data(self, sensor_data):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, f"Update at {now}:\n")
        for sensor, data in sensor_data.items():
            log_entry = (
                f"{sensor}: Temp={data['temperature']:.1f}°F, "
                f"Humidity={data['humidity']:.1f}%, "
                f"Wind={data['wind_speed']:.1f} mph, "
                f"Soil={data['soil_saturation']:.1f}%\n"
            )
            self.log_display.insert(tk.END, log_entry)
        self.log_display.insert(tk.END, "\n")
        self.log_display.config(state=tk.DISABLED)
