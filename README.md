# Wildfire Monitoring Dashboard

## Project Overview
This project is focused on accurately assessing environmental sensor data to evaluate the likelihood of wildfire occurrences. The **Wildfire Monitoring Dashboard** integrates real-time data simulation, multithreading, and intuitive user interfaces to provide an effective monitoring tool.

---

## Objectives
### Primary Goals
- Simulate real-time environmental data from multiple sensors, updating at specified intervals.
- Identify and flag abnormal conditions that indicate a higher likelihood of wildfire occurrence.
- Provide an intuitive graphical user interface (GUI) for monitoring sensor data and visualizing fire risk.

### Key Features
- **Multi-threaded simulation**: Independent operation of sensors updating at fixed intervals.
- **Thread safety with mutex locks**: Ensures data integrity during concurrent access.
- **Real-time logging**: Historical data storage for trend analysis and accountability.
- **Color-coded alerts**: Quick visual indicators for normal, warning, and critical conditions.

---

## Significance of the Project
### Importance
- Wildfires are a significant threat to ecosystems, human settlements, and climate stability. Early detection can save lives and resources.
- The project demonstrates how IoT technologies can integrate to mitigate disasters effectively.

### Novel Contributions
- Concurrent operations with multithreading ensure realistic simulation scenarios.
- Mutex locking addresses real-world challenges like sensor delays and overlapping data access.
- Modular design allows seamless addition of sensors or integration with real data sources.

---

## Installation and Usage
### Prerequisites
- Python 3.8 or higher.
- Tkinter library (pre-installed with Python on most systems).

### Installation Steps
1. Download the files: `main.py`, `populateListView.py`, `ListViewUI.py`, and `weatherGeneration.py`.
2. Place all files in the same directory.
3. Run the program using:
   ```bash
   python main.py
   ```
   The Wildfire Dashboard will appear.

---

## Code Structure
The program’s execution begins with `main.py`, which initializes multithreading and orchestrates data flow between other components.

### Core Modules
#### `main.py`
- Manages sensor threads that update data at intervals (1, 2, and 3 minutes).
- Employs mutex locks (`sensor_lock`) for thread-safe operations.

#### `populateListView.py`
- Defines the `ListViewApp` class:
  - Creates a queue for storing sensor data.
  - Instantiates and populates `list_view` objects with queued data.

#### `ListViewUI.py`
- Defines the `WildfireListUI` class:
  - Organizes sensor data into a grid layout.
  - Dynamically updates the display with incoming data.

#### `weatherGeneration.py`
- Defines the `Sensor` class:
  - Simulates sensor data, including temperature, humidity, and wind speed.
  - Randomly generates initial conditions and updates data iteratively.
  - Sends data to both a CSV file and a shared queue.

### Data Flow Diagram
> Diagram placeholder for illustrating sensor data generation, processing, and display.

---

## Functionalities and Test Results
### Key Functionalities
#### Multithreaded Sensor Simulation
- Sensors operate independently, updating data at fixed intervals.
- Mutex locks ensure consistent and conflict-free data updates.

#### Real-Time Monitoring
- Color-coded alerts for rapid evaluation:
  - **Green**: Normal.
  - **Yellow**: Warning.
  - **Red**: Critical.

#### Historical Logging
- Logs sensor updates with timestamps for review and auditing.

#### User Interaction
- Dropdown menu for selecting sensors.
- Automatic synchronization of displayed data with sensor updates.

### Test Outcomes
- Concurrent sensor updates completed without data corruption.
- Accurate detection and flagging of fire-prone conditions.
- Smooth GUI performance with multiple threads.
- Example CSV files demonstrate recorded sensor data for each runtime.

---

## Project Achievements
### Results
- Successfully displayed live sensor data and detected fire risks using predefined thresholds.
- Maintained seamless operation of multi-threaded sensors.
- Provided a transparent system with real-time logging capabilities.

### Demonstrations
Video Presentation Link: https://youtu.be/ZSt13-u6up4

Simulated scenarios:
- High temperature and low humidity triggered "Fire Likely" alerts.
- Normal conditions displayed as "Fire Unlikely."
- Sensor data updated precisely at defined intervals.

---

## Challenges, Limitations, and Future Improvements
### Challenges
- Ensuring thread safety and preventing race conditions in a concurrent environment.
- Maintaining UI responsiveness alongside background thread operations.

### Limitations
- Relies on simulated data, which may not reflect real-world conditions.
- Adding more sensors or reducing update intervals may strain the Tkinter UI.

### Future Improvements
- Integrate live IoT sensors for real-world data collection.
- Implement a database for long-term storage and analysis.
- Upgrade the GUI framework (e.g., PyQt or Kivy) for better scalability and performance.

---

## Conclusion
The **Wildfire Monitoring Dashboard** effectively demonstrates a simulation-based approach to wildfire risk assessment. By leveraging multithreading, real-time data visualization, and intuitive design, it offers insights into how IoT technologies can aid in early disaster detection and prevention.

