# Project_2_472

Goal of the Project:
  This project aims to accurately assess different sensor data to find the different chances of a fire occuring in wildlife.
  Objective: The primary objective of this project is to develop a robust Wildfire Monitoring Dashboard capable of:
  
  -  Simulating real-time environmental data from multiple sensors, updating at specified intervals.
    
  -  Identifying and flagging abnormal conditions that indicate a higher likelihood of wildfire occurrence.
    
  -  Providing an intuitive graphical user interface (GUI) to monitor sensor data and visualize fire risk.

Key Features:
  - Multi-threaded simulation: Each sensor operates independently, updating data at fixed intervals.
  - Thread safety with mutex locks: Prevents data corruption during concurrent access to shared resources.
  - Real-time logging: Displays historical sensor data for accountability and trend analysis.
  - Color-coded alerts: Visual indicators for normal, warning, and critical conditions, aiding rapid decision-making.

Significance of the Project:

  Meaningfulness:
    -  Wildfires pose a severe threat to ecosystems, human settlements, and climate stability. Early detection is vital.
    -  By simulating a wildfire monitoring system, this project showcases how such systems could integrate with IoT technologies to mitigate disasters.
  
  Novelty:
    -  Unlike typical simulation dashboards, this project emphasizes concurrent operations (via multithreading) while maintaining data integrity using mutex locking.
    -  The system mimics real-world challenges, such as sensor delays and overlapping data access, offering a practical approach to solving these issues.
    -  Provides a modular design where more sensors or real data sources can be added seamlessly in the future.

Installation and Instructions to Use 
Installation:
Prerequisites:
Python 3.8 or higher.
Tkinter library (pre-installed with Python on most systems).
Steps:
Download the main.py and ui.py files into the same directory.
Launch the program by running main.py, and the Wildfire Dashboard should appear
Structure of the Code :
  Code Structure Diagram:

    bash
    Copy code
    Wildfire Monitoring System
    main.py                  # Entry point; handles threading and sensor updates
    ui.py                    # GUI implementation and sensor data visualization
    Detailed Explanation:

main.py:
-  Handles multithreading for periodic sensor updates (1, 2, and 3-minute intervals).
-  Employs mutex locking (sensor_lock) to ensure thread-safe operations on sensor_data.
ui.py:
-  Defines the WildfireMonitoringUI class, including:
-  Monitoring tab for real-time data visualization.
-  Log tab for recording and reviewing sensor updates.
-  Helper methods for data display, color-coded alerts, and threshold checks.
UI Integration:
-  The update_display method dynamically refreshes the monitoring tab based on user selection.
Functionalities and Test Results:
  Functionalities:
    Multithreaded Sensor Simulation:
      -  Each sensor updates at a fixed interval (1, 2, or 3 minutes), running independently.
      -  Mutex locking ensures that shared data (sensor_data) remains consistent during concurrent updates.
    Real-Time Monitoring:
      Displays sensor data with color-coded alerts for quick status evaluation:
        -  Green: Normal.
        -  Yellow: Warning (close to thresholds).
        -  Red: Critical (fire likely).
    Historical Logging:
      -  Records every sensor update with a timestamp in the log tab for auditing purposes.
    User Interaction:
      -  Dropdown menu for selecting sensors.
      -  Automatic refresh of displayed data in sync with sensor updates.
  Test Results:
    -  Concurrent updates for all three sensors completed without data corruption.
    -  Fire likelihood detection accurately flagged abnormal conditions (e.g., high temperature, low humidity).
    -  The system maintained smooth UI performance even with multiple threads running simultaneously.
Project Goals/Achievements 
  Results:
    -  The dashboard successfully displays live sensor data and detects fire risks based on thresholds.
    -  Multi-threaded architecture ensures seamless and independent operation of each sensor.
    -  Real-time logging provides a transparent record of system operations.
  Demonstration:
    Simulated scenarios:
      -  High temperature and low humidity led to a "Fire Likely" alert.
      -  Normal conditions displayed as "Fire Unlikely."
    -  Sensor data updates occurred exactly at the defined intervals, with no overlaps or skipped updates.
Discussion and Conclusions 
Project Challenges:
    -  Managing concurrent threads without causing race conditions was a significant challenge.
    -  Balancing the responsiveness of the GUI while running background threads required careful design.
  Limitations:
    -  The current system relies on simulated data, which may not fully replicate real-world conditions.
    -  Adding more sensors or reducing intervals could strain the single-threaded tkinter UI.
  Applications of Course Learning:
  -  Multithreading and Mutex Locks: Applied to ensure thread-safe data sharing in a concurrent environment.
  -  Software Design Principles: Separation of concerns between UI and backend logic enhances maintainability.
  -  Data Visualization: Developed a dynamic, color-coded dashboard for user-friendly monitoring.
  Future Improvements:
  -  Integrate actual IoT sensors for live data collection.
  -  Implement a database for long-term storage and advanced analytics.
  -  Upgrade the GUI framework to a more modern alternative (e.g., PyQt or Kivy) for enhanced scalability.
