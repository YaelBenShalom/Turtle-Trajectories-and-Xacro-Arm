#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/src/interbotix_ros_arms/interbotix_descriptions"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/install/lib/python3/dist-packages:/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/build" \
    "/usr/bin/python3" \
    "/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/src/interbotix_ros_arms/interbotix_descriptions/setup.py" \
     \
    build --build-base "/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/build/interbotix_ros_arms/interbotix_descriptions" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/install" --install-scripts="/home/yael/Documents/MSR_Courses/MECH_ENG_495/HW/HW2/nuws/install/bin"
