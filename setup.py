from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="hue_logger",
    version="0.1.2",
    author="Harman Singh",
    author_email="harman@petdrifts.com",
    description="A simple client for sending logs to the Hue Logs server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singh47/hue_logger_py_client", 
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

