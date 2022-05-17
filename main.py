import requests
s_city = "Moscow, RU"
appid = "ea7d7d1154a9bd17d45f79deadfb0456"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': s_city, 'units': 'metric', 'lang': 'ru','APPID': appid})
data = res.json()
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'])
    print("Дата <", i['dt_txt'], "> \r\nВидимость <", i['visibility'])
    print("____________________________")


