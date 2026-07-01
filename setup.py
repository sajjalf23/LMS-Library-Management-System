from setuptools import setup, find_packages

setup(
    name="LMS",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "lms = main:main",
        ],
    },
)