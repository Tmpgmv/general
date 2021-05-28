import os
from enum import Enum

from django.conf import settings


class DestinationDirs(Enum):
    RESULT_DIR = os.path.join(settings.BASE_DIR, "..", "..", "result").lower()
    EXTERNAL = "external"  # For static assets and PHP files.
    MARKETING_AGENCY = "ma"
    CONTENT = "c"


class FileExtensions(Enum):
    CSS = "css"
    PHP = "php"
    JS = "js"


class StaticFileNames(Enum):
    RESULT_FILE_NAME = "main"
