import requests


response = requests.get('https://www.google.com')
html = response.text

print(html)
