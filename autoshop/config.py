"""Configuration utilities for the autoshop package."""

from dataclasses import dataclass, field
from typing import Dict
import json


def load_dtc_codes(path: str) -> Dict[str, str]:
    """Load diagnostic trouble codes from a JSON file."""
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data


@dataclass
class AppConfig:
    """Application configuration."""
    dtc_path: str = 'data/dtc_codes.json'
    host: str = '0.0.0.0'
    port: int = 8080
    extra: Dict[str, str] = field(default_factory=dict)
