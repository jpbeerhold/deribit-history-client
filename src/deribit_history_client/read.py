from typing import Any, Dict

import requests


def get_instrument(base_url: str, headers: Dict[str, str], instrument_name: str) -> Dict[str, Any]:
    """
    Fetch metadata for a specific trading instrument.

    Args:
        base_url: Base URL of the Deribit API.
        headers: HTTP headers including authentication information.
        instrument_name: Name of the instrument.

    Returns:
        JSON response containing instrument data.
    """
    response = requests.get(
        f"{base_url}/get_instrument",
        headers=headers,
        params={"instrument_name": instrument_name},
        timeout=30,
    )
    return response.json()


def get_instruments(
    base_url: str,
    headers: Dict[str, str],
    currency: str,
    kind: str,
    expired: bool,
) -> Dict[str, Any]:
    """
    Fetch a list of instruments for a given currency and instrument type.

    Args:
        base_url: Base URL of the Deribit API.
        headers: HTTP headers including authentication information.
        currency: Currency code (e.g. "BTC", "ETH").
        kind: Instrument type (e.g. "future", "option").
        expired: If True, include expired instruments.

    Returns:
        JSON response containing a list of instruments.
    """
    expired_str = "true" if expired else "false"

    response = requests.get(
        f"{base_url}/get_instruments",
        headers=headers,
        params={
            "currency": currency,
            "kind": kind,
            "expired": expired_str,
        },
        timeout=30,
    )

    return response.json()


def get_trades_by_sequence(
    base_url: str,
    headers: Dict[str, str],
    instrument_name: str,
    start_seq: int,
    end_seq: int,
    count: int,
) -> Dict[str, Any]:
    """
    Fetch trades for a specific trading instrument by sequence range.

    Args:
        base_url: Base URL of the Deribit API.
        headers: HTTP headers including authentication information.
        instrument_name: Name of the instrument.
        start_seq: Trade sequence number where the query should start.
        end_seq: Trade sequence number where the query should end.
        count: Maximum number of trades to request.

    Returns:
        JSON response containing trade data.
    """
    params = {
        "start_seq": start_seq,
        "end_seq": end_seq,
        "instrument_name": instrument_name,
        "count": count,
    }

    response = requests.get(
        f"{base_url}/get_last_trades_by_instrument",
        headers=headers,
        params=params,
        timeout=30,
    )

    return response.json()
