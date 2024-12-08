# Description: This file is used to populate the list view with data from the sensors. It creates a queue to hold the data from the threads, opens the list view, starts the threads to generate data, and updates the list view with data from the queue.

import threading
import queue
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import weatherGeneration as wg
import ListViewUI as lv
import pandas as pd


class ListViewApp:
    def __init__(self, num_sensors):
        # Create a queue to hold the data from the threads
        self.data_queue = queue.Queue()
        
        # Open the list view
        self.list_view = lv.WildfireListUI(num_sensors)
        
        # Start the threads to generate data
        self.populate(num_sensors)
        
        # Start updating the list view with data from the queue
        self.list_view.root.after(1000, self.update_list_view)
    
    

    def populate(self, num_sensors):
        for i in range(num_sensors):
            sensor = wg.Sensor(i + 1, self.data_queue)
            threading.Thread(target=sensor.weatherCollection, daemon=True).start() 
            # Mark threads as daemon

    def update_list_view(self):
        while not self.data_queue.empty():
            data = self.data_queue.get_nowait()
            self.list_view.setData(data['id'], data)
        self.list_view.root.after(1000, self.update_list_view)

