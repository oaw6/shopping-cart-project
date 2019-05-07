#Shopping cart test file

import pytest
import datetime

from shopping_cart import to_usd, human_friendly_string

def test_to_usd():
    assert to_usd(23.50) == "$23.50"
    assert to_usd(2) == "$2.00"
    assert to_usd(1230.4) == "$1,230.40"

def test_human_friendly_string():
    assert human_friendly_string(datetime.datetime.now()) == datetime.datetime.now().strftime("%Y/%m/%d at %H:%M:%S")