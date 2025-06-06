import requests

class HomeAssistantContextTool:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def run(self, query: str):
        # Naive example — just fetch all sensors for now
        response = requests.get(f"{self.base_url}/context/home-assistant/entities?domain=sensor")
        return response.json()
