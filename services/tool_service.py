from services.registry_service import RegistryService


class ToolService:

    def __init__(self):

        self.registry = RegistryService()

    def available(self):

        return {

            "tools": self.registry.list_tools()

        }
