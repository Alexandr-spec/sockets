from urllib import request

url = "https://python.org"
#url = "https://httpforever.com"

with request.urlopen(url) as response:
    html = response.read()

print(f"Retrieved {len(html)} bytes")
print("First 50 characters:")
print(f"{str(html[:50])}")