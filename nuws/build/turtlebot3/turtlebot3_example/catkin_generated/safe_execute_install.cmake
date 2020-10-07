execute_process(COMMAND "/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/build/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/build/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
