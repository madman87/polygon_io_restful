from dotenv import load_dotenv          
import os 
import datetime
from polygon import RESTClient
import pytz

load_dotenv()
API_KEY = os.environ.get('API_KEY')

print(API_KEY)

est=pytz.timezone("US/Eastern")
utc=pytz.utc


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = API_KEY
    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        from_ = "2021-01-01"
        to = "2021-02-01"
        resp = client.stocks_equities_aggregates("PTPI", 1, "minute", from_, to, unadjusted=False)

        print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")


if __name__ == '__main__':
    main()