import json
import os

from ibgeexplorer.domain.models.config import Settings


def load_settings() -> Settings:
    """Load settings from a JSON file."""
    config_path = "settings.json"
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Arquivo de configuração não encontrado: {config_path}"
        )
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Settings.from_json(data)


settings = load_settings()
