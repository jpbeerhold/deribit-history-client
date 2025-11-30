import pytest

from deribit_history_client.client import DeribitHistoryClient


@pytest.mark.external
def test_api_check_runs_against_live_api() -> None:
    """Run perform_api_check against the live Deribit API."""
    client = DeribitHistoryClient()
    client.perform_api_check()
