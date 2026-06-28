from fastapi import FastAPI

from routes.tools import router as tool_router
from routes.health import router as health_router

app = FastAPI(
    title="AI-Tools",
    version="1.0.0"
)

app.include_router(tool_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"AI-Tools",

        "status":"running"

    }
