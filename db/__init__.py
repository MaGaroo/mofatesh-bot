import os

import config
from db.course import Course

os.makedirs(config.DATA_DIR, exist_ok=True)
os.makedirs(config.COURSES_DIR, exist_ok=True)
os.makedirs(config.LISTENERS_DIR, exist_ok=True)
