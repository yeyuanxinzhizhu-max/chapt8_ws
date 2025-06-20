from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'fishbot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
        #(os.path.join('share', package_name, 'world'), glob('world/**')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xinzhizhu',
    maintainer_email='xinzhizhu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           # "rotate_wheel= fishbot_description.rotate_wheel:main"
        ],
    },
)
