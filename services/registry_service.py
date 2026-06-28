from tools.calculator import CalculatorTool
from tools.weather import WeatherTool
from tools.datetime_tool import DateTimeTool
from tools.file_reader import FileReaderTool
from tools.web_search import WebSearchTool


class RegistryService:

    def __init__(self):

        self.tools = [

            CalculatorTool(),

            WeatherTool(),

            DateTimeTool(),

            FileReaderTool(),

            WebSearchTool()

        ]

    def list_tools(self):

        return [

            tool.info()

            for tool in self.tools

        ]
