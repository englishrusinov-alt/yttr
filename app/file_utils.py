from pathlib import Path

import re
import app.exceptions as ex
_SAFE_CHARS_RE = re.compile(r'[^a-zA-Z0-9._-]+')
_LEADING_DOTS_RE = re.compile(r'^\.+')
_MULTI_UNDERSCORES_RE = re.compile(r'_+')


def sanitize_upload_filename(filename: str) -> str:

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    name = Path(filename).name.strip()

    if name in {"",".",".."}:
        raise ex.InvalidFilenameError("filename is empty or invalid")
    name = _LEADING_DOTS_RE.sub("",name)
    name = _SAFE_CHARS_RE.sub("_",name)
    name = _MULTI_UNDERSCORES_RE.sub("_", name).strip("_")
    if name == "":
        raise ex.InvalidFilenameError("filename is empty or invalid")
    return name
def build_safe_upload_path(base_dir: Path, filename: str) -> Path:
    safe_name = sanitize_upload_filename(filename)
    return base_dir / safe_name

