from setuptools import setup, find_packages

setup(
    name="hue_logger",
    version="0.1.0",
    author="Harman Singh",
    author_email="harman@petdrifts.com",
    description="A simple client for sending logs to the Hue Logs server.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/singh47/hue_logger_py_client",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

