# Technical Interview: Coding Exercise
## :money_with_wings: Build a simplified spread trading algorithm :money_with_wings:
### :bulb: Background
In this exercise you will be asked to develop a simulated trading algorithm in python. 

You should expect to put in roughly 3 to 4 hours on this exercise. If you realise you are taking longer, we recommend you stop and take a few notes on what you wanted to do more, and how you would have approached it.

The aims of the exercise are to assess:
- your general level of familiarity and skill with python
- your ability to mock a trading algorithm

At the interview, you will be asked to go through the code to explain how it works and elaborate on the choices you made along the way.

The algorithm monitors the spread across a number of products and performs trades on pairs when the spread (price difference) between the products in the pair is larger than a given threshold. 
The different products may represent different hours of the same day, or the price of power in the same hour but across different price regions.
You can read some information about power markets [here](https://www.epexspot.com/en/basicspowermarket) and see some real-world market results [here](https://data.nordpoolgroup.com/auction/day-ahead/prices). Note: your simulated algorithm should be simplified, so do not worry about trying to replicate how markets actually function.

In real life, this algorithm may represent the behavior of an energy storage trading algorithm which attempts to buy power with low-priced products and sell high-priced ones, charging the storage with cheap energy and discharging it when it's expensive. A minimum spread threshold ensures that the battery only runs when the profit from the trades is higher than the cost of cycling the battery and the degradation that it causes.

Another example of a real-world application of this kind of algorithm would be pairs trading, where statistical arbitrage is performed between pairs of products when their prices diverge and are (for some reason) expected to converge through mean reversion. In other words, one can speculate on the price difference between e.g. the price of power in Germany versus France, placing a bet that they will converge if they are currently trading too far apart from each other.

### :computer: The task

Your code should be split into (at least) 2 modules: 
- `market.py` simulates the behavior of the market by generating orders
- `strategy.py` contains the logic of your algorithm

Please write unit tests at least for `strategy.py`.
Include a short readme that explains how to run the code.
When running the code, both components should spin up and there should be some kind of way to verify that things are happening and trades are being performed, e.g. by printing to screen.

#### `market.py`
This module should contain some kind of method, class or endpoint that represents the state of the market (orderbook). 
This is essentially a matrix of *N* rows, each of them representing a different product, and 2 columns: one representing the price of the best bid (the price of the buy order that is priced the highest in the market, i.e. what you can immediately sell at) and the other one representing the best offer (the price of the sell order that is priced the lowest in the market, i.e. what you can immediately buy at). These prices should be distributed in some random way and change over time with some random time interval between changes, ideally different for every product. Make sure that for the same product (any row in the matrix) the best bid price is always lower than the best ask price. 
For this exercise we will ignore the volume component: we will assume that the market is infinitely liquid (i.e. you can trade as much as you want without directly influencing the price) and all trades have a size of 1 unit of volume.

#### `strategy.py`
This module should contain a method, class or endpoint that contains the logic for our trading algorithm. 
The logic is very simple: we want to continuously monitor the spread (price difference) between the best bid for any product and the best ask for any of the other products. If this spread for a given pair is larger than a fixed threshold, we want to make a trade, i.e. buy at the best ask and sell at the best bid. Make sure to keep track of the trades you perform, e.g. maintain a record as an attribute or your class or in a local file storage/database. 


### Example
In `/example/` you can find a short and simple example implementation. You can run it to see what happens (after installing requirements) by running the following command from the main repo directory.
```
python example/market.py
```

Feel free to use it as a starting point, but note that this is not mandatory! How can you improve on it?
A few suggestions:
- make it more realistic by simulating the market sending messages with price changes to a strategy listener
- use an asynchronous implementation
- refactor using classes

:sparkles: If you have a good idea on how do to this feel free to totally ignore the example and suggestions above, we really value creativity at Reel! :sparkles:

And remember tests :wink: