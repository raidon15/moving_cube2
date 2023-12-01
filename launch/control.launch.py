#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription


# this is the function launch  system will look for


def generate_launch_description():

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        output="screen",
    )

    spawn_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
        output="screen",
    )

    spawn_controller_cube = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["inertia_wheel_roll_joint_velocity_controller", "--controller-manager", "/controller_manager"],
        output="screen",
    )

    

    # create and return launch description object
    return LaunchDescription(
        [
            control_node,
            spawn_controller,
            #spawn_controller_cube,
            
        ]
    )
