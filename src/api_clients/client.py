
import requests

class Client:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_leads(self):
        response = requests.get(
            f"{self.base_url}/leads",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
