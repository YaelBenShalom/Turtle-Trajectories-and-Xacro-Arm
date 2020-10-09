# homework02-YaelBenShalom
GitHub repository - https://github.com/ME495-EmbeddedSystems/homework02-YaelBenShalom

## Overview
This package contains files that control the turtlebot's speed and direction, and make it move in an eight-shape trajectory
1. The turtlebot begins in a "paused" state and believe that that configuration is (x, y, z) = (0, 0, 0), relative to it's odometry frame.
2. Upon calling the "resume" service, the turtlebot will enter a "moving" state and begin following the eight-shape trajectory
3. Upon calling the "pause" service, the turtlebot will pause its motion, without resetting its position

## Usage instructions
1. To start running the turtlebot in figure-eight trajectory, run roslaunch homework2 figure_eight.launch.
2. To change the parameters W (the width of the figure eight), H (the height of the figure eight), T (the period of time it takes the turtlebot to complete the figure eight) and R (the frequency at which we publish the cmd_vel messages), you can edit the launchfile - launch/figure_eight.launch.