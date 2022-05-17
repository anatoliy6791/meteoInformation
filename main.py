import requests
s_city = "Moscow, RU"
appid = "ea7d7d1154a9bd17d45f79deadfb0456"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
