from datetime import datetime

def test_strftime():
    date_str = datetime.min.strftime("%4Y-%m-%d")
    assert date_str == "0001-01-01"