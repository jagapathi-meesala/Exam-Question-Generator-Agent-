import os

class Settings:
    """
    Runtime configuration loaded from environment variables.
    Defaults are provided for missing variables.
    """
    DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
    DEFAULT_SEED = int(os.environ.get("DEFAULT_SEED", "42"))
    MAX_QUESTIONS_PER_REQUEST = int(os.environ.get("MAX_QUESTIONS_PER_REQUEST", "50"))
    STRICT_VALIDATION = os.environ.get("STRICT_VALIDATION", "true").lower() == "true"

settings = Settings()
