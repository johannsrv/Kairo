import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command, FindExecutable

def generate_launch_description():
    pkg_my_robot = get_package_share_directory('my_robot_description')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    xacro_file = os.path.join(pkg_my_robot, 'urdf', 'robot.xacro')
    robot_description_content = Command([FindExecutable(name='xacro'), ' ', xacro_file])

    # Node for robot_state_publisher to publish the robot's state to TF and the /robot_description topic
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content, 'use_sim_time': use_sim_time}]
    )

    # Node for spawning the robot entity in Gazebo jazzy (ROS 2 Humble y Gazebo Harmonic)
    spawn_entity = Node(
        package='ros_gz_sim',       # pakage for Gazebo jazzy (ROS 2 Humble) and Gazebo Harmonic
        executable='create',
        arguments=[
            '-name', 'kairo',        # remplace 'kairo' with the name you want for your robot in Gazebo
            '-topic', 'robot_description',
            '-x', '0.0', '-y', '0.0', '-z', '0.5'
        ],
        output='screen'
    )

    # Command to launch Gazebo Harmonic (ROS 2 Humble) with an empty world
    gz_sim = ExecuteProcess(
        cmd=['gz', 'sim', 'empty.sdf', '-r'],  # -r ejecuta la simulación inmediatamente
        output='screen'
    )

    # load controllers 
    controllers_yaml = os.path.join(pkg_my_robot, 'config', 'controllers.yaml')
    load_parameters = ExecuteProcess(cmd=['ros2', 'param', 'load', '/controller_manager', controllers_yaml], output='screen')
    load_joint_state = ExecuteProcess(cmd=['ros2', 'control', 'load_controller', 'joint_state_broadcaster'], output='screen')
    load_imu = ExecuteProcess(cmd=['ros2', 'control', 'load_controller', 'imu_broadcaster'], output='screen')
    load_diff_drive = ExecuteProcess(cmd=['ros2', 'control', 'load_controller', 'diff_drive_controller'], output='screen')

    # Node for RViz2 to visualize the robot and its state in the simulation
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        gz_sim,                  # Launch Gazebo
        spawn_entity,            # Load the robot into Gazebo
        load_parameters,
        load_joint_state,
        load_imu,
        load_diff_drive,
        rviz2_node,
    ])