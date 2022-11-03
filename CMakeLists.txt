cmake_minimum_required(VERSION 3.0.2)
project(test_demo_py)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_python_setup()
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Add rostests
find_package(rostest REQUIRED)
add_rostest(test/pub_test.test)

