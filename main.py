import serial
import time
import threading

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

robot_distance = 225.99
robot_close_distance = 70
interation_status = False

# Lock for thread synchronization
distance_lock = threading.Lock()


def calculate_emotion():
    if interation_status:
        return "lookDown"
    elif robot_distance < robot_close_distance:
        return "sayHI"
    else:
        return "idle"


def serial_updater():
    global robot_distance
    ser = None

    # Try connecting to available COM ports
    for i in range(9):  # Search from COM0 to COM8
        try:
            ser = serial.Serial(f'COM{i}', 9600, timeout=1)
            print(f"Connected to {ser.port}")
            break  # Exit loop if connection is successful
        except serial.SerialException:
            continue

    if ser is None:
        raise Exception("Serial Port not found")

    time.sleep(2)  # Wait for the connection to stabilize

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(f"Received: {line}")
                if line.startswith("--distance:"):
                    try:
                        distance = float(line.split(":")[-1])

                        with distance_lock:  # Use lock when updating shared variable
                            robot_distance = distance

                        emotion = calculate_emotion()

                        # Send command based on emotion
                        if emotion == "sayHI":
                            ser.write("sayHI\n".encode())
                        elif emotion == "lookDown":
                            ser.write("LookDown\n".encode())

                        print(f"Updated serial_out: {robot_distance} - {emotion}")

                    except ValueError:
                        print("Error parsing distance from serial data.")
                else:
                    print("Unknown serial message format.")

    except KeyboardInterrupt:
        print("Exiting...")

    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
        with distance_lock:
            robot_distance = 250.99  # Fallback distance on error

    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial connection closed.")


serial_thread = threading.Thread(target=serial_updater)
serial_thread.daemon = True
serial_thread.start()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": 'hello world'}


@app.get("/head_status")
async def head_screen():
    emotion = calculate_emotion()
    return {'distance': robot_distance, 'emotion': emotion}


@app.get("/body_update")
async def body_update(interacting: bool):
    global interation_status
    interation_status = interacting
    return {'status': 'updated'}


uvicorn.run(app, host="localhost", port=8000)

# ngrok http --domain=kangaroo-tops-coral.ngrok-free.app 8000
