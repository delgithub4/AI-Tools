from typing import Any

from pydantic import BaseModel


class ToolRequest(BaseModel):
    tool: str
    parameters: dict[str, Any] = {}


class ToolResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
