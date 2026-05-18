import os
import shutil

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable, TimerAction
from launch.substitutions import Command, FindExecutable
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('my_robot_description')

    world_file = os.path.join(
        pkg_share,
        'world',
        'world_restauran.sdf'
    )

    xacro_file = os.path.join(pkg_share, 'urdf', 'urdf', 'robot.xacro')
    controllers_src = os.path.join(pkg_share, 'config', 'controllers.yaml')

    # Temporary path without “robot_description” in the path
    controllers_yaml = '/tmp/kairo_controllers.yaml'
    shutil.copy2(controllers_src, controllers_yaml)

    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        xacro_file,
        ' ',
        'controllers_file:=',
        controllers_yaml,
        ' ',
    ])

    share_dir = os.path.dirname(pkg_share)

    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=share_dir
    )

    ign_resource_path = SetEnvironmentVariable(
        name='IGN_GAZEBO_RESOURCE_PATH',
        value=':'.join([
            pkg_share,
            os.path.join(pkg_share, 'models')
        ])
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )

    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_file, '-r'],
        output='screen'
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'kairo',
            '-topic', 'robot_description',
            '-x', '-3.5',
            '-y', '0.0',
            '-z', '0.5'
        ],
        output='screen'
    )

    joint_state_broadcaster_spawner = ExecuteProcess(
        cmd=[
            'ros2', 'run', 'controller_manager', 'spawner',
            'joint_state_broadcaster',
            '--controller-manager', '/controller_manager',
            '--param-file', controllers_yaml,
        ],
        output='screen'
    )

    diff_drive_controller_spawner = ExecuteProcess(
        cmd=[
            'ros2', 'run', 'controller_manager', 'spawner',
            'diff_drive_controller',
            '--controller-manager', '/controller_manager',
            '--param-file', controllers_yaml,
        ],
        output='screen'
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    clock_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'
        ],
        output='screen'
    )

    return LaunchDescription([
        gz_resource_path,
        ign_resource_path,
        robot_state_publisher,
        gazebo,
        spawn_entity,
        TimerAction(period=5.0, actions=[joint_state_broadcaster_spawner]),
        TimerAction(period=7.0, actions=[diff_drive_controller_spawner]),
        rviz2,
        clock_bridge,
    ])