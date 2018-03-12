# Dynamic Time Warped crptocurrency series
Applied dtaidistance to a set of time-series data (cryptocurrencies), followed by hierarchical clustering (top-down)

The main premise was to identify group-trajectories (independent of time) in cryptocurrencies; the suspicion was that the largest cluster would consist of alt-coins of dubious quality, and as such, display a momentum pattern reminiscent of a "pump-and-dump". 

* Bitcoin was removed from all analysis, as the premise of this study was to examine alt-coins specifically
* Date range was 1 year, Nov 2016 to Nov 2017
* Cryptos delisted in that time range, or facing upcoming delisting were not included in analysis

Process:
* Fetch JSON cryptocurrency data from Poloniex 
* Reduce dimensionality with pip (perceptually important points) to 100 data points; prices normalized to 0:100 scale 
* Use dynamic time warping as distance metric for clustering


![Dendrogram_cryptos](https://imgur.com/9QtISmd.jpg)

The clustering process identified three clusters among the 54 cryptocurrencies. Further investigation revealed significant variations in average market capitalisation value among clusters. The first cluster, C1 (left) has an average market capitalisation of $3294M USD, followed by $69M USD in the second cluster, C2, and the third cluster (C3) at $1009M USD. 
Further investigation reveals that C1 contained many high-profile cryptocurrencies, including Ethereum with a current market cap of $44 billion USD. Removing Ethereum from the calculation yields a market cap of $1070M USD, supporting the inference that C2 consists mostly of cryptocurrencies of declining quality. Below are figures describing summarized movements of each cluster shape using DTW averages.


![Cluster averages](https://imgur.com/pHp1Hbg.jpg)

![Comovement pairs](https://imgur.com/eTgbpvz.jpg)

The above plot visualises a clear pattern: DCR precedes LTC’s movements. In contrast, there is no recognizable co-movement relationship between DASH and PPC. These pairs that display sufficient time-lag may lend themselves well to arbitrage strategies. Additionally, and consistent with the findings of Aghabozorgi and Wah Teh (2014), the results have some benefit in risk management in that any dependencies between different cryptocurrencies are uncovered. An investor wishing to diversify her holdings can select cryptocurrencies that are not only uncorrelated, but also show no evidence of co-movement. 

However, it is important to consider that pairwise relationships between cryptocurrencies may change over time depending on the time range that these clusters were derived from, in addition to other fundamental factors. To truly assess the robustness of this application, sufficient backtesting will be necessary.
