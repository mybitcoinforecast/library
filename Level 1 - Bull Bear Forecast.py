#Top skill 1. Python Coding
import requests
from IPython.display import Image, display

#Top skill 2. Import API Data
getYourApiData = requests.get("https://mybitcoinforecast.com/api/bitcoin-bull-bear-forecast/624cc5b8d9363a0052955381")
YourApiData = getYourApiData.json()

#Top skill 3. Variables
YourApiDataToday = YourApiData[-1]
Points = YourApiDataToday['points']

#Top skill 4. If Statements
if Points > 50:
    BullBear = 'https://i.imgur.com/siL8Hak.png'
else: BullBear = 'https://i.imgur.com/KyM7b6o.png'

ExpectedReturn = (-0.1129826611596502 + 0.0021708085870005087 * Points) * 1 * 100

print('Bitcoin Bull Bear Forecast')
print('Points')
print(Points)
display(Image(BullBear))
print('Expected Return')
print(ExpectedReturn)
