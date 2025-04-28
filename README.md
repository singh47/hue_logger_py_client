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
# Initialize the logger - replace localhost with your url
logger = HueLogger(server_url="http://localhost:5000", api_key="your-api-key", service_name="your service")
# Send a log
logger.log("Test log from Python client")
```