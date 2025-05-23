from pathlib import Path
import yaml
from typing import Literal
from ..schemas.app import AppConfig

EnvType = Literal["dev", "prod"]

def load_app_config(env: EnvType) -> AppConfig: #Carga configuración desde YAMLs locales (uso real)
    yaml_path = Path(__file__).parent.parent / "envs" / f"{env}.yml"
    with open(yaml_path) as file:
        data = yaml.safe_load(file)
        return AppConfig(**data["app"])  # Asume estructura {app: {...}}