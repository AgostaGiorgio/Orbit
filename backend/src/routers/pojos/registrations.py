from pydantic import BaseModel, Field, HttpUrl

class Registration(BaseModel):
    name: str = Field(..., description="Name of the platform or service being registered")      
    version: str = Field(..., description="Version of the platform or service being registered")  
    description: str = Field(..., description="Description of the platform or service being registered")
    icon: HttpUrl = Field(..., description="URL of the icon for the platform or service being registered")
    url: HttpUrl = Field(..., description="URL of the platform or service being registered")