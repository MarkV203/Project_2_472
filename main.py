import threading
import queue
import tkinter as tk
from tkinter import messagebox
import weatherGeneration as wg
import ListViewUI as lv

class LoginScreen:
    def __init__(self, on_success_callback):
        """
        Initialize the login screen.
        :param on_success_callback: A function to call upon successful login.
        """
        self.on_success_callback = on_success_callback
        self.root = tk.Tk()
        self.root.title("Login")

        # Login Frame
        self.login_frame = tk.Frame(self.root, padx=20, pady=20)
        self.login_frame.pack()

        # Username Label and Entry
        tk.Label(self.login_frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, sticky="W")
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password Label and Entry
        tk.Label(self.login_frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, sticky="W")
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Login Button
        self.login_button = tk.Button(
            self.login_frame, text="Login", font=("Arial", 12), command=self.validate_login
        )
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def validate_login(self):
        """
        Validate the entered username and password.
        If correct, call the success callback.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Placeholder credentials (replace with secure checks for production)
        if username == "admin" and password == "password123":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.root.destroy()  # Close the login window
            self.on_success_callback()  # Call the success callback
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def run(self):
        """Run the login screen."""
        self.root.mainloop()


class ListViewAppWithLogin:
    def __init__(self, num_sensors):
        self.num_sensors = num_sensors
        self.data_queue = None
        self.list_view = None

        # Start with the login screen
        self.start_login()

    def start_login(self):
        """Initialize and show the login screen."""
        login_screen = LoginScreen(self.start_list_view)
        login_screen.run()

    def start_list_view(self):
        """Start the sensor data UI after successful login."""
        self.data_queue = queue.Queue()
        self.list_view = lv.WildfireListUI(self.num_sensors)
        self.populate(self.num_sensors)
        self.list_view.root.after(1000, self.update_list_view)
        self.list_view.root.mainloop()

    def populate(self, num_sensors):
        for i in range(num_sensors):
            sensor = wg.Sensor(i + 1, self.data_queue)
            threading.Thread(target=sensor.weatherCollection, daemon=True).start()

    def update_list_view(self):
        while not self.data_queue.empty():
            data = self.data_queue.get_nowait()
            self.list_view.setData(data['id'], data)
        self.list_view.root.after(1000, self.update_list_view)


if __name__ == "__main__":
    num_sensors = 5  # Number of sensors
    app = ListViewAppWithLogin(num_sensors)
