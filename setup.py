from setuptools import find_packages, setup

package_name = 'person_learning_mock'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ri-onefujitsu',
    maintainer_email='gilsocojp@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'vision_node = person_learning_mock.vision_node:main',
        'person_tracker = person_learning_mock.person_tracker:main',
        'task_planner = person_learning_mock.task_planner:main',
        'dialogue_manager = person_learning_mock.dialogue_manager:main',
        'asr_node = person_learning_mock.asr_node:main',
        'nlp_node = person_learning_mock.nlp_node:main',
    ],
},
)
