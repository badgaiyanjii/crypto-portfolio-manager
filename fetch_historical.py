import yfinance as yf
import csv

EDA_COINS_FILE = "eda_coins.csv"
HISTORICAL_CSV = "historical_prices.csv"

PERIOD = "1y"
INTERVAL = "1d"

YAHOO_SYMBOLS = {
    "bitcoin":"BTC-USD",
    "ethereum":"ETH-USD",
    "binancecoin":"BNB-USD",
    "ripple":"XRP-USD",
    "solana":"SOL-USD",
    "cardano":"ADA-USD",
    "dogecoin":"DOGE-USD",
    "tron":"TRX-USD",
    "polkadot":"DOT-USD",
    "litecoin":"LTC-USD"
}

def load_eda_coins():

    coins = []

    with open(EDA_COINS_FILE) as f:

        reader = csv.DictReader(f)

        for row in reader:

            cid = row["coin_id"]

            if cid in YAHOO_SYMBOLS:
                coins.append((cid,YAHOO_SYMBOLS[cid]))

    return coins


def main():

    coins = load_eda_coins()

    with open(HISTORICAL_CSV,"w",newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "coin_id","date","open","high",
            "low","close","volume"
        ])

        for coin_id,symbol in coins:

            data = yf.download(
                symbol,
                period=PERIOD,
                interval=INTERVAL,
                progress=False
            )

            for index,row in data.iterrows():

                writer.writerow([
                    coin_id,
                    index.date(),
                    row["Open"],
                    row["High"],
                    row["Low"],
                    row["Close"],
                    row["Volume"]
                ])

    print("Historical data saved")


if __name__ == "__main__":
    main()