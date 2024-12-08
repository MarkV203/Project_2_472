# Project_2_472

## Goal of the Project
This project aims to accurately assess different sensor data to find the chances of a fire occurring in wildlife.

### Objective
The primary objective of this project is to develop a robust **Wildfire Monitoring Dashboard** capable of:
- Simulating real-time environmental data from multiple sensors, updating at specified intervals.
- Identifying and flagging abnormal conditions that indicate a higher likelihood of wildfire occurrence.
- Providing an intuitive graphical user interface (GUI) to monitor sensor data and visualize fire risk.

## Key Features
- **Multi-threaded simulation**: Each sensor operates independently, updating data at fixed intervals.
- **Thread safety with mutex locks**: Prevents data corruption during concurrent access to shared resources.
- **Real-time logging**: Displays historical sensor data for accountability and trend analysis.
- **Color-coded alerts**: Visual indicators for normal, warning, and critical conditions, aiding rapid decision-making.

---

## Significance of the Project

### Meaningfulness
- Wildfires pose a severe threat to ecosystems, human settlements, and climate stability. Early detection is vital.
- By simulating a wildfire monitoring system, this project showcases how such systems could integrate with IoT technologies to mitigate disasters.

### Novelty
- Unlike typical simulation dashboards, this project emphasizes concurrent operations (via multithreading) while maintaining data integrity using mutex locking.
- The system mimics real-world challenges, such as sensor delays and overlapping data access, offering a practical approach to solving these issues.
- Provides a modular design where more sensors or real data sources can be added seamlessly in the future.

---

## Installation and Instructions to Use 

### Installation

#### Prerequisites
- Python 3.8 or higher.
- Tkinter library (pre-installed with Python on most systems).

#### Steps
1. Download the `main.py`, `populateListView.py`,`ListViewUI.py`, and `weatherGeneration.py` files into the same directory.
2. Launch the program by running `main.py`, and the Wildfire Dashboard should appear.

---

## Structure of the Code
The base of each file is called by `main.py` which begins by creating an instance of `populateListView.py` and then creating a given number of threads.
Each thread calls `weatherGeneration.py` to simulate each sensor collecting data and stores that data in a queue and in a csv document. 
The `populateListView.py` then calls `ListViewUI.py` and begins to fill it with the queued data. 

### Code Structure Diagram:

### Detailed Explanation:
#### `main.py`
- Handles multithreading for periodic sensor updates (1, 2, and 3-minute intervals).
- Employs mutex locking (`sensor_lock`) to ensure thread-safe operations on `sensor_data`.

#### `ui.py`
- Defines the `WildfireMonitoringUI` class, including:
  - Monitoring tab for real-time data visualization.
  - Log tab for recording and reviewing sensor updates.
  - Helper methods for data display, color-coded alerts, and threshold checks.
 
#### `populateListView.py`
 - Defines the `ListViewApp` class:
    - creates the initial queue that will store values on the UI
    - creates and instance of `list_view`
    - populates each `list_view` by sending the data to `ListViewUI.py`

#### `ListViewUI.py`
 - Defines the `WildfireListUI`
   - Organises the view in a grid that will place more rows depening on how many sensors are declared
   - Sets the data received by `populateListView.py`
#### `weatherGeneration.py`
  - Defines the `Sensor` class:
     - Each instance of `Sensor` keeps track of its ID, data_queue, temperature, humidity, and wind speed
     - Randomly generates an initial state and then iterates it slightly each loop
     - sends the data to a csv file and the data queue that is used by `populateListView.py`

### UI Integration
- The `update_display` method dynamically refreshes the monitoring tab.

---

## Functionalities and Test Results

### Functionalities
#### Multithreaded Sensor Simulation:
- Each sensor updates at a fixed interval (1, 2, or 3 minutes), running independently.
- Mutex locking ensures that shared data (`sensor_data`) remains consistent during concurrent updates.

#### Real-Time Monitoring:
- Displays sensor data with color-coded alerts for quick status evaluation:
  - **Green**: Normal.
  - **Yellow**: Warning (close to thresholds).
  - **Red**: Critical (fire likely).

#### Historical Logging:
- Records every sensor update with a timestamp in the log tab for auditing purposes.

#### User Interaction:
- Dropdown menu for selecting sensors.
- Automatic refresh of displayed data in sync with sensor updates.

### Test Results
- Concurrent updates for all three sensors completed without data corruption.
- Fire likelihood detection accurately flagged abnormal conditions (e.g., high temperature, low humidity).
- The system maintained smooth UI performance even with multiple threads running simultaneously.
- all csv documents attached to this repo are an example of how sensor data is shown. Each runtime of the program will result in an updated csv document

---

## Project Goals/Achievements 

### Results
- The dashboard successfully displays live sensor data and detects fire risks based on thresholds.
- Multi-threaded architecture ensures seamless and independent operation of each sensor.
- Real-time logging provides a transparent record of system operations.

### Demonstration
Simulated scenarios:
- High temperature and low humidity led to a "Fire Likely" alert.
- Normal conditions displayed as "Fire Unlikely."
- Sensor data updates occurred exactly at the defined intervals, with no overlaps or skipped updates.

---

## Discussion and Conclusions 

### Project Challenges
- Managing concurrent threads without causing race conditions was a significant challenge.
- Balancing the responsiveness of the GUI while running background threads required careful design.

### Limitations
- The current system relies on simulated data, which may not fully replicate real-world conditions.
- Adding more sensors or reducing intervals could strain the single-threaded Tkinter UI.

### Applications of Course Learning
- **Multithreading and Mutex Locks**: Applied to ensure thread-safe data sharing in a concurrent environment.
- **Software Design Principles**: Separation of concerns between UI and backend logic enhances maintainability.
- **Data Visualization**: Developed a dynamic, color-coded dashboard for user-friendly monitoring.

### Future Improvements
- Integrate actual IoT sensors for live data collection.
- Implement a database for long-term storage and advanced analytics.
- Upgrade the GUI framework to a more modern alternative (e.g., PyQt or Kivy) for enhanced scalability.
