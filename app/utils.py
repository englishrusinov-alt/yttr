import hashlib
import uuid
from datetime import UTC,  datetime


def safe_time() -> datetime:
     return datetime.now(UTC)

def new_uuid4_str()-> str:
    return str(uuid.uuid4())

def sha256_hex(value : str)->str:
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return hashlib.sha256(value.encode("utf-8")).hexdigest()