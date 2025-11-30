import pytest

from deribit_history_client.client import DeribitHistoryClient


@pytest.fixture
def wrapper() -> DeribitHistoryClient:
    """Return an instance of DeribitHistoryClient."""
    return DeribitHistoryClient()
