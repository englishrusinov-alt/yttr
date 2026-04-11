import pytest

import app.exceptions as ex
import app.file_utils as fu
def test_custom_exception_success():
    with pytest.raises(ex.InvalidFilenameError):
        fu.sanitize_upload_filename("")