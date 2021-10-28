# ros-simulation
Robotic Programming using Gazebo Simulation


You must be using ROS Kinetic with Ubuntu 16.04

To install ROS Kinetic

-- ROS Source and Key Setup
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt-get update

-- Step 2: Installation
Note: If you are using a different Distribute of ROS, you must change the “kinetic” to your   distribution name.

sudo apt-get install ros-kinetic-desktop-full

-- Step 3: Environment Setup
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/kinetic/setup.bash

-- Step 4: Environment Setup and Initialize Rosdep

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update

-- Step 5: Installing Gazebo and Rviz Simulator

sudo apt-get install ros-kinetic-turtlebot ros-kinetic-turtlebot-apps ros-kinetic-turtlebot-interactions ros-kinetic-turtlebot-simulator ros-kinetic-kobuki-ftdi ros-kinetic-ar-track-alvar-msgs

-- Step 6: Updating Gazebo

sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install gazebo7


Launching Gazebo Simulation 

-- Step 1: Launching Gazebo Simulator with the Turtlebot

roslaunch turtlebot_gazebo turtlebot_world.launch

-- Step 2: Setting Up the Depth Camera 

sudo apt-get install ros-kinetic-openni-*
echo $TURTLEBOT_3D_SENSOR
echo "export TURTLEBOT_3D_SENSOR=kinect" >> .bashrc

-- Step 3: Depth Camera 
Note: Open two new terminals and input these two commands

roslaunch turtlebot_rviz_launchers view_robot.launch
roslaunch turtlebot_teleop keyboard_teleop.launch

-- Step 4: Activating The Camera

Note: Open a new terminal and create a folder where your picture is stored. Change Directory into the new folder and type the following command.

rosrun image_view image_view image:=/camera/rgb/image_raw

Note: A new window should pop up and show what the robot sees in the simulation in real time. A separate depth camera view can also be activated this way.

rosrun image_view image_view image:=/camera/depth/image_raw

