"""
Generate JSON schema files used for API validation.

Run this script only when new `.json` files for API checks need to be generated.

Example (executed on June 15, 2025):
    generate_api_check_file(
        "BTC",
        "BTC-PERPETUAL",
        "future",
        False,
        1,
        999_999_999,
    )
"""

import json
import os
import sys
from datetime import datetime, timezone

from genson import SchemaBuilder

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from deribit_history_client.client import DeribitHistoryClient  # noqa: E402


def generate_api_check_file(
    currency: str,
    instrument_name: str,
    kind: str,
    expired: bool,
    start_seq: int,
    end_seq: int,
) -> None:
    """
    Generate JSON schema files for API validation.

    This function is intended for one-off internal use during development.
    It creates `.json` files that are later used to validate API responses.
    """
    deribit = DeribitHistoryClient()

    endpoints = {
        "get_instrument": deribit.get_instrument(instrument_name, raw=True),
        "get_instruments": deribit.get_instruments(
            currency,
            kind,
            expired,
            raw=True,
        ),
        "get_trades_by_sequence": deribit.get_trades_by_sequence(
            instrument_name,
            start_seq,
            end_seq,
            raw=True,
        ),
    }

    for name, response in endpoints.items():
        builder = SchemaBuilder()
        builder.add_object(response)
        schema = builder.to_schema()

        schema_with_metadata = {
            "$schema_generated_from": name,
            "$generated_at": datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z"),
            "schema": schema,
        }

        with open(
            f"src/deribit_history_client/schemas/{name}.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(schema_with_metadata, file, indent=2)

        print(f"✅ Schema for {name} saved.")
