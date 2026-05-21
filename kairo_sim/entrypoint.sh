#!/bin/bash

set -e

# =========================================================
# SOURCE ROS
# =========================================================

source /opt/ros/$ROS_DISTRO/setup.bash
source /root/ros2_ws/install/setup.bash

# =========================================================
# DISPLAY CONFIG
# =========================================================

export DISPLAY=${DISPLAY}
export QT_X11_NO_MITSHM=1

# =========================================================
# XDG RUNTIME
# =========================================================

export XDG_RUNTIME_DIR=/tmp/runtime-root

mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR

# =========================================================
# ROS DOMAIN
# =========================================================

export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}

# =========================================================
# GAZEBO RESOURCE PATHS
# =========================================================

export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/root/ros2_ws/src/my_robot_description/models

# =========================================================
# GAZEBO SYSTEM PLUGINS
# =========================================================

export GZ_SIM_SYSTEM_PLUGIN_PATH=$GZ_SIM_SYSTEM_PLUGIN_PATH:/opt/ros/$ROS_DISTRO/lib

# =========================================================
# RMW IMPLEMENTATION
# =========================================================
export ROS_DOMAIN_ID=0
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# =========================================================
# DEBUG INFO
# =========================================================

echo "======================================="
echo "Kairo Simulation Environment"
echo "ROS_DISTRO: $ROS_DISTRO"
echo "ROS_DOMAIN_ID: $ROS_DOMAIN_ID"
echo "DISPLAY: $DISPLAY"
echo "======================================="

# =========================================================
# EXECUTE COMMAND
# =========================================================

exec "$@"