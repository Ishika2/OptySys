from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import get_database_connection
from app.routers import organizations

"""FastAPI Instance"""
app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    version=settings.project_version,
    docs_url=settings.debug and "/docs" or None,
)

"""MiddleWares"""
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

"""Routers"""
app.include_router(organizations.router)


"""Database Connection"""


@app.on_event("startup")
async def startup_db_client():
    await get_database_connection()
