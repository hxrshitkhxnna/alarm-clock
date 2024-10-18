import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to set the alarm
def set_alarm():
    alarm_time = alarm_entry.get()
    if alarm_time == "":
        messagebox.showerror("Error", "Please enter a time for the alarm!")
        return
    
    try:
        # Convert input to a datetime object for validation
        valid_time = datetime.strptime(alarm_time, "%H:%M:%S")
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        
        # Keep checking the time
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Wake up! Time's up!")
                break
            time.sleep(1)  # Delay to avoid excessive CPU usage
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time as HH:MM:SS")

# Create the GUI window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label for the alarm time
alarm_label = tk.Label(window, text="Enter alarm time (HH:MM:SS):")
alarm_label.pack(pady=10)

# Create an entry widget to input the alarm time
alarm_entry = tk.Entry(window, font=("Helvetica", 24))
alarm_entry.pack(pady=10)
# Create a button to set the alarm
set_button = tk.Button(window, text="Set Alarm", command=set_alarm, font=("Helvetica", 14), bg="green", fg="white")
set_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
