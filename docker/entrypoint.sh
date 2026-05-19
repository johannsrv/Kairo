#!/bin/bash
set -e

# =========================
# ROS setup
# =========================
source /opt/ros/$ROS_DISTRO/setup.bash
source /root/ros2_ws/install/setup.bash

# =========================
# GUI support (Gazebo / RViz)
# =========================
export DISPLAY=${DISPLAY}
export QT_X11_NO_MITSHM=1

# XDG runtime (fix GUI crashes)
export XDG_RUNTIME_DIR=/tmp/runtime-$USER
mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR

# =========================
# ROS network config
# =========================
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}

# =========================
# GZ_SIM_RESOURCE_PATH
# =========================
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/root/ros2_ws/src/my_robot_description/models

# =========================
# API endpoints (future LLM / CV / planning)
# =========================
# export KAIRO_LLM_ENDPOINT=${KAIRO_LLM_ENDPOINT}
# export KAIRO_VISION_ENDPOINT=${KAIRO_VISION_ENDPOINT}
# export KAIRO_MAP_ENDPOINT=${KAIRO_MAP_ENDPOINT}

# =========================
# Optional: debug info
# =========================
echo "=============================="
echo "Kairo Robotics Environment"
echo "ROS_DISTRO: $ROS_DISTRO"
echo "ROS_DOMAIN_ID: $ROS_DOMAIN_ID"
# echo "LLM: $KAIRO_LLM_ENDPOINT"
# echo "VISION: $KAIRO_VISION_ENDPOINT"
# echo "MAP: $KAIRO_MAP_ENDPOINT"
echo "=============================="

# =========================
# Execute container command
# =========================
exec "$@"