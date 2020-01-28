from setuptools import setup

setup(
    name="aws-snapshot-checker",
    version="0.1",
    author="Dheeraj Saini",
    author_email="2dheerajkumar@gmail.com",
    description="Tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['aws'],
    url="https://github.com/dheerajsaini-ni/aws-snapshot-checker",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        snapmanager=aws.snapManager:cli
    ''',
)