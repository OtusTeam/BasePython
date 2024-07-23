import asyncio
import sys
from pathlib import Path

import pytest

helpers = Path(__file__).resolve().parent / "helpers"
sys.path.insert(0, str(helpers))


@pytest.yield_fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
