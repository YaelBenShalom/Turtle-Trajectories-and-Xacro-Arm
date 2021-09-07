cmake_minimum_required(VERSION 3.0.2)
project(turtle_trajectories_and_xacro_arm)


## Find catkin macros and libraries
find_package(
  catkin
  REQUIRED
  COMPONENTS
  geometry_msgs
  message_generation
  turtlesim
)

catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate services in the 'srv' folder
add_service_files(
  FILES
  PauseTurtle.srv
  ResumeTurtle.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
    DEPENDENCIES
    turtlesim
)

###################################
## catkin specific configuration ##
###################################

## The catkin_package macro generates cmake config files for your package
catkin_package(
  CATKIN_DEPENDS
  geometry_msgs
  message_runtime
  turtlesim
)

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
  nodes/trajectory.py
  nodes/arm_traj.py
  nodes/arm_mark.py
  src/${PROJECT_NAME}/calculations.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############

# Add rostest files
if (CATKIN_ENABLE_TESTING)
    catkin_add_nosetests(test)
endif()