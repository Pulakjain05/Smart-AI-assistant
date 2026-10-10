
# distance/hardware_interface.py
# Simulated hardware interface
# Real sensor and vibration motor are not connected yet.

def read_distance():
    """Simulate a distance sensor reading."""
    try:
        distance = float(input("Enter distance in cm: "))

        if distance < 0:
            print("Invalid distance. Enter a non-negative value.")
            return None

        return distance

    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def vibration_on():
    """Simulate turning the vibration motor on."""
    print("VIBRATION MOTOR: ON (simulation)")


def vibration_off():
    """Simulate turning the vibration motor off."""
    print("VIBRATION MOTOR: OFF (simulation)")


def read_sos_button():
    """Simulate an SOS button."""
    choice = input("Press SOS button? (y/n): ").strip().lower()
    return choice == "y"


def main():
    print("AI-VISION HARDWARE INTERFACE")
    print("----------------------------")

    distance = read_distance()

    if distance is not None:
        print(f"Distance: {distance:.1f} cm")

        # Temporary test threshold; not the final safety logic.
        if distance <= 20:
            vibration_on()
        else:
            vibration_off()

    if read_sos_button():
        print("SOS ACTIVATED! (simulation)")
    else:
        print("SOS: OFF")


if __name__ == "__main__":
    main()
