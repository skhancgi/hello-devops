from http_util import fetch_status


def test_fetch_status_ok():
    # httpbin.org provides stable testing endpoints
    status = fetch_status("https://httpbin.org/status/200")
    assert status == 200