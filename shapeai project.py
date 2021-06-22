import requests
from datetime import datetime

api_key = '3a842c37e0d8a1ca7e538d3515647581'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %m %Y | %H:%M:%S %p")

#fetching information
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

#storing in a text file
f = open("weather report.txt", "a")
print ("-------------------------------------------------------------",file=f)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=f)
print ("-------------------------------------------------------------",file=f)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=f)
print ("Current weather desc  :",weather_desc,file=f)
print ("Current Humidity      :",hmdt, '%',file=f)
print ("Current wind speed    :",wind_spd ,'kmph',file=f)
f.close()
