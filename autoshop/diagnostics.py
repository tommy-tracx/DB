"""Utilities for interpreting OBD-II diagnostic codes."""

from typing import List, Dict
import json
from .config import load_dtc_codes, AppConfig


def interpret_codes(codes: List[str], config: AppConfig) -> List[Dict[str, str]]:
    """Return interpretations for the provided diagnostic codes."""
    dtc_map = load_dtc_codes(config.dtc_path)
    results = []
    for code in codes:
        desc = dtc_map.get(code.upper(), 'Unknown code')
        results.append({'code': code.upper(), 'description': desc})
    return results
