import time
import socket

from gpiozero import DistanceSensor

from config import (
    TRIG_PIN,
    ECHO_PIN,
    WARNING_DISTANCE,
    MAX_DISTANCE,
    BLUETOOTH_PORT
)

# Create ultrasonic sensor
sensor = DistanceSensor(
    echo=ECHO_PIN,
    trigger=TRIG_PIN,
    max_distance=MAX_DISTANCE
)

# ESP32 Bluetooth MAC address
ESP32_MAC = "REPLACE_WITH_ESP32_MAC_ADDRESS"

# Create Bluetooth socket
bt_socket = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM
)

last_command = None

try:
    print("Connecting to ESP32 SmartBand...")

    bt_socket.connect((ESP32_MAC, BLUETOOTH_PORT))

    print("Bluetooth connected successfully!")

    while True:
        # Read distance in centimetres
        distance = sensor.distance * MAX_DISTANCE * 100

        print(f"Distance: {distance:.2f} cm")

        # Decide vibration command
        if distance < WARNING_DISTANCE:
            command = "VIBRATE"
        else:
            command = "STOP"

        # Send only when command changes
        if command != last_command:
            bt_socket.sendall((command + "\n").encode())
            print("Command sent:", command)
            last_command = command

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

except OSError as error:
    print("Bluetooth or sensor error:", error)

finally:
    try:
        bt_socket.sendall(b"STOP\n")
        bt_socket.close()
    except OSError:
        pass

    sensor.close()
    print("Program closed.")