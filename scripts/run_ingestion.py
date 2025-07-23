#!/usr/bin/env python3
"""
scripts/run_ingestion.py

Orchestrates ingestion of raw equity price and fundamental data.
Saves CSV/JSON files under data/raw/ and logs metadata.
"""

import argparse
import logging
import os
from datetime import datetime

from src.config import (
    RAW_DATA_DIR,
    TICKERS_FILE,
    PRICE_DATA_FILENAME,
    FUNDAMENTALS_FILENAME,
)
from src.data_ingestion import (
    fetch_price_data,
    fetch_fundamentals_data,
    save_ingestion_metadata,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Ingest OHLCV price data and fundamentals for equity universe"
    )
    parser.add_argument(
        "--tickers-file",
        type=str,
        default=TICKERS_FILE,
        help="Path to CSV file containing one ticker per line",
    )
    parser.add_argument(
        "--start-date",
        type=str,
        required=True,
        help="Start date for price data (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--end-date",
        type=str,
        required=True,
        help="End date for price data (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download and overwrite existing raw files",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )

    # ensure raw data directory exists
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    logging.info(f"Raw data directory: {RAW_DATA_DIR}")

    # load tickers
    with open(args.tickers_file, "r") as f:
        tickers = [line.strip() for line in f if line.strip()]
    logging.info(f"Loaded {len(tickers)} tickers from {args.tickers_file}")

    # parse dates
    start = datetime.fromisoformat(args.start_date)
    end = datetime.fromisoformat(args.end_date)

    # price data ingestion
    price_path = os.path.join(RAW_DATA_DIR, PRICE_DATA_FILENAME)
    if not os.path.exists(price_path) or args.force:
        logging.info(
            f"Fetching OHLCV price data from {start.date()} to {end.date()}"
            + (" (force overwrite)" if args.force else "")
        )
        price_df = fetch_price_data(tickers, start_date=start, end_date=end)
        price_df.to_csv(price_path, index=True)
        logging.info(f"Wrote price data to {price_path}")
    else:
        logging.info(f"Skipping price download; file exists at {price_path}")

    # fundamentals data ingestion
    fund_path = os.path.join(RAW_DATA_DIR, FUNDAMENTALS_FILENAME)
    if not os.path.exists(fund_path) or args.force:
        logging.info(
            "Fetching company fundamentals via EDGAR"
            + (" (force overwrite)" if args.force else "")
        )
        fund_df = fetch_fundamentals_data(tickers)
        fund_df.to_json(fund_path, orient="records", lines=True)
        logging.info(f"Wrote fundamentals to {fund_path}")
    else:
        logging.info(f"Skipping fundamentals download; file exists at {fund_path}")

    # save ingestion metadata
    save_ingestion_metadata(
        output_dir=RAW_DATA_DIR,
        tickers=tickers,
        start_date=start,
        end_date=end,
    )
    logging.info("Data ingestion complete.")


if __name__ == "__main__":
    main()
