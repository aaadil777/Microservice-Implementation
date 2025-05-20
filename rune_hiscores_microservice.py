from fastapi import FastAPI
from httpx import AsyncClient
import asyncio

app = FastAPI(title="Wilson's RuneScape Hiscores Microservice")

BASE_URL = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player="

async def fetch_hiscores(player_name: str) -> dict:
    async with AsyncClient() as client:
        response = await client.get(BASE_URL + player_name)
        response.raise_for_status()
        return response.json()

@app.post("/fetch-hiscores/")
async def get_hiscores(player_name: str):
    try:
        data = await fetch_hiscores(player_name)
        return {
            "status": "success",
            "message": "Data delivered",
            "player": player_name,
            "hiscores": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "player": player_name
        }