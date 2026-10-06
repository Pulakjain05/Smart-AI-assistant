import tkinter as tk
from tkinter import messagebox


# -----------------------------
# AI-VISION SAFETY DASHBOARD
# Member 4 - Safety & Wearable
# -----------------------------

SAFE_DISTANCE = 150
DANGER_DISTANCE = 80


def check_distance():
    try:
        distance = float(distance_entry.get())

        if distance < 0:
            messagebox.showerror("Error", "Distance cannot be negative.")
            return

        distance_value.config(text=f"{distance:.1f} cm")

        if distance <= DANGER_DISTANCE:
            status_value.config(text="DANGER", fg="red")
            warning_value.config(
                text="⚠️ Obstacle is very close!"
            )
            vibration_value.config(
                text="ON 📳", fg="red"
            )

        elif distance <= SAFE_DISTANCE:
            status_value.config(text="WARNING", fg="orange")
            warning_value.config(
                text="⚠️ Obstacle detected nearby."
            )
            vibration_value.config(
                text="OFF", fg="orange"
            )

        else:
            status_value.config(text="SAFE", fg="green")
            warning_value.config(
                text="✅ Path is clear."
            )
            vibration_value.config(
                text="OFF", fg="green"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid distance in cm."
        )


def activate_sos():
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

    messagebox.showwarning(
        "SOS ALERT",
        "Emergency alert triggered!\n\n"
        "Location sharing can be connected later."
    )


def reset_system():
    distance_entry.delete(0, tk.END)

    distance_value.config(
        text="-- cm"
    )

    status_value.config(
        text="READY",
        fg="blue"
    )

    warning_value.config(
        text="No obstacle detected."
    )

    vibration_value.config(
        text="OFF",
        fg="green"
    )


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()

window.title("AI-VISION Safety System")
window.geometry("700x600")


title = tk.Label(
    window,
    text="AI-VISION SAFETY SYSTEM",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


subtitle = tk.Label(
    window,
    text="Member 4 - Safety & Wearable Module",
    font=("Arial", 14)
)

subtitle.pack(pady=5)


# Distance input

distance_label = tk.Label(
    window,
    text="Enter Obstacle Distance (cm)",
    font=("Arial", 15)
)

distance_label.pack(pady=(30, 5))


distance_entry = tk.Entry(
    window,
    font=("Arial", 16),
    width=15,
    justify="center"
)

distance_entry.pack()


check_button = tk.Button(
    window,
    text="CHECK DISTANCE",
    font=("Arial", 13, "bold"),
    command=check_distance
)

check_button.pack(pady=15)


# Distance display

distance_value = tk.Label(
    window,
    text="-- cm",
    font=("Arial", 20, "bold")
)

distance_value.pack(pady=5)


# Status

status_title = tk.Label(
    window,
    text="SYSTEM STATUS",
    font=("Arial", 14, "bold")
)

status_title.pack(pady=(20, 5))


status_value = tk.Label(
    window,
    text="READY",
    font=("Arial", 22, "bold"),
    fg="blue"
)

status_value.pack()


# Warning

warning_value = tk.Label(
    window,
    text="No obstacle detected.",
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
    font=("Arial", 20, "bold"),
    fg="green"
)

vibration_value.pack(pady=5)


# SOS button

sos_button = tk.Button(
    window,
    text="🚨 SOS / EMERGENCY",
    font=("Arial", 16, "bold"),
    command=activate_sos
)

sos_button.pack(pady=25)


# Reset button

reset_button = tk.Button(
    window,
    text="RESET SYSTEM",
    font=("Arial", 12),
    command=reset_system
)

reset_button.pack()


window.mainloop()