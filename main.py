"""BackProfit — Live Trading Signal Bot."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from app.api.routes import api_router

BASE_DIR = Path(__file__).resolve().parent / "app"

app = FastAPI(title="BackProfit", version="1.0.0")

# Static files & templates
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# API routes
app.include_router(api_router, prefix="/api")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
