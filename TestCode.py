import serial
import time

# Replace '/dev/ttyUSB0' with your Arduino's serial port
arduino_port = '/dev/ttyUSB0'
baud_rate = 9600

# Initialize serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the connection to establish

# List of PWM-capable pins to cycle through (3, 5, 6, 9)
pwm_pins = [3, 5, 6, 9]

try:
    while True:
        # Loop through each pin in the pwm_pins list
        for pwm_pin in pwm_pins:
            # Ramp up PWM value over 4 seconds
            for pwm_value in range(0, 256):  # Ramp from 0 to 255
                ser.write(f"{pwm_pin} {pwm_value}\n".encode())  # Send as bytes
                time.sleep(4 / 256)  # Wait 4 seconds divided by 256 steps
'''
                # Read response from Arduino
                if ser.in_waiting > 0:
                    response = ser.readline().decode('utf-8').rstrip()  # Read the response
                    print(f'Response from Arduino: {response}')
'''
            # Ramp down PWM value over 4 seconds
            for pwm_value in range(255, -1, -1):  # Ramp from 255 to 0
                ser.write(f"{pwm_pin} {pwm_value}\n".encode())  # Send as bytes
                time.sleep(4 / 256)  # Wait 4 seconds divided by 256 steps
'''
                # Read response from Arduino
                if ser.in_waiting > 0:
                    response = ser.readline().decode('utf-8').rstrip()  # Read the response
                    print(f'Response from Arduino: {response}')
'''
        # No need for a pause, as the next pin will immediately start ramping up

except KeyboardInterrupt:
    print("Exiting program")

finally:
    ser.close()  # Close the serial connection when done
