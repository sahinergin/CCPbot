import tweepy
import time
import json
from urllib.request import urlopen

def get_api_access():
	"""
		Returns the authenticated API for tweepy.

		NOTE:
		The keys are not filled in because it is a private key.
		The consumer key and access token can be easily found for
		your twitter handle by going to app.twitter.com

	"""
	consumer_key = "LdGanePPg8C3Weg5h87P2Ci5S"
	consumer_secret = "Pnr7EpEKw9QGwgdqlnS4Xdi2ITzIutElFxnWvdMgbhMIqJRJGv"

	access_token = "1525894398-F1x0nALaw7XwrqQM3kuG0DRFHcEksI8YmS0olEN"
	access_token_secret = "loSnlMKar9TLRUu08wBlNz3XVJvHXEziiiRwIvcelrhNB"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def get_crypto_information():
	"""
		Retrieves the prices of the desired crypto through the
		coin market cap api.
	"""
	bitcoin_api = urlopen("https://api.coinmarketcap.com/v1/ticker/bitcoin")
	bitcoin_data = json.load(bitcoin_api)

	ethereum_api = urlopen("https://api.coinmarketcap.com/v1/ticker/ethereum")
	ethereum_data = json.load(ethereum_api)

	litecoin_api = urlopen("https://api.coinmarketcap.com/v1/ticker/litecoin")
	litecoin_data = json.load(litecoin_api)

	global_api = urlopen("https://api.coinmarketcap.com/v1/global/")
	global_data = json.load(global_api)


	bitcoin_price = '${0:.2f}'.format(float(bitcoin_data[0]['price_usd']))
	ethereum_price = '${0:.2f}'.format(float(ethereum_data[0]['price_usd']))
	litecoin_price = '${0:.2f}'.format(float(litecoin_data[0]['price_usd']))
	market_cap = '${}'.format(float(global_data['total_market_cap_usd']))
	btc_dominance = '%{}'.format(float(global_data['bitcoin_percentage_of_market_cap']))

	return bitcoin_price, ethereum_price, litecoin_price, market_cap, btc_dominance

api = get_api_access()

while True:
	#Sends a tweet out every 15 minutes FOREVER.
	bitcoin_price, ethereum_price, litecoin_price, market_cap, btc_dominance = get_crypto_information()
	message = " #BTC #Bitcoin: " + bitcoin_price + "\n#ETH #Ethereum: " + ethereum_price + "\n#LTC #Litecoin: " + litecoin_price + "\n#MarketCap: " + market_cap + "\n#BitcoinDominance: " + btc_dominance

	api.update_status(status=message)
	time.sleep(900)
