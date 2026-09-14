import os
from dotenv import load_dotenv

class Settings:
    def __init__(self) -> None:
        load_dotenv()
        self.steam_api_key = os.getenv("STEAM_API_KEY")
        self.steam_id = os.getenv("STEAM_ID") or None

        if not self.steam_api_key:
            raise ValueError("A variável STEAM_API_KEY não foi configurada.")
        