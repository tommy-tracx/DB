"""LookupBotAgent searches internal docs."""
from typing import Dict

class LookupBotAgent:
    def search(self, query: str) -> Dict:
        return {
            "links": [],
            "summary": "No results",
        }
