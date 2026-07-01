from dependency_injector import containers, providers
from src.config.app_config import app_config

from src.services.registration import RegistrationService

class Container(containers.DeclarativeContainer):
    registration_service = providers.Singleton(RegistrationService)