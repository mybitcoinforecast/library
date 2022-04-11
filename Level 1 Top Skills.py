#Top Skill 1. Python Coding
#Import Python Libraries
import requests
from IPython.display import Image, display

#Top Skill 2. Get API Data
getMyApiData = requests.get("https://mybitcoinforecast.com/api/bitcoin-bull-bear-forecast/YOUR-API_KEY")
MyApiData = getMyApiData.json()

#Top Skill 3. Variables
MyApiDataToday = MyApiData[-1]
Points = MyApiDataToday['points']
BTCPrice = MyApiDataToday['price_close']

#Top Skill 4. If Statements
if Points > 50:
    BullBear = 'https://i.imgur.com/siL8Hak.png'
else: BullBear = 'https://i.imgur.com/KyM7b6o.png'

ExpectedReturn = round((-0.1129826611596502 + 0.0021708085870005087 * Points) * 1 * 100, 2)

print('Bitcoin Bull Bear Forecast')
display(Image(BullBear))
print('Points')
print(Points)
print('BTC Price')
print(BTCPrice)
print('Expected Return')
print(ExpectedReturn)
