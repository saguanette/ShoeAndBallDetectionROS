from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='thing_detector',
            executable='video_publisher',
            name='pub'
        ),
        Node(
            package='thing_detector',
            executable='thing_detect_subscriber',
            name='sub'
        )

    ])
