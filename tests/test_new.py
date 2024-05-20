from unittest.mock import patch
from uuid import uuid4

import pytest

from pew.pew import pew


@pytest.fixture
def mocked_check_call():
    with patch("pew.pew.check_call") as mock:
        yield mock


@pytest.mark.usefixtures("workon_home")
@pytest.mark.parametrize(
    "pip_cmd,exp_call", 
    [
        ("pip", ["pip", "install", "pew"]), 
        ("uv", ["uv", "pip", "install", "pew"]),
    ]
)
def test_pip_cmd_option(mocked_check_call, pip_cmd, exp_call):
    pew(["new", "-d", "--pip-cmd", pip_cmd, "-i", "pew", str(uuid4())])
    assert mocked_check_call.called
    assert mocked_check_call.call_args[0][0] == exp_call
