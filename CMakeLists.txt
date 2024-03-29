cmake_minimum_required(VERSION 3.8)
project(moving_cube2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()
install(
  DIRECTORY
    launch
    worlds
    urdf
    config
    rviz
  DESTINATION
    share/${PROJECT_NAME}/
)
ament_package()
