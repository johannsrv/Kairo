from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Config files (controllers.yaml)
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        # URDF xacro files
        (os.path.join('share', package_name, 'urdf', 'urdf'), glob('urdf/urdf/*.xacro')),
        # STL files (opcional, si quieres tenerlos en install)
        (os.path.join('share', package_name, 'urdf', 'stl', 'electronics'), glob('urdf/stl/electronics/*.stl')),
        (os.path.join('share', package_name, 'urdf', 'stl', 'robot_body'), glob('urdf/stl/robot_body/*.stl')),
        (os.path.join('share', package_name, 'world'),glob('world/*.sdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='johann',
    maintainer_email='johann@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)