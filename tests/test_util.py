from unittest.mock import patch

from hello import fetch_status


@patch("hello.http_util.requests.get")
def test_fetch_status_mock(mock_get):
    class Dummy:
        status_code = 200

    mock_get.return_value = Dummy()
    assert fetch_status("https://example.com") == 200
