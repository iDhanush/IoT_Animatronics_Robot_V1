# Iot Animatronic Greeting Robot

This project is an Iot enabled Animatronic Greeting Robot sponsored by the IEDC of St. Joseph's College, Devagiri. The robot is designed to interact dynamically with users, creating an engaging experience by greeting, animating expressions, and allowing interaction through its body screen.

---

## Features

### Greeting and Interaction
- **Proximity-Based Greeting**: The robot detects users using an ultrasonic proximity sensor and greets them through a speaker.
- **Facial Expressions**: The robot's face, represented by a tablet, displays animated eyes that change based on the user's actions.
- **Interactive Body Screen**: An interactive screen on the robot's body allows users to interact. While interacting, the robot's face animation changes to look down at the screen.
- **Dynamic Movements**: The robot waves its hands and moves its ears dynamically.

### Hardware Components
1. **Ultrasonic Proximity Sensor**: Detects users approaching the robot.
2. **Tablet (Face)**: Displays animated eyes and plays audio for voice interactions.
3. **Interactive Screen (Body)**: Serves as a touch interface for user interaction.
4. **Arduino Boards**:
   - **Arduino 1**: Streams distance data from the ultrasonic proximity sensor to a laptop.
   - **Arduino 2**: Controls the waving hands and moving ears.

---

## System Architecture

### Central Server
A laptop acts as the server, facilitating communication between components:
- **Tablet**: Receives commands for eye animations and voice playback.
- **Interactive Screen**: Monitors user interaction and updates animations accordingly.
- **Second Arduino**: Controls the robot's mechanical movements (hands and ears).

### Communication Flow
1. **Ultrasonic Sensor**: Sends distance data to the server via the first Arduino.
2. **Server**: Processes the data and:
   - Updates the tablet with appropriate animations and audio.
   - Sends interaction data to the interactive screen.
   - Commands the second Arduino to control movements.

---

## Software Components

### Programming Languages
- **Arduino IDE**: For programming the Arduino boards.
- **Python**: For server-side communication and control logic.

### Dependencies
- Libraries for ultrasonic sensor communication.
- Libraries for controlling animations and handling interactions on the tablet and screen.
- Communication protocols for Arduino and server synchronization (e.g., Serial or MQTT).

---

## Setup Instructions

### Hardware Setup
1. Assemble the robot with the following components:
   - Mount the tablet as the face.
   - Connect the ultrasonic proximity sensor to Arduino 1.
   - Connect the motors for hands and ears to Arduino 2.
   - Attach the interactive screen to the body.
2. Ensure all components are powered and connected to the central server (laptop).

### Software Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/robot-greeter.git
   cd robot-greeter
   ```
2. Upload the respective Arduino sketches to Arduino 1 and Arduino 2 using the Arduino IDE.
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server script:
   ```bash
   python server.py
   ```

---

## Usage
1. Power on the robot and start the server.
2. Approach the robot to trigger the proximity sensor.
3. Interact with the robot through its screen and observe its dynamic responses.
4. Enjoy the engaging experience of a responsive and animated robotic greeter!

---

## Future Improvements
- Add more expressive animations and voice options.
- Enable multi-language support for greetings and interactions.
- Integrate advanced AI for personalized user interactions.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
Special thanks to the IEDC of St. Joseph's College, Devagiri, for sponsoring this project and supporting innovation.

