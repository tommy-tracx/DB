"""TechWriterAgent converts text to SOP."""
from typing import Dict

class TechWriterAgent:
    def generate_sop(self, text: str) -> Dict:
        return {
            "title": "Generated SOP",
            "steps": ["Example step"],
            "tools": [],
            "triggers": [],
        }
