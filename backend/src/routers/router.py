from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from src.di import Container

from src.routers.pojos.registrations import Registration
from src.services.registration import RegistrationService


api_router = APIRouter()

@api_router.post("/register", status_code=200)
@inject
async def register_platform(registration: Registration, registration_service: RegistrationService = Depends(Provide[Container.registration_service])):
    registration_service.register_platform(registration)
    
@api_router.get("/platforms", status_code=200, response_model=list[dict])
@inject
async def get_registered_platforms(registration_service: RegistrationService = Depends(Provide[Container.registration_service])):
    return registration_service.get_registered_platforms()
