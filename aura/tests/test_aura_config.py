import pytest
from aura.aura_config import SafetyConfigValidator

def test_valid_config():
    cfg = {"threshold": 5.0, "timeout_secs": 10}
    validator = SafetyConfigValidator(cfg)
    assert validator.validate()

def test_missing_key():
    cfg = {"threshold": 5.0}
    with pytest.raises(ValueError, match="Missing required key: timeout_secs"):
        SafetyConfigValidator(cfg).validate()

def test_invalid_value():
    cfg = {"threshold": -1, "timeout_secs": 10}
    with pytest.raises(ValueError, match="Invalid value for threshold"):
        SafetyConfigValidator(cfg).validate()
