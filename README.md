# IoT Animatronic Greeting Robot

This project is an IoT-enabled Animatronic Greeting Robot sponsored by the IEDC of St. Joseph's College, Devagiri. The robot is designed to interact dynamically with users, creating an engaging experience by greeting, animating expressions, and allowing interaction through its body screen.

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

### Videos
Phase 1:
- **Planning 📝**:
  ![asd](https://github.com/iDhanush/IoT_Animatronics_Robot_V1/raw/refs/heads/master/assets/WhatsApp%20Video%202024-12-26%20at%2010.52.33%20PM.mp4)
- **Robot in Action**:
  ![Robot in Action](videos/robot_in_action.mp4)

---

## Showcase
This project demonstrates the integration of IoT with animatronics to create a functional and interactive robotic greeter. It showcases:
- The use of proximity sensors for detecting user presence.
- The synchronization of visual animations with physical movements.
- A seamless interaction between hardware and software components.

---

## Future Improvements
- Add more expressive animations and voice options.
- Enable multi-language support for greetings and interactions.
- Integrate advanced AI for personalized user interactions.

---

## Acknowledgments
Special thanks to the IEDC of St. Joseph's College, Devagiri, for sponsoring this project and supporting innovation.

