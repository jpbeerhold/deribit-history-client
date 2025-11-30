from unittest.mock import patch

from .config import DUMMY_RESPONSE


@patch(
    "deribit_history_client.read.get_instrument",
    return_value=DUMMY_RESPONSE
)
def test_get_instrument(mock_get, wrapper) -> None:
    result = wrapper.get_instrument("BTC-30JUN23-20000-C", raw=True)

    assert result == DUMMY_RESPONSE
    mock_get.assert_called_once()


@patch(
    "deribit_history_client.read.get_instruments",
    return_value=DUMMY_RESPONSE
)
def test_get_instruments(mock_get, wrapper) -> None:
    result = wrapper.get_instruments("BTC", "future", True, raw=True)

    assert result == DUMMY_RESPONSE
    mock_get.assert_called_once()


@patch(
    "deribit_history_client.read.get_trades_by_sequence",
    return_value=DUMMY_RESPONSE,
)
def test_get_last_trades_by_sequence(mock_get, wrapper) -> None:
    result = wrapper.get_trades_by_sequence(
        "BTC-30JUN23-20000-C",
        1,
        5_000,
        raw=True,
    )

    assert result == DUMMY_RESPONSE
    mock_get.assert_called_once()
