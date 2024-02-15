from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='your_package_name',
    version='1.0',
    install_requires=requirements,
    packages=['your_package_name'],
    entry_points={
        'console_scripts': [
            'your_script_name=your_package_name.your_module:main',
        ],
    },
)