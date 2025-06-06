from fastapi import FastAPI
from server.context import get_entities

app = FastAPI()

@app.get("/context/home-assistant/entities")
async def entities(domain: str = None, device_class: str = None):
    return await get_entities(domain=domain, device_class=device_class)
