from flask import *
import json, time
import pandas as pd
import datetime as dt
from binance.spot import Spot as Client

app = Flask(__name__)

# getting btc data
api_key = "LS2FxhfRjqp6TOv3q2QFOGuQzU8KoSGwlcLIOVaxjRjc0UOhncD2ZRMzT4xRGsfu"
secret_key = "p3AHHm2sq26yV2y92y0XkFkDxNqE3AAPVphtslNzrmLAJOrMN3r5Gm8ohNolfsXn"
spot_client = Client(api_key, secret_key)
# spot_client = Client(base_url=base_url) if the other should fail

limit = 1000


@app.route("/", methods=["GET"])
def home_page():
    btcusd_historical = spot_client.klines("BTCUSDT", "1d", limit=limit)
    data_set = {"Page": "Home", "Time": time.time(), "Data": btcusd_historical}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route("/user/", methods=["GET"])
def user_page():
    user_query = str(request.args.get("coin"))  # /user/?user=USER_NAME
    timeframe_query = str(request.args.get("timeframe"))

    btcusd_historical = spot_client.klines(user_query, timeframe_query, limit=limit)
    data_set = {
        "Page": "Request",
        "Time": time.time(),
        "Data": btcusd_historical,
    }
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == "__main__":
    app.run(port=7777)
