from fastapi import APIRouter

from services.tool_service import ToolService

router = APIRouter(
    prefix="/tools",
    tags=["Tools"]
)

tool = ToolService()


@router.get("/")
def tools():

    return tool.available()
