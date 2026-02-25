# Person Learning Mock System (ROS 2)

A modular **ROS 2** system simulating a person interaction pipeline for a service robot.

This project demonstrates:

- Perception  
- Tracking  
- Speech recognition  
- Task planning  

All implemented as separate ROS 2 nodes communicating via topics.

---

# System Overview

This mock system contains the following nodes:

- **vision_node** — Simulates person detection  
- **person_tracker** — Tracks detected person  
- **asr_node** — Simulates speech recognition  
- **task_planner** — Handles interaction logic  
- **dialogue_manager** — Publishes greeting trigger  

---

# Node Architecture

## Vision Node

**Publishes:**

```
person_detections (std_msgs/String)
```

**Behavior:**
- Simulates detecting a person every 5 seconds.

---

## Person Tracker

**Subscribes to:**

```
person_detections
```

**Publishes:**

```
tracked_person
```

**Behavior:**
- Simulates tracking and estimating person position.

---

## ASR Node

**Publishes:**

```
speech_text
```

**Behavior:**
- Simulates speech recognition every 10 seconds.

---

## Task Planner

**Subscribes to:**

```
tracked_person
intent
```

**Publishes:**

```
start_dialogue
```

**Behavior:**
- When a person is tracked → publishes `"greet_person"`
- When an intent is received → logs the intent

This node acts as the interaction coordinator of the system.

---

# Package Structure

```
person_learning_mock/
├── task_planner.py
├── vision_node.py
├── person_tracker.py
├── asr_node.py
├── dialogue_manager.py
├── setup.py
├── package.xml
```

---

# Setup & Running Instructions

## 1. Add Console Entry Point

Ensure the following exists inside `setup.py`:

```python
entry_points={
    'console_scripts': [
        'task_planner = person_learning_mock.task_planner:main',
    ],
},
```

---

## 2. Build the Workspace

From your workspace root:

```bash
cd ~/Documents/GILTEST_ws
colcon build --symlink-install
```

---

## 3. Source ROS 2 and Workspace

```bash
# Source ROS 2
source /opt/ros/humble/setup.bash

# Source your workspace
source install/setup.bash
```

Tip: Add both lines to `~/.bashrc` to auto-source in new terminals.

---

# Running the System

Each node should run in a separate terminal.

## Recommended Launch Order

1. Run `task_planner`
2. Run all other nodes except `asr_node` and `vision_node`
3. Finally run:
   - `vision_node`
   - `asr_node`

---

## Run a Node

```bash
ros2 run person_learning_mock task_planner
```

Repeat the command for each node.

---

# Useful ROS 2 Commands

## List all topics

```bash
ros2 topic list
```

## Echo a topic

```bash
ros2 topic echo tracked_person
```

## Rebuild After Changes

```bash
colcon build --symlink-install
source install/setup.bash
ros2 run person_learning_mock task_planner
```

---

# Topic Flow Diagram

```
vision_node
    ↓
person_detections
    ↓
person_tracker
    ↓
tracked_person
    ↓
task_planner
    ↓
start_dialogue
```

ASR runs in parallel and publishes speech text.

---

# Requirements

- Python 3.10+
- ROS 2 Humble
- rclpy
- std_msgs

---

# Notes

- This is a mock system for development and testing.
- Messages use `std_msgs/String` for simplicity.
- Can be extended with real perception, ASR, and intent classification modules.