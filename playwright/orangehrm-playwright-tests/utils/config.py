"""Loads settings from .env so tests don't hardcode URLs/credentials."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
