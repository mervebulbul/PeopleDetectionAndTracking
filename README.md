
# Drone-Based Human Tracking 

This project was developed to perform real-time human tracking using a drone with the YOLOv8 deep learning model. The images captured by the drone camera are processed to detect the person, and the drone is directed to follow the detected individual.

## Purpose
In this project, the YOLOv8 model is used to detect humans in images captured by a drone camera, and tracking algorithms are applied based on the person's position. This enables the drone to automatically follow the detected individual.

## Use Cases
- **Security:** Drones can patrol large areas, monitor people, and track them. For instance, in the event of a security breach, the drone can continuously follow the target individual.
- **Search and Rescue:** It can be used to detect and track missing or endangered individuals in rescue operations.
- **Filmmaking:** Drones that automatically follow a moving target can be useful in capturing dynamic footage.
- **Sports Events:** Aerial footage can be captured by tracking athletes in real-time during sports events.
- **Autonomous Drones:** Can be used to enable drones to independently track specific objects or individuals.



  
## Technologies Used

**YOLOv8:** Used for human detection and classification.

**OpenCV:** Used for image processing and handling video streams.

**Python:** The entire application is developed using Python.
## Installation

1. Clone the project:

```bash 
    git clone https://github.com/mervebulbul/PeopleDetectionAndTracking.git
    cd PeopleDetectionAndTracking
```    
2. Install the OpenCV

```bash 
    pip install opencv-python
```
3. Install the ultralytics module to load the YOLOv8 model:
```bash 
    pip install ultralytics
```
4. Start the video stream from the drone camera and run the tracking algorithm:
```bash 
    python drone_human_tracking.py
```
## Usage

This project processes real-time video streams from the drone camera to detect humans. Once a person is detected, their position relative to the drone camera is determined, and directional commands such as *"go left,""go right," and "go up"* are generated. Note: The actual implementation of drone control commands is not included in this project; it focuses solely on detection and tracking.

  
## Example GIF
The following GIFs demonstrate human tracking:

![alt text](2humantracking.gif)
## Development

This project is optimized for real-time human tracking but can be adapted for different tracking scenarios. If you'd like to add new features or integrate actual drone control commands, feel free to fork the repository and modify the code as needed.

  