#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription


# this is the function launch  system will look for


def generate_launch_description():


    spawn_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
        output="screen",
    )

    spawn_velocity_controller_cart = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["velocity_controller", "--controller-manager", "/controller_manager"],
        output="screen",
    )

    spawn_position_controller_cart = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["position_controller", "--controller-manager", "/controller_manager"],
        output="screen",
    )
    
    spawn_position_controller_pole = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["pole_controller", "--controller-manager", "/controller_manager"],
        output="screen",
    )

    

    # create and return launch description object
    return LaunchDescription(
        [
            
            spawn_controller,
            spawn_position_controller_cart,
            spawn_velocity_controller_cart,
            #spawn_position_controller_pole,
            
        ]
    )
