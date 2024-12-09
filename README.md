# ShoeAndBallDetectionROS

This is the project for Embodied Intelligence subject, it is part of a bigger project MechanumBot, the code uses YOLOV8 for detecting shoes and balls (will be extended later) using ROS subscriber/publisher architecture

Prerequisites:
 * Ubuntu 20.04 Focal Fossa (https://releases.ubuntu.com/20.04/)
 * ROS 2 foxy (https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
 ----------------------------------------------------------------------------------------------------------------------------
Installation:
 YOLOv8 via the ultralytics pip package for the latest stable release 
 (open new terminal)
 >> pip install ultralytics
 ----------------------------------------------------------------------------------------------------------------------------
To build:
   To build this package, you either need a ROS 2 workspace or create a new one. Here is the instructions to create a new ROS 2 workspace, build the package.
    (open new terminal)
 >> mkdir -p ~/ros2_ws/src </br>
 >> cd  ~/ros2_ws/src

copy or clone the package to src folder & go back to workspace directory & do colcon build
>>cd  ~/ros2_ws
>> colcon build

Set up your environment by sourcing the following file.

>> source install/setup.bash
------------------------------------------------------------------------------------------------------------------------------
To run your package:

>> ros2 launch thing_detector thing_detection.py

------------------------------------------------------------------------------------------------------------------------------




