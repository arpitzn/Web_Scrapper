import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.3987&lon=-99.4146#.YG6fGs_itPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week) 

items = (week.find_all(class_='tombstone-container'))


print(items[0].find(class_='period-name').get_text()) 
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
print(period_names)
short_desc = [item.find(class_='short-desc').get_text() for item in items]
print(short_desc)
temp = [item.find(class_='temp').get_text() for item in items]
print(temp)

weather_stuff = pd.DataFrame(
    {
        'period': period_names, 
        'short_descriptions': short_desc, 
        'temperatures':temp,
    })
print(weather_stuff)    

weather_stuff.to_csv('weather.csv')