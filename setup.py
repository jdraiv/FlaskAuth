
from setuptools import setup


setup(
    name='flaskauth',
    packages=['flaskauth'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-login',
    ],
)