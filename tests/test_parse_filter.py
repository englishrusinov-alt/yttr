from app.exceptions import InvalidFilterError
from app.filter_utils import parse_filter_params
import pytest

def test_parse_filter_params_success():
    params = {
        "limit": "20",
        "offset": "5",
        "status": " Active ",
        "sort_order": "DESC",
    }

    result = parse_filter_params(params)

    assert result == {
        "limit": 20,
        "offset": 5,
        "status": "active",
        "sort_order": "desc",
    }


def test_parse_filter_params_failure():
    with pytest.raises(InvalidFilterError):
        parse_filter_params({"limit": "-1"})