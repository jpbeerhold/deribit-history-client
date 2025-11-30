from __future__ import annotations

import json
from importlib.resources import files
from typing import Any, Dict

from jsonschema import ValidationError, validate

from . import read


class DeribitHistoryClient:
    """
    Wrapper for requests to historical Deribit trading data.

    This class encapsulates various HTTP GET requests to the public
    Deribit API in order to query information about instruments and trades.
    """

    BASE_URL: str = "https://history.deribit.com/api/v2/public/"
    HEADERS: Dict[str, str] = {"Accept": "application/json"}

    def get_instrument(self, instrument_name: str, raw: bool = False) -> Dict[str, Any]:
        """
        Fetch details for a specific trading instrument.

        Args:
            instrument_name: Name of the instrument
                (e.g. "BTC-30JUN23-20000-C").
            raw: If True, return the full HTTP response from the API;
                otherwise return only the "result" part.

        Returns:
            JSON response containing instrument metadata.
        """
        response = read.get_instrument(self.BASE_URL, self.HEADERS, instrument_name)
        if raw:
            return response
        return response["result"]

    def get_instruments(
        self,
        currency: str,
        kind: str,
        expired: bool,
        raw: bool = False,
    ) -> Dict[str, Any]:
        """
        Fetch a list of instruments for a given currency and instrument type.

        Args:
            currency: Currency code (e.g. "BTC", "ETH").
            kind: Instrument type (e.g. "future", "option").
            expired: If True, include expired instruments.
            raw: If True, return the full HTTP response from the API;
                otherwise return only the "result" part.

        Returns:
            JSON response containing a list of instruments.
        """
        response = read.get_instruments(
            self.BASE_URL,
            self.HEADERS,
            currency,
            kind,
            expired,
        )
        if raw:
            return response
        return response["result"]

    def get_trades_by_sequence(
        self,
        instrument_name: str,
        start_seq: int,
        end_seq: int,
        count: int = 10_000,
        raw: bool = False,
    ) -> Dict[str, Any]:
        """
        Fetch trades for a given instrument by sequence range.

        Args:
            instrument_name: Name of the instrument.
            start_seq: Trade sequence number where the query should start.
            end_seq: Trade sequence number where the query should end.
            count: Maximum number of trades to request.
            raw: If True, return the full HTTP response from the API;
                otherwise return only the "result" part.

        Returns:
            JSON response containing trade data.
        """
        response = read.get_trades_by_sequence(
            self.BASE_URL,
            self.HEADERS,
            instrument_name,
            start_seq,
            end_seq,
            count,
        )
        if raw:
            return response
        return response["result"]

    def perform_api_check(
        self,
        currency: str = "BTC",
        instrument_name: str = "BTC-PERPETUAL",
        kind: str = "future",
        expired: bool = False,
        start_seq: int = 99_999_999,
        end_seq: int = 99_999_999,
    ) -> None:
        """
        Validate current API responses against stored JSON schemas.

        This method calls several endpoints and checks their responses
        against local JSON schema files to detect API format changes.

        Args:
            currency: Currency code of the instruments.
            instrument_name: Name of the instrument.
            kind: Instrument type (e.g. "future", "option").
            expired: If True, include expired instruments.
            start_seq: Trade sequence number where the query should start.
            end_seq: Trade sequence number where the query should end.
        """
        endpoints: Dict[str, Dict[str, Any]] = {
            "get_instrument": self.get_instrument(instrument_name, raw=True),
            "get_instruments": self.get_instruments(
                currency,
                kind,
                expired,
                raw=True,
            ),
            "get_trades_by_sequence": self.get_trades_by_sequence(
                instrument_name,
                start_seq,
                end_seq,
                raw=True,
            ),
        }

        for name, response in endpoints.items():
            schema_path = files("deribit_history_client.schemas").joinpath(
                f"{name}.json",
            )

            try:
                with schema_path.open("r", encoding="utf-8") as file:
                    schema = json.load(file)
            except FileNotFoundError:
                print(f"⚠️  No schema found for {name}. Skipping.")
                continue

            print(f"⏳ Validating {name} ...")

            try:
                validate(instance=response, schema=schema)
                print(f"✅ {name} OK\n")
            except ValidationError as exc:
                print(f"❌ {name} FAILED – detected format change!")
                print(f"Error: {exc.message}\n")
