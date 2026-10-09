import tkinter as tk
from tkinter import messagebox
import random
from distance.safety_system import check_obstacle
# ---------------------------------
# AI-VISION AUTOMATIC SENSOR SIMULATOR
# Member 4 - Safety & Wearable
# ---------------------------------

SAFE_DISTANCE = 150
DANGER_DISTANCE = 80

running = False

# Simulated vibration modes
vibration_mode = "SAFE"
vibration_phase = False


def get_sensor_distance():
    """
    Simulates a distance sensor.
    Later this function will be replaced
    with the real Raspberry Pi sensor.
    """

    return random.randint(30, 220)

def update_vibration_display():
    """Simulate continuous and intermittent vibration patterns."""
    global vibration_phase

    if vibration_mode == "DANGER":
        # Continuous vibration for a very close obstacle
        vibration_value.config(
            text="ON - CONTINUOUS (simulated)",
            fg="red"
        )

    elif vibration_mode == "WARNING":
        # Intermittent vibration for a nearby obstacle
        vibration_phase = not vibration_phase

        if vibration_phase:
            vibration_value.config(
                text="ON - PULSE (simulated)",
                fg="orange"
            )
        else:
            vibration_value.config(
                text="OFF - PULSE (simulated)",
                fg="orange"
            )

    elif vibration_mode == "SOS":
        # Flashing simulated emergency pattern
        vibration_phase = not vibration_phase
        vibration_value.config(
            text="SOS - ALERT ON" if vibration_phase
            else "SOS - ALERT OFF",
            fg="red"
        )

    else:
        vibration_value.config(
            text="OFF",
            fg="green"
        )

    window.after(300, update_vibration_display)

def update_sensor():
    global running, vibration_mode

    if not running:
        return

    # Get simulated sensor value
    distance = get_sensor_distance()

    distance_value.config(text=f"{distance} cm")

    # Use the shared safety logic
    safety_status = check_obstacle(distance)

    # Update the dashboard based on the result
    if safety_status == "DANGER":
        vibration_mode = "DANGER"
        status_value.config(text="DANGER", fg="red")
        warning_value.config(text="OBSTACLE VERY CLOSE!")


    elif safety_status == "WARNING":
        vibration_mode = "WARNING"
        status_value.config(text="WARNING", fg="orange")
        warning_value.config(text="OBSTACLE DETECTED NEARBY")

    elif safety_status == "SAFE":
        vibration_mode = "SAFE"
        status_value.config(text="SAFE", fg="green")
        warning_value.config(text="PATH IS CLEAR")


    # Update every second
    window.after(1000, update_sensor)


def start_sensor():

    global running

    if not running:

        running = True

        start_button.config(
            text="SENSOR RUNNING"
        )

        update_sensor()


def stop_sensor():

    global running, vibration_mode
    vibration_mode = "SAFE"

    running = False

    start_button.config(
        text="START SENSOR"
    )

    status_value.config(
        text="STOPPED",
        fg="blue"
    )

    warning_value.config(
        text="Sensor simulation stopped."
    )

    vibration_value.config(
        text="OFF",
        fg="green"
    )


def activate_sos():
    global vibration_mode
    vibration_mode = "SOS"
    messagebox.showwarning(
        "SOS ALERT",
        "Emergency alert triggered!\n\n"
        "Location sharing can be connected later."
    )

    status_value.config(
        text="EMERGENCY",
        fg="red"
    )

    warning_value.config(
        text="🚨 SOS ACTIVATED!"
    )

    vibration_value.config(
        text="ALERT 📳",
        fg="red"
    )


# ---------------------------------
# MAIN WINDOW
# ---------------------------------

window = tk.Tk()

window.title("AI-VISION Automatic Safety Sensor")

window.geometry("700x650")


title = tk.Label(
    window,
    text="AI-VISION SAFETY SYSTEM",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


subtitle = tk.Label(
    window,
    text="Member 4 - Automatic Sensor Simulation",
    font=("Arial", 14)
)

subtitle.pack()


# Distance

distance_title = tk.Label(
    window,
    text="SIMULATED DISTANCE",
    font=("Arial", 15, "bold")
)

distance_title.pack(pady=(35, 5))


distance_value = tk.Label(
    window,
    text="-- cm",
    font=("Arial", 30, "bold")
)

distance_value.pack()


# Status

status_title = tk.Label(
    window,
    text="SYSTEM STATUS",
    font=("Arial", 14, "bold")
)

status_title.pack(pady=(30, 5))


status_value = tk.Label(
    window,
    text="READY",
    font=("Arial", 25, "bold"),
    fg="blue"
)

status_value.pack()


# Warning

warning_value = tk.Label(
    window,
    text="Start the sensor simulation.",
    font=("Arial", 15)
)

warning_value.pack(pady=20)


# Vibration

vibration_title = tk.Label(
    window,
    text="VIBRATION MOTOR",
    font=("Arial", 14, "bold")
)

vibration_title.pack()


vibration_value = tk.Label(
    window,
    text="OFF",
    font=("Arial", 22, "bold"),
    fg="green"
)

vibration_value.pack(pady=5)


# Start

start_button = tk.Button(
    window,
    text="START SENSOR",
    font=("Arial", 15, "bold"),
    command=start_sensor
)

start_button.pack(pady=20)


# Stop

stop_button = tk.Button(
    window,
    text="STOP SENSOR",
    font=("Arial", 13),
    command=stop_sensor
)

stop_button.pack()


# SOS

sos_button = tk.Button(
    window,
    text="🚨 SOS / EMERGENCY",
    font=("Arial", 16, "bold"),
    command=activate_sos
)

sos_button.pack(pady=25)

window.after(300, update_vibration_display)
window.mainloop()
