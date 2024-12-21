import requests

class HueLogger:
    def __init__(self, server_url):
        """
        Initialize the logger with the server URL.
        :param server_url: Base URL of the Hue Logs server (e.g., "http://localhost:5000").
        """
        self.server_url = server_url.rstrip("/")
        self.log_endpoint = f"{self.server_url}/api/add-log"

    def log(self, message):
        """
        Send a log message to the Hue Logs server.
        :param message: The log message to send.
        """
        try:
            response = requests.post(
                self.log_endpoint,
                json={"message": message},
                timeout=5
            )
            if response.status_code == 200:
                print(f"Log sent: {message}")
            else:
                print(f"Failed to send log: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending log: {e}")

