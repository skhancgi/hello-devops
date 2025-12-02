import requests


def fetch_status(url: str) -> int:
    """Return HTTP status code for GET request to url."""
    resp = requests.get(url, timeout=5)
    return resp.status_code
