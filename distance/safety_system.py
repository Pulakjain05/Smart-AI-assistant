
# AI-VISION SAFETY SYSTEM
# Simulated safety logic for the wearable assistant

SAFE_DISTANCE = 150       # cm
DANGER_DISTANCE = 80      # cm


def check_obstacle(distance):
    """Classify the distance and simulate a safety response."""

    if distance < 0:
        print("Invalid distance. Please enter a non-negative value.")
        return "INVALID"

    print(f"\nDistance detected: {distance:.1f} cm")

    if distance <= DANGER_DISTANCE:
        print("DANGER: Obstacle is very close!")
        
        return "DANGER"

    elif distance <= SAFE_DISTANCE:
        print("WARNING: Obstacle detected nearby.")
        return "WARNING"

    else:
        print("SAFE: Path is clear.")
        return "SAFE"


def vibration_alert():
    """Simulate a vibration motor alert in the terminal."""
    print("VIBRATION MOTOR: ON (simulation)")
    print("VIBRATION MOTOR: OFF (simulation)")


def sos_alert():
    """Simulate an SOS emergency alert."""
    print("\nSOS BUTTON ACTIVATED!")
    print("Emergency assistance required.")
    print("Location sharing is not connected yet.")


def get_distance_response(distance):
    """Convert a distance into a spoken safety message."""

    status = check_obstacle(distance)

    if status == "DANGER":
        return (
            f"Danger! An obstacle is only {distance:.0f} "
            "centimetres away. Please be careful."
        )

    elif status == "WARNING":
        return (
            f"Warning. An obstacle is approximately "
            f"{distance:.0f} centimetres away."
        )

    elif status == "SAFE":
        return "The simulated sensor indicates the path is clear."

    return "Sorry, the distance reading is invalid."


def main():
    print("================================")
    print(" AI-VISION SAFETY SYSTEM")
    print(" Distance module test")
    print("================================")

    while True:
        print("\n1. Enter obstacle distance")
        print("2. Activate SOS")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                distance = float(input("Enter distance in cm: "))
                check_obstacle(distance)
            except ValueError:
                print("Invalid input. Enter a number, such as 75.")

        elif choice == "2":
            sos_alert()

        elif choice == "3":
            print("Safety system test ended.")
            break

        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
