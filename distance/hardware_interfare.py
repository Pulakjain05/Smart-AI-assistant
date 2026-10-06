# hardware_interface.py

# -------------------------------
# SIMULATED HARDWARE INTERFACE
# -------------------------------

def read_distance():
    """
    Simulates distance sensor reading.
    Later this function will read from
    the real Raspberry Pi sensor.
    """
    distance = float(input("Enter distance in cm: "))
    return distance


def vibration_on():
    print("🔴 VIBRATION MOTOR: ON")


def vibration_off():
    print("🟢 VIBRATION MOTOR: OFF")


def read_sos_button():
    """
    Simulates SOS button.
    Enter y for YES, n for NO.
    """
    choice = input("Press SOS button? (y/n): ").lower()

    if choice == "y":
        return True

    return False 
    print("AI-VISION HARDWARE INTERFACE")
print("----------------------------")

distance = read_distance()
print("Distance:", distance, "cm")

if distance <= 20:
    vibration_on()
else:
    vibration_off()

if read_sos_button():
    print("🚨 SOS ACTIVATED!")
else:
    print("SOS: OFF")