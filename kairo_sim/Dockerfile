ARG ROS_DISTRO=jazzy

FROM ros:${ROS_DISTRO}-ros-base

LABEL maintainer="Kairo Robotics Project"

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=${ROS_DISTRO}
ENV ROS_DOMAIN_ID=0
ENV RCUTILS_COLORIZED_OUTPUT=1
ENV PYTHONUNBUFFERED=1
ENV PIP_BREAK_SYSTEM_PACKAGES=1

SHELL ["/bin/bash", "-c"]

# =========================================================
# SYSTEM DEPENDENCIES
# =========================================================

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    vim \
    nano \
    sudo \
    python3-pip \
    python3-rosdep \
    python3-colcon-common-extensions \
    python3-vcstool \
    locales \
    lsb-release \
    gnupg2 \
    software-properties-common \
    x11-apps \
    mesa-utils \
    libgl1 \
    libglx-mesa0 \
    libgl1-mesa-dri \
    && rm -rf /var/lib/apt/lists/*

# =========================================================
# ROS2 + GAZEBO + CONTROL
# =========================================================

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-robot-state-publisher \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-ros-gz-sim \
    ros-${ROS_DISTRO}-ros-gz-bridge \
    ros-${ROS_DISTRO}-gz-ros2-control \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-controller-manager \
    ros-${ROS_DISTRO}-twist-mux \
    ros-${ROS_DISTRO}-teleop-twist-keyboard \
    && rm -rf /var/lib/apt/lists/*

# =========================================================
# ROSDEP
# =========================================================

RUN rosdep init || true
RUN rosdep update

# =========================================================
# WORKSPACE
# =========================================================

RUN mkdir -p /root/ros2_ws/src

WORKDIR /root/ros2_ws

# =========================================================
# COPY PROJECT
# =========================================================

COPY ./src /root/ros2_ws/src

# =========================================================
# INSTALL DEPENDENCIES
# =========================================================

RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    rosdep install \
    --from-paths src \
    --ignore-src \
    -r -y

# =========================================================
# BUILD WORKSPACE
# =========================================================

RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    colcon build --symlink-install

# =========================================================
# ENTRYPOINT
# =========================================================

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]