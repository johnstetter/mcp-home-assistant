import httpx, os
from dotenv import load_dotenv

load_dotenv()
HASS_URL = os.getenv("HASS_URL")
HASS_TOKEN = os.getenv("HASS_TOKEN")

async def get_entities(domain=None, device_class=None):
    headers = {"Authorization": f"Bearer {HASS_TOKEN}"}
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{HASS_URL}/api/states", headers=headers)
        r.raise_for_status()
        entities = r.json()
        if domain:
            entities = [e for e in entities if e["entity_id"].startswith(f"{domain}.")]
        if device_class:
            entities = [e for e in entities if e["attributes"].get("device_class") == device_class]
        return entities
