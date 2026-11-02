# Raspberry Pi Hardware Module

This module handles ultrasonic distance measurement and Bluetooth communication with the ESP32 SmartBand.

## Hardware
- Raspberry Pi 4 Model B
- HC-SR04 Ultrasonic Sensor
- ESP32 SmartBand
- Jumper wires and voltage divider resistors

## Project Files

- `raspberry_pi.py` – Main program for distance measurement and Bluetooth communication.
- `config.py` – Stores GPIO pins, distance threshold and Bluetooth settings.
- `requirements.txt` – Lists required Python libraries.

## GPIO Connections

| HC-SR04 | Raspberry Pi 4 |
|---|---|
| VCC | 5V (Pin 2) |
| GND | GND (Pin 6) |
| TRIG | GPIO23 (Pin 16) |
| ECHO | GPIO24 (Pin 18), through voltage divider |

## Bluetooth Communication

The Raspberry Pi communicates with the ESP32 using Bluetooth Classic (RFCOMM).

ESP32 device name: `ESP32_SmartBand`

Commands:
- `VIBRATE` – Turns the vibration motor ON.
- `STOP` – Turns the vibration motor OFF.

## Distance Alert

The default warning distance is 80 cm.

- Object closer than 80 cm: send `VIBRATE`.
- Object at or beyond 80 cm: send `STOP`.

## Setup on Raspberry Pi

Install the required library:

```bash
sudo apt update
sudo apt install python3-gpiozero
```

Pair and connect the ESP32 using Bluetooth before running the main program.

Run:

```bash
python3 raspberry_pi.py
```

**Note:** The ESP32 Bluetooth MAC address must be configured in `raspberry_pi.py` before running. Hardware testing and Bluetooth pairing are still pending.