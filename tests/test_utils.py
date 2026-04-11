import datetime
import hashlib
import uuid

import pytest

import app.utils as u



def test_safe_time_success():
    test_date_time = u.safe_time()
    assert isinstance(test_date_time, datetime.datetime)
    assert test_date_time.tzinfo is not None

def test_uuid_success():
    test_uuid = u.new_uuid4_str()
    parsed =  uuid.UUID(test_uuid)
    assert str(parsed) == test_uuid

def test_sha_256_hex_success():
    value = "Test me!"
    test_sha_256_hex = u.sha256_hex(value)

    assert test_sha_256_hex == hashlib.sha256(value.encode("utf-8")).hexdigest()

def test_sha_256_hex_failure():

    with pytest.raises(TypeError):
        u.sha256_hex(None)
