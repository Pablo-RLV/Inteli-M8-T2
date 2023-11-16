import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
   gazebo_world = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('turtlebot3_gazebo'), 'launch'),
         '/turtlebot3_world.launch.py'])
         )
   nav2_ros = ExecuteProcess(
         cmd=['ros2', 'launch', 'nav2_bringup', 'bringup_launch.py', 'use_sim_time:=True', 'map:=../assets/mapa.yaml'],
         name='navigator_ros2',
         output='screen'
         )
   waypoint = ExecuteProcess(
         cmd=['ros2', 'run', 'controller_package', 'waypoint'],
         name='point_stack',
         output='screen'
         )

   return LaunchDescription([
      gazebo_world,
      nav2_ros,
      waypoint
   ])


if __name__ == "__main__":
   generate_launch_description()
