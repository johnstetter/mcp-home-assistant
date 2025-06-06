import click
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("MCP_URL", "http://localhost:8000")

@click.group()
def cli():
    pass

@cli.command()
@click.option('--domain', help='Filter by domain (e.g., sensor)')
@click.option('--device-class', help='Filter by device class (e.g., pm25)')
def entities(domain, device_class):
    params = {}
    if domain:
        params["domain"] = domain
    if device_class:
        params["device_class"] = device_class
    r = requests.get(f"{BASE_URL}/context/home-assistant/entities", params=params)
    for entity in r.json():
        print(f"{entity['entity_id']}: {entity['state']}")

if __name__ == "__main__":
    cli()
