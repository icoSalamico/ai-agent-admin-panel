import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from sqladmin import Admin
from starlette.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import create_async_engine
from admin import setup_admin
import sqladmin
from routes.prompt_test import router as prompt_test

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL)

app = FastAPI()

app.include_router(prompt_test)

# Serve SQLAdmin statics
app.mount(
    "/admin/statics",
    StaticFiles(directory=os.path.join(os.path.dirname(sqladmin.__file__), "statics")),
    name="admin-statics",
)

setup_admin(app, engine)
