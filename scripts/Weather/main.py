import requests

city = input("Podaj miasto: ")
response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
print(f"Pogoda w {city}:", response.text)