from typing import Dict, Any
import json
from pathlib import Path

class OpenAIFunctionHelper:
    def __init__(self):
        self.schema_path = Path(__file__).parent.parent / "schemas" / "function_schemas.json"
        self.function_schemas = self._load_schemas()

    def _load_schemas(self) -> Dict[str, Any]:
        """Load function schemas from JSON file"""
        with open(self.schema_path) as f:
            return json.load(f)

    def get_function_schema(self, function_name: str) -> Dict[str, Any]:
        """Get schema for a specific function"""
        return self.function_schemas.get(function_name)

    def get_all_schemas(self) -> Dict[str, Any]:
        """Get all function schemas"""
        return self.function_schemas