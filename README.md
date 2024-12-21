# Project description
Hue Logger is a simple Python client for sending logs to the Hue Logs server. Hue Logs is minimal logging dashboard. Compatible with Python3.
Install Hue Server from [here](https://github.com/singh47/huelogs/)

## Installation
```bash
pip install hue-logger
```

## Usage

Replace localhost with your server url

```bash
from hue_logger import HueLogger

logger = HueLogger("http://localhost:5000")
logger.log("This is a test log")
```