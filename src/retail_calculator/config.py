"""
Config and Constants
"""
import os

from logging import getLogger


logger = getLogger('fastapi')
DB_URI = os.getenv('DB_URI', '')
