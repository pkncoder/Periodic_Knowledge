from setuptools import setup

setup(
    name='elemSear',
    version='0.0.1',
    py_modules=['elemSear'],
    install_requires=[
        'click',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'elemSear = elemSear:cli',
        ],
    },
)