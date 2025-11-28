from http_util import fetch_status

def test_fetch_status_ok():
    # httpbin.org is a stable testing endpoint; returns 200 on /status/200
    status = fetch_status("https://httpbin.org/status/200")
    assert status == 200
