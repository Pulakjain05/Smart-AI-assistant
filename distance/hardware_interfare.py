
# distance/hardware_interface.py
# Simulated hardware interface for the AI-VISION project.

from distance.safety_system import check_obstacle, sos_alert


def read_distance():
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
    print("VIBRATION MOTOR: ON (simulation)")


def vibration_off():
    print("VIBRATION MOTOR: OFF (simulation)")


def main():
    print("================================")
    print(" AI-VISION HARDWARE INTERFACE")
    print("================================")

    while True:
        print("\n1. Check obstacle distance")
        print("2. Activate SOS")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            distance = read_distance()

            if distance is None:
                continue

            status = check_obstacle(distance)

            if status == "DANGER":
                vibration_on()
            else:
                vibration_off()

        elif choice == "2":
            sos_alert()

        elif choice == "3":
            print("Hardware interface test ended.")
            break

        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
