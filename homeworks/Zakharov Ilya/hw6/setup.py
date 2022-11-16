from setuptools import setup

setup(
    name='my-awesome-scipt',
    entry_points={
        'console_scripts': [
            'my-awesome-scipt = main:main',
        ],
    }
)