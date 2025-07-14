# aura/aura_config.py

class SafetyConfigValidator:
    """
    Validates that a safety config dict has required keys and
    sensible positive values.
    """
    def __init__(self, config: dict):
        self.config = config

    def validate(self) -> bool:
        required = ["threshold", "timeout_secs"]
        for key in required:
            if key not in self.config:
                raise ValueError(f"Missing required key: {key}")
            val = self.config[key]
            if not isinstance(val, (int, float)) or val <= 0:
                raise ValueError(f"Invalid value for {key}: {val}")
        return True
