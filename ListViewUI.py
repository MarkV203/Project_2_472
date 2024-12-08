# Description: This file contains the code for the ListViewUI class.
# The ListViewUI class is responsible for creating a list view that displays sensor data.
# It was created in a class in case mutliple instances of the list view are needed.
# functionality to change the title may be implemented later

import tkinter as tk
from tkinter import ttk



class WildfireListUI:
    def __init__(self, num_sensors):
        self.num_sensors = num_sensors
        self.temp_entry_list = []
        self.humi_entry_list = []
        self.wind_entry_list = []
        self.create_list_view()
        
    @property
    def getTempList(self):
        return self.temp_entry_list
    
    @property
    def getHumiList(self):
        return self.humi_entry_list
    
    @property
    def getWindList(self):
        return self.wind_entry_list

    """
    The following code creates a list view for displaying sensor data. 
    The list view consists of four columns: ID, Temperature, Humidity, and Wind Speed
    Example:
    ID | Temperature (C) | Humidity | Wind Speed (m/s)
    1  | 75.0            | 25.0     | 15.0
    2  | 85.0            | 18.0     | 22.0
    3  | 78.0            | 21.0     | 19.0
    etc...

    The list view is created using the Tkinter library in Python.
    Each section is written as a separate frame to allow for better organization and layout.
    """
    
    def create_list_view(self):
        self.root = tk.Tk()
        self.root.title("Wildfire Monitoring List View")
        
        # Listview Frame
        self.List_View = tk.Frame(self.root, padx = 10, pady = 10)
        self.List_View.grid(row = 0, column = 0, sticky = "NSEW")

        # Configure grid weights to make the Listbox widgets resize with the window
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)
        self.List_View.grid_columnconfigure(1, weight = 1)
        self.List_View.grid_columnconfigure(2, weight = 1)
        self.List_View.grid_columnconfigure(3, weight = 1)
        
        self.createIDColumn()
        self.createTempColumn()
        self.createHumiColumn()
        self.createWindColumn()
        
        # self.root.mainloop()
        
    # id column
    def createIDColumn(self):
        id_frame = tk.Frame(self.List_View)
        id_frame.grid(row = 0, column = 0, sticky = "NSEW")
        id_title = tk.Label(id_frame, text = "ID", font = ("Arial", 14))
        id_title.grid(row = 0, column = 0, sticky = "W")
        id_label_list = []
        for label in range(1, self.num_sensors + 1):
            id_label_list.append(tk.Label(id_frame, text = f"{label}", font = ("Arial", 9)))
        for label in range(self.num_sensors):
            id_label_list[label].grid(row = label + 1, column = 0, sticky = "NSEW")

    # temperature column
    def createTempColumn(self):
        temp_frame = tk.Frame(self.List_View)
        temp_frame.grid(row = 0, column = 1, sticky = "NSEW")
        temp_frame.grid_columnconfigure(0, weight = 1)
        temp_title = tk.Label(temp_frame, text = "Temperature (C)", font = ("Arial", 14))
        temp_title.grid(row = 0, column = 0, sticky = "W")
        for _ in range(self.num_sensors):
            self.temp_entry_list.append(tk.Listbox(temp_frame, height = 1, font = ("Arial", 10)))
        for entry in range(self.num_sensors):
            self.temp_entry_list[entry].grid(row = entry + 1, column = 0, sticky = "EW")
        


    # humidity column
    def createHumiColumn(self):
        humi_frame = tk.Frame(self.List_View)
        humi_frame.grid(row = 0, column = 2, sticky = "NSEW")
        humi_frame.grid_columnconfigure(0, weight = 1)
        humi_title = tk.Label(humi_frame, text = "Humidity", font = ("Arial", 14))
        humi_title.grid(row = 0, column = 0, sticky = "W")
        for _ in range(self.num_sensors):
            self.humi_entry_list.append(tk.Listbox(humi_frame, height = 1, font = ("Arial", 10)))
        for entry in range(self.num_sensors):
            self.humi_entry_list[entry].grid(row = entry + 1, column = 0, sticky = "EW")


    # wind speed column
    def createWindColumn(self):
        wind_frame = tk.Frame(self.List_View)
        wind_frame.grid(row = 0, column = 3, sticky = "NSEW")
        wind_frame.grid_columnconfigure(0, weight = 1)
        wind_title = tk.Label(wind_frame, text = "Wind Speed (m/s)", font = ("Arial", 14))
        wind_title.grid(row = 0, column = 0, sticky = "W")
        for _ in range(self.num_sensors):
            self.wind_entry_list.append(tk.Listbox(wind_frame, height = 1, font = ("Arial", 10)))
        for entry in range(self.num_sensors):
            self.wind_entry_list[entry].grid(row = entry + 1, column = 0, sticky = "EW")


    '''
    This code will populate the list view with sample sensor data.
    from the weatherGeneration.py file.
    It will be sent from the main file
    '''
    def setData(self, sensor, data):
        self.temp_entry_list[sensor - 1].insert(0, data['Temperature'])
        self.humi_entry_list[sensor - 1].insert(0, data['Humidity'])
        self.wind_entry_list[sensor - 1].insert(0, data['Wind Speed'])

# Create an instance of WildfireListUI
