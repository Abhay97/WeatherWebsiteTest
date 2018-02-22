
import requests

def getWeather(City):
    where = 'http://api.wunderground.com/api/c23f7fd718aefd50/conditions/q/Canada/'+City+'.json'
    data = requests.get(where).json()
    return(data)

x=(getWeather('kanata'))
print(x)
