class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Dev configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = False

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass