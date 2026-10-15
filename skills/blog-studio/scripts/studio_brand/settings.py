"""Brand repository inputs use the same shape as Training Studio's settings."""

from pathlib import Path
import re

from studios_config import repository


def check_repository(value):
    if value in (None, ''):
        return None
    value = repository(value).strip()
    if len(value) > 2000 or any(c.isspace() or ord(c) < 32 for c in value):
        raise ValueError('Give the brand skill repository as one https or ssh address.')
    if not re.match(r'^(https?://|ssh://|[\w.-]+@[\w.-]+:)', value):
        folder = Path(value).expanduser()
        if not folder.is_absolute():
            raise ValueError('Use an https or ssh repository address, or an absolute folder path.')
    return value


def check_release(value, repository=None):
    if value in (None, ''):
        return None
    if not isinstance(value, str) or not re.fullmatch(r'v?\d+\.\d+\.\d+', value):
        raise ValueError('Give a release tag such as v1.4.0, or leave it empty for the newest.')
    if not repository:
        raise ValueError('Give the brand skill repository before choosing a release.')
    return value
