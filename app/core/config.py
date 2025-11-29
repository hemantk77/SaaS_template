from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SaaS Backend"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./saas.db"
    
    class Config:
        case_sensitive=True
        
settings = Settings()