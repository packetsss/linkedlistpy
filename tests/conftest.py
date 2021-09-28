""" Fixtures that available everywhere """
import sys
import pytest
import random

@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer

@pytest.fixture(scope="session") # session will only run once
def get_random_number():
    # use yield if requires tear down code
    return random.uniform(0, 1000)