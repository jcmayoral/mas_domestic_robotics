cmake_minimum_required(VERSION 2.8.3)
project(mdr_sound_monitor)

find_package(catkin REQUIRED
  COMPONENTS
    roslint
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
    rospy
)

### TESTS
roslint_python()

if(CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)

  roslaunch_add_file_check(ros/launch)
endif()

install(DIRECTORY ros/launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/ros/launch
)

install(PROGRAMS
  ros/scripts/sound_monitor_node
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
