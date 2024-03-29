# Turtle Trajectories and Xacro ARM

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Usage and Configuration Instructions](#usage-and-configuration-instructions)


## Overview
This repo contains 2 independent projects:

### Part 1:
This package contains files that control the turtlebot's speed and direction, and make it move in an eight-shape trajectory.
1. The turtlebot begins in a `paused` state and believe that that configuration is *(x, y, z)* = *(0, 0, 0)*, relative to it's odometry frame.
2. Upon calling the `resume` service, the turtlebot will enter a "moving" state and begin following the eight-shape trajectory.
3. Upon calling the `pause` service, the turtlebot will pause its motion, without resetting its position.

### Part 2:
In this part I created a Xacro URDF for the robot arm shown below, visualized it in rviz, and made it's end-effector follow a trajectory.
<p align="center">
  <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/images/twolink.png">
</p>


# Getting Started

Create a workspace, clone the repo, and build the workspace:
```
mkdir -p ws/src && cd ws/src
git clone https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM.git
cd ../..
catkin_make
source devel/setup.bash 
```


## Usage and Configuration Instructions

### Part 1:

1. To activate the turtle, SSH into the turtlebot (`ssh ubuntu@turtlebot.local`) and run `roslaunch turtlebot3_bringup turtlebot3_robot.launch`.
2. To start running the turtlebot in figure-eight trajectory, run `roslaunch Turtle-Trajectories-and-Xacro-ARM figure_eight.launch`. The turtle begins in a `paused` state. <br/>
    <p align="center">
      <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/GIFs/turtlebot3.gif">
    </p>

    1. To launch the rqt_plot and show the turtlebot's x and y position (from odometry) vs. time, add `rqt_plot:=True` to the roslaunch command.

    <p align="center">
        <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/GIFs/robot_turtlesim.gif">
    </p>

    2. To launch the turtlebot Gazebo simulation, add `Gazebo:=True` to the roslaunch command.

    <p align="center">
        <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/GIFs/robot_gazebo.gif">
    </p>

    3. To launch the turtlebot Gazebo simulation, add `rviz:=True` to the roslaunch command.

    <p align="center">
        <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/GIFs/robot_rviz.gif">
    </p>

3. To move the turtle, call the service `resume` (`rosservice call /resume`).
4. To pause the turtle movement, call the service `pause` (`rosservice call /pause`).
5. To change the parameters `width` (W - the width of the figure eight), `height` (H - the height of the figure eight), `period` (T - the period of time it takes the turtlebot to complete the figure eight), edit the file `config/trajectory.yaml`
6. To change the parameter `pub_freq` (R - the frequency at which we publish the cmd_vel messages) edit the file `launch/figure_eight.launch`.
7. To test the calculated values at *t=0* and at *t=T/2* (half a cycle), run `catkin_make run_tests` from the root of workspace.
8. To see the transformation between the `world` frame and the `odom` frame, run `rosrun tf tf_echo /world /odom`
9. To watch the rqt tree, run `rosrun rqt_tf_tree rqt_tf_tree`


### Part 2:

1. To run the arm launchfile on rviz, run `roslaunch Turtle-Trajectories-and-Xacro-ARM xacro_arm.launch`.
2. To run the launchfile on rviz with gui, run `roslaunch Turtle-Trajectories-and-Xacro-ARM xacro_arm.launch gui:=True`
3. To run the arm launchfile on rviz with the marker, run `roslaunch Turtle-Trajectories-and-Xacro-ARM mark_arm.launch`

<p align="center">
    <img align="center" src="https://github.com/YaelBenShalom/Turtle-Trajectories-and-Xacro-ARM/blob/master/GIFs/arm_rviz.gif">
</p>
