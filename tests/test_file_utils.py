from pathlib import Path

import pytest

import app.file_utils as fu
from app.exceptions import InvalidFilenameError


def test_sanitize_upload_filename_success():
    assert fu.sanitize_upload_filename("the best@.exe") == "the_best_.exe"

def test_sanitize_upload_filename_strips_path():
    assert fu.sanitize_upload_filename("../../etc/passwd") == "passwd"


def test_sanitize_upload_filename_fail():
    with pytest.raises(InvalidFilenameError):
        fu.sanitize_upload_filename("")

def test_build_safe_upload_path_success():
    result = fu.build_safe_upload_path(Path("/tmp/uploads"), "my report?.pdf")
    assert result == Path("/tmp/uploads/my_report_.pdf")