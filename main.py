import time
import serial
import uvicorn
import threading
from fastapi import FastAPI
from serial.win32 import ClearCommError

robot_distance = 225.99
robot_close_distance = 30


def serial_updater():
    global robot_distance

    ser = False
    for i in range(0, 7):
        try:
            ser = serial.Serial(f'COM{i}', 9600, timeout=1)
        except:
            pass
    if not ser:
        raise Exception("Serial Port not found")
    time.sleep(2)

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                distance = float(line.split(":")[-1])
                robot_distance = distance
                if distance < robot_close_distance:
                    emotion = "sayhi"
                else:
                    emotion = "idle"
                print(f"Updated serial_out: {robot_distance} - {emotion}")

    except KeyboardInterrupt:
        print("Exiting...")
    except ClearCommError:
        robot_distance = 250.99
    finally:
        ser.close()


serial_thread = threading.Thread(target=serial_updater)
serial_thread.daemon = True
serial_thread.start()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": 'hello world'}


@app.get("/emotion")
async def calculate_emotion():
    if robot_distance < robot_close_distance:
        emotion = "sayhi"
    else:
        emotion = "idle"
    return {'distance': robot_distance, 'emotion': emotion}


uvicorn.run(app, host="localhost", port=8000)
