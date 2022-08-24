import sys
from setuptools import setup, find_packages

setup(
    name="stepbystep",
    version="1.0.1",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="A simple tool to help you understand how a function works visually",
    long_description="A simple tool to help you understand how a function works following each step in terminal and inspecting the variable values",
    url="https://github.com/Funny-OpenSource-Projects/step_by_step.git",
    project_urls={
        'Source': 'https://github.com/Funny-OpenSource-Projects/step_by_step.git',
        'Tracker': 'https://github.com/Funny-OpenSource-Projects/step_by_step.git/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='algorithm visualization cli tool learning terminal'
)