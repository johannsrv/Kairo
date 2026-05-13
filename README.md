# 🤖 Kaido Robot

**Kaido** is a robot designed to serve tables in restaurants, offering an interactive and autonomous experience for both customers and staff.

> **🚧 Simulation-only project** – This robot is a concept developed in Autodesk Inventor for simulation purposes only. No physical hardware is intended.

## 🎯 Robot Objective

- **Main objective** → Provide customer service in restaurants. 🍽️
- **Verbal interaction** → Ability to communicate with diners using natural language. 🗣️
- **Autonomous movement** → Navigate through the restaurant, avoiding customers and obstacles. 🚶‍♂️📦
- **Route planning** → Calculate optimal paths to deliver dishes to each table. 🗺️

## ⚙️ Technical Requirements (Onboard)

- **Camera** → Object and human recognition. 📷
- **LiDAR** → Create map and generate navigation routes. 📡
- **Wheels** → Locomotion system. 🛞

## 🖥️ Simulation Environment (Gazebo + ROS 2)

The entire robot behavior is simulated in **Gazebo** using a custom model designed in **Autodesk Inventor** (conceptual design, not for real construction). The simulation includes:

- **Virtual camera** → Publishes image streams to a ROS topic. A Computer Vision node detects objects and humans inside the simulated world.
- **Virtual LiDAR** → Provides laser scans for SLAM and navigation.
- **Real microphone & speakers** → Your PC's microphone captures customer voice; speakers play the robot's responses. These real I/O devices are integrated via ROS nodes that communicate with the simulation.
- **Interactive testing** → You can speak to the robot while watching it move in Gazebo, and the robot will answer using an LLM.

This setup allows you to develop and showcase the complete system (perception, navigation, conversational AI) without physical hardware.

## 🧩 System Services

### ✅ Onboard Services (running locally on Kaido)

| Service | Description | Status |
|---------|-------------|--------|
| 🗺️ **SLAM** | Simultaneous Localization and Mapping: builds the restaurant map and locates the robot within it. | 🟢 Planned |
<!-- | 🧭 **Route Planning** | Calculates optimal paths to serve dishes, avoiding customers and dynamic obstacles. | 🟢 Planned |
| 🛞 **Local Motion Control** | Low-level wheel control for navigation and obstacle avoidance. | 🟢 Planned |
| 🎙️ **Voice Interface** | Microphone capture and speaker playback (local audio processing). Actual PC mic/speakers are used via ROS. | 🟢 Planned | -->

<!-- ### ☁️ External Services (cloud / future)

| Service | Description | Status | Repository |
|---------|-------------|--------|-------------|
| 🧠 **LLM Service** | Enables natural conversation with customers using a Large Language Model. | 🟢 Planned | `[Link when available]` |
| 👁️ **Computer Vision Service** | Object and human recognition (diners, tables, obstacles) from the simulated camera feed. | 🟢 Planned | `[Link when available]` |
| 🚦 **Motion Control Service (Go)** | Limits movement area, assigns table numbers or working zones. | 🟢 Planned | `[Link when available]` |
| 🎮 **Manual/Auto Control (Go)** | Allows switching between remote manual control and autonomous mode. | 🟢 Planned | `[Link when available]` |
| 🏠 **Docking Service (Go)** | Command to return to the charging station or resting zone when not in service. | 🟢 Planned | `[Link when available]` | -->

> **Status legend**  
> 🟢 Planned – Not started yet  
> 🟡 In development – Active work  
> ✅ Completed – Ready for integration  
> ⏳ Future – Defined for later phases

## 🏗️ System Architecture (Simulation-based)

*Diagram coming soon – will show how Gazebo, ROS nodes, real mic/speakers, and cloud services interact.*