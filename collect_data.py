import requests
import sqlite3
import csv

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
DB_NAME = "crypto.db"

SNAPSHOT_CSV = "market_snapshot.csv"
EDA_CSV = "eda_coins.csv"

YAHOO_SUPPORTED_COINS = {
    "bitcoin","ethereum","binancecoin","solana","ripple",
    "cardano","dogecoin","polkadot","litecoin","tron"
}

def fetch_market_snapshot():

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    return response.json()


def save_snapshot_csv(data):

    with open(SNAPSHOT_CSV,"w",newline="",encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "coin_id","symbol","name",
            "current_price","market_cap","last_updated"
        ])

        for coin in data:

            writer.writerow([
                coin["id"],
                coin["symbol"],
                coin["name"],
                coin.get("current_price",0),
                coin.get("market_cap",0),
                coin.get("last_updated","")
            ])


def select_eda_coins(data):

    selected = []

    for coin in data:

        if coin["id"] in YAHOO_SUPPORTED_COINS:
            selected.append(coin)

    return selected


def save_eda_csv(data):

    with open(EDA_CSV,"w",newline="",encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "coin_id","symbol","name",
            "current_price","market_cap"
        ])

        for coin in data:

            writer.writerow([
                coin["id"],
                coin["symbol"],
                coin["name"],
                coin.get("current_price",0),
                coin.get("market_cap",0)
            ])


def save_snapshot_to_db(data):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS market_snapshot")

    cur.execute("""
        CREATE TABLE market_snapshot(
        coin_id TEXT,
        symbol TEXT,
        name TEXT,
        current_price REAL,
        market_cap INTEGER,
        last_updated TEXT)
    """)

    rows = [
        (
            coin["id"],
            coin["symbol"],
            coin["name"],
            coin.get("current_price",0),
            coin.get("market_cap",0),
            coin.get("last_updated","")
        )
        for coin in data
    ]

    cur.executemany(
        "INSERT INTO market_snapshot VALUES (?,?,?,?,?,?)",
        rows
    )

    conn.commit()
    conn.close()


def main():

    data = fetch_market_snapshot()

    save_snapshot_csv(data)

    eda = select_eda_coins(data)

    save_eda_csv(eda)

    save_snapshot_to_db(data)

    print("Data pipeline completed")


if __name__ == "__main__":
    main()