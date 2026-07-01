import logging
from datetime import datetime
from src.routers.pojos.registrations import Registration

logger = logging.getLogger(__name__)

class RegistrationService:
    def __init__(self):
        self.__PLATFORMS: dict[str, dict] = {}
        
    def register_platform(self, platform_data: Registration) -> None:
        platform_id = platform_data.name.lower().strip().replace(" ", "_")
        current_time = datetime.now()
        
        self.__PLATFORMS[platform_id] = {
            **platform_data.model_dump(),
            "last_heartbeat": current_time
        }
        
    def get_registered_platforms(self) -> list[dict]:
        platforms_with_status = []
        now = datetime.now()

        for _, service_data in self.__PLATFORMS.items():
            last_heartbeat = service_data["last_heartbeat"]

            time_difference = now - last_heartbeat
            hours_passed = time_difference.total_seconds() / 3600
            
            if hours_passed < 2:
                status = "online"
            elif 2 <= hours_passed < 5:
                status = "warning"
            else:
                status = "offline"
                
            platform_info = service_data.copy()
            platform_info.pop("last_heartbeat", None)
            platform_info["status"] = status
            
            platforms_with_status.append(platform_info)
        return platforms_with_status