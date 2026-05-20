from setuptools import setup
import os
from glob import glob

package_name = 'my_robot_description'


def package_files(directory):
    paths = []

    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))

    return paths


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[

        # Ament
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        # package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Launch
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),

        # Config
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),

        # Worlds
        (
            os.path.join('share', package_name, 'world'),
            glob('world/*.sdf')
        ),

        # URDF/Xacro
        (
            os.path.join('share', package_name, 'urdf', 'urdf'),
            glob('urdf/urdf/*.xacro')
        ),

        # STL electronics
        (
            os.path.join(
                'share',
                package_name,
                'urdf',
                'stl',
                'electronics'
            ),
            glob('urdf/stl/electronics/*.stl')
        ),

        # STL robot body
        (
            os.path.join(
                'share',
                package_name,
                'urdf',
                'stl',
                'robot_body'
            ),
            glob('urdf/stl/robot_body/*.stl')
        ),

    ] +

    # MODELS COMPLETOS
    [
        (
            os.path.join(
                'share',
                package_name,
                os.path.dirname(path)
            ),
            [path]
        )
        for path in package_files('models')
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='johann',
    maintainer_email='johann@todo.todo',
    description='Robot description package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)