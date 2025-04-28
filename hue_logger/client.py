import requests

class HueLogger:
    def __init__(self, server_url, api_key, service_name=None):
        """
        Initialize the logger with the server URL, API key, and optional service name.
        :param server_url: Base URL of the Hue Logs server (e.g., "http://localhost:5000").
        :param api_key: API key for authentication.
        :param service_name: Optional name of the service or application (e.g., "WebApp").
        """
        self.server_url = server_url.rstrip("/")
        self.api_key = api_key
        self.service_name = service_name
        self.log_endpoint = f"{self.server_url}/api/add-log"
        self.headers = {"X-API-Key": self.api_key}

    def log(self, message):
        """
        Send a log message to the Hue Logs server.
        :param message: The log message to send.
        """
        try:
            payload = {"message": message}
            if self.service_name:
                payload["service_name"] = self.service_name
            response = requests.post(
                self.log_endpoint,
                json=payload,
                headers=self.headers,
                timeout=5
            )
            if response.status_code == 200:
                print(f"Log sent: {message}")
            elif response.status_code == 401:
                print(f"Authentication failed: Invalid or missing API key")
            else:
                print(f"Failed to send log: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending log: {e}")