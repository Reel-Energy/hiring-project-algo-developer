import numpy as np
import datetime as dt
from conf import MIN_SPREAD


def spread_monitor(prices: np.ndarray) -> tuple | None:
    """Takes the lowest priced offer and the highest priced bid from the current price vector.
    If the spread is above our threshold, we make a trade and return some trade info.

    :param prices: vector of bid and offer prices
    :return: tuple with trade info or None if no trade is performed
    """
    # we buy at the lowest offer price
    best_offer_product = np.argmin(prices[1])
    best_offer_price = prices[1, best_offer_product]
    # we sell at the highest priced bid price
    best_bid_product = np.argmax(prices[0])
    best_bid_price = prices[0, best_bid_product]

    if (best_bid_price - best_offer_price) > MIN_SPREAD:
        # we can make the trade!
        profit = best_bid_price - best_offer_price
        now = dt.datetime.now(dt.UTC)
        trade_info = (
            now,
            best_offer_product,
            best_offer_price,
            best_bid_product,
            best_bid_price,
            profit,
        )
        print("Making money! Trade info:", trade_info)
        return trade_info
