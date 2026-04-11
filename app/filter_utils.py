from app.exceptions import InvalidFilterError


def _parse_non_negative_int(value: str | None , field_name: str , default: int)->int:
    if value is None or value == "":
        return default
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        raise InvalidFilterError(f"{field_name} must be an integer")
    if parsed < 0:
        raise InvalidFilterError(f"{field_name} must be non-negative")
    return parsed

def parse_filter_params(params: dict[str,str])->dict:
    limit = _parse_non_negative_int(params.get("limit"), "limit" , 10)
    offset = _parse_non_negative_int(params.get("offset"),"offset",10)

    status_raw = params.get("status")
    status = status_raw.strip().lower() if status_raw else None
    if status not in {None, "active","inactive"}:
        raise InvalidFilterError("status must be 'active or 'inactive'")
    sort_order_raw = params.get("sort_order")
    sort_order = sort_order_raw.strip().lower() if sort_order_raw else "asc"
    if sort_order not in {"asc", "desc"}:
        raise InvalidFilterError("sort_order must be 'asc' or 'desc'")
    return {
        "limit":limit ,
        "offset":offset ,
        "status":status ,
        "sort_order":sort_order
        }