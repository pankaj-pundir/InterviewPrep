from setuptools import setup

setup(
    name='resource_manager',
    packages=['.'],
    include_package_data=True,
    install_requires=[
        'flask','pydantic'
    ], )
