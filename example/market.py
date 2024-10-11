import time
import numpy as np
from conf import PRICE_MEAN, PRICE_STD, BID_ASK_SPREAD_BOUNDS, N_PRODUCTS
from strategy import spread_monitor


def get_bid_ask_prices(size: int = 1) -> np.ndarray:
    """Generates randomly distributed the bid and ask price matrix.

    :param size: number of products, defaults to 1
    :return: numpy array. Shape is (2, N_PRODUCTS) where the first element is the vector of
        bid prices and the second is offer prices
    """
    bid_price = np.random.randn(size) * PRICE_STD + PRICE_MEAN
    ask_price = bid_price + np.random.uniform(*BID_ASK_SPREAD_BOUNDS, size=size)
    prices = np.array([bid_price, ask_price]).round(2)
    return prices


if __name__ == "__main__":
    price_array = get_bid_ask_prices(size=N_PRODUCTS)
    trades = []
    while True:
        # some random product changes price
        i = np.random.randint(0, N_PRODUCTS)
        price_array[:, i] = get_bid_ask_prices(size=1)[:, 0]

        # we apply our strategy
        trade = spread_monitor(price_array)
        if trade is not None:
            trades.append(trades)

        # nothing happens for a random amount of time
        time.sleep(np.random.rand())
