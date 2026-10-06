import time

# -----------------------------
# AI-VISION SAFETY MODULE
# Member 4
# -----------------------------

SAFE_DISTANCE = 150      # cm
DANGER_DISTANCE = 80     # cm


def check_obstacle(distance):
    print(f"\nDistance detected: {distance} cm")

    if distance <= DANGER_DISTANCE:
        print("⚠️ DANGER! Obstacle is very close.")
        vibration_alert()

    elif distance <= SAFE_DISTANCE:
        print("⚠️ WARNING! Obstacle detected nearby.")

    else:
        print("✅ Path is clear.")


def vibration_alert():
    print("📳 VIBRATION MOTOR: ON")
    time.sleep(1)
    print("📳 VIBRATION MOTOR: OFF")


def sos_alert():
    print("\n🚨 SOS BUTTON ACTIVATED!")
    print("🚨 EMERGENCY ALERT TRIGGERED!")
    print("📍 Location sharing can be connected later.")
    print("📢 Emergency assistance required.")


def main():

    print("================================")
    print(" AI-VISION SAFETY SYSTEM")
    print(" Member 4 - Safety Module")
    print("================================")

    while True:

        print("\nChoose an option:")
        print("1. Enter obstacle distance")
        print("2. Activate SOS")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            try:
                distance = float(
                    input("Enter distance in cm: ")
                )

                check_obstacle(distance)

            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":

            sos_alert()

        elif choice == "3":

            print("Safety system stopped.")
            break

        else:

            print("❌ Invalid choice.")


if __name__ == "__main__":
    main() 
    from hardware_interface import  (
        read_distance,
        vibration_on,
        vibration_off,
        read_sos_button
    ) 
    def main():
        check_safety(distance)

    if distance > 150:
        print("✅ SAFE")
        vibration_off()

    elif distance > 80:
        print("⚠️ WARNING: Obstacle is getting closer.")
        vibration_off()

    else:
        print("🚨 DANGER: Obstacle is very close!")
        vibration_on() 
        distance = read_distance()

check_safety(distance)

if read_sos_button():
    print("🚨 SOS ALERT ACTIVATED!")
    print("Emergency assistance required.")