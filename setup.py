from setuptools import setup

setup(
    name='simple_calculator',
    version='1.0.0',
    description="A simple Python calculator",
    py_modules=['calculator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires= '>=3.6',
)