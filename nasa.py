import requests
import json

url = "https://api.nasa.gov/planetary/apod?api_key=m2zYmwlDszhiaZ1ikAsnu5KoJmWhu3uETyk1hOHx"
raw_response = requests.get(url)
img_url = raw_response.json()['url']
img = requests.get(img_url)
print("--------------------")
print(img.content)
raw_image = img.content
file = open(f'Desktop/nasa.jpg', 'wb')
file.write(raw_image)
