#!/usr/bin/env python
"""
Contains utility functions for the dashboard app that call the Polygon.io API and format the data that it returns
"""
import pandas as pd
# noinspection PyUnresolvedReferences
from polygon import RESTClient
import os
import datetime

DEBUG_MODE = True


def ts_to_datetime(ts) -> str:
    """
    Returns a formatted string describing the date of the Unix style ms timestamp
    :param ts:  Unix timestamp (ms)
    :type ts:   TODO
    :return:    Formatted string
    :rtype:     TODO
    """
    return datetime.datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M")


def get_api_key() -> str:
    """
    Returns an api key for the Polygon.io API
    :return apiKey: str:
    """
    return os.environ["POLYGON_KEY"]


# TODO: Let user choose what symbol they are plotting/viewing/pulling
# TODO: Let user choose what adjustment scheme to apply to the data
# TODO: Let user choose what types of bars (1m, 1h, 1d, ...) they are requesting from the API
# TODO: Let function request partial date pull, less of a problem if I was using a database to cache these requests
def get_data(start_time, finish_time):
    """
    Calls the REST client API to pull in data from Polygon.io. See reference websites for examples and notes on API usage.
    :param finish_time: str
    :param start_time: str
    :return:    Array with raw record values
    :see reference: https://polygon.io/docs/getting-started
    :see reference: https://polygon.io/docs/get_v2_aggs_ticker__stocksTicker__range__multiplier___timespan___from___to__anchor
    :see reference: https://github.com/polygon-io/client-python
    """
    # TODO: The Polygon.io API accepts both Unix timestamps and strings, need to allow Unix timestamps too to request partial dates.
    with RESTClient(get_api_key()) as client:
        return client.stocks_equities_aggregates("AAPL", 1, "minute", start_time, finish_time, unadjusted = False)


def convert_to_df(data):
    """
    Convert the result JSON into a pandas dataframe and perform some basic formatting on it.
    :param data:    Ragged array returned by Polygon.io API request
    :type data:     TODO
    :return:        Formatted Pandas Dataframe representing time series of raw data returned by Polygon.io API pull
    :rtype:         Pandas.Dataframe
    """
    df = pd.DataFrame.from_records(data.results, index = "t")

    if DEBUG_MODE:
        print(df.head())
        print(df.info())

    df = df.reset_index()
    df = df.rename(index = str,
                   columns = {
                       "index": "idx", "t": "date", "o": "open", "h": "high", "l": "low", "c": "close", "v": "volume", "vw": "VWAP", "n": "Transactions"
                       })

    # Convert to datetime
    # df["date"] = pd.to_datetime(df["date"])
    df["date"] = pd.to_datetime(df["date"], unit = "ms")

    # Sort data according to date
    df = df.sort_values(by = ["date"])

    # Ensure the correct data types
    df.open = df.open.astype(float)
    df.close = df.close.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    df.volume = df.volume.astype(int)
    df.VWAP = df.VWAP.astype(float)
    df.Transactions = df.Transactions.astype(int)

    # Spit the dataframe back out to the user
    return df
